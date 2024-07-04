import tkinter as tk
from tkinter import Label
import socket
from PIL import Image, ImageTk
import time
from AC import AC

class AC_Client:
    def __init__(self, root, host='192.168.137.69', port=65432, people_per_degree=2):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.last_people_count = 0
        self.people_per_degree = people_per_degree
        self.ac = AC()
        self.cloud_time = time.time()

        self.root = root
        self.root.title("AC Control Panel")
        
        self.ac_image = ImageTk.PhotoImage(Image.open("ac_image.jpg"))  
        self.ac_image_label = Label(root, image=self.ac_image)
        self.ac_image_label.pack()

        self.status_label = Label(root, text="AC is turned on !!!", font=("Helvetica", 16))
        self.status_label.pack(pady=20)

    def update_status(self):
        status_text = self.ac.get_status().split(" ")
        self.status_label.config(text=f'Temperature :{status_text[1]} | Fan Speed : {status_text[2]} | People in the Hall : {self.last_people_count}')
        self.root.update()

    def begin(self, update_delay=5, status_delay=10):
        try:
            while True:
                if time.time() - self.cloud_time > status_delay:
                    status = self.ac.get_status()
                    status += str(self.last_people_count)
                    self.client_socket.sendall(status.encode())
                    response = self.client_socket.recv(1024).decode()
                    self.cloud_time = time.time()
                    time.sleep(3)

                message = "people_count"
                self.client_socket.sendall(message.encode())
                response = self.client_socket.recv(1024).decode()
                print(f"Number of people and status : {response} - {self.ac.get_status()}")

                try:
                    current_ppl = int(response)
                except ValueError:
                    print("not integer from server ", response)
                    continue

                diff = current_ppl - self.last_people_count
                temp_to_change = diff // self.people_per_degree

                if temp_to_change > 0:
                    self.ac.decrease_temperature(temp_to_change)
                elif temp_to_change < 0:
                    self.ac.increase_temperature(-temp_to_change)

                self.last_people_count = current_ppl
                self.update_status()
                time.sleep(update_delay)

        except ConnectionAbortedError as e:
            print(f"Connection aborted: {e}")
        except ConnectionResetError as e:
            print(f"Connection reset by peer: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    root = tk.Tk()
    client = AC_Client(root, people_per_degree=1)
    
    import threading
    client_thread = threading.Thread(target=client.begin)
    client_thread.start()

    root.mainloop()
