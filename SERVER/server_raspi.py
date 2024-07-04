from datetime import datetime
import socket
from threading import Thread
import time
from people import People
from cloud import FBDB
import json
import struct

class Server:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  
        self.is_running = True
        print(f"Server listening on {self.host}:{self.port}")
        self.people = People()
        self.cloud = FBDB()

    def start(self):
        try:
            while self.is_running:
                client_socket, client_address = self.server_socket.accept()
                print(f"Connection from {client_address}")
                client_thread = Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            self.close()

    def handle_client(self, client_socket):
        try:
            while True:
                message = client_socket.recv(1024).decode()

                if not message:
                    break
                
                if message == 'people_count':
                    response = self.people.get_count()
                    client_socket.send(str(response).encode())
                
                elif message == 'UIdata':
                    status_data = self.cloud.get()
                    status_data = json.dumps(status_data)
                    message_length = struct.pack('>I', len(status_data))
                    client_socket.sendall(message_length + status_data.encode())
                
                else:
                    values = message.split(" ")
                    data = {
                        'time': datetime.now().strftime("%d/%m/%Y - %I:%M:%S %p"),
                        'temp_value': values[1], 
                        'fan_speed': values[2],
                        'people_count': values[3]
                        }
                    self.cloud.push('status', data)
                    client_socket.send("UPLOADED".encode())
                
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()
            print("Client disconnected")

    def close(self):
        self.is_running = False
        self.server_socket.close()
        print("Server socket closed")

if __name__ == "__main__":
    server = Server()
    try:
        server.start()
    except KeyboardInterrupt:
        server.close()
