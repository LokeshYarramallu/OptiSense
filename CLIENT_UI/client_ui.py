import socket
from flask import Flask, render_template, jsonify
import json
import struct

app = Flask(__name__)

received_data = None

@app.route('/')
def index():
    return render_template('index.html', data=received_data)

@app.route('/api/data')
def get_data():
    return jsonify(received_data)

class UI_client:
    def __init__(self, server_ip='192.168.137.69', port=65432):
        self.server_ip = server_ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.client_socket.connect((self.server_ip, self.port))
        print(f"Connected to server at {self.server_ip}:{self.port}")

    def receive_data(self):
        global received_data
        self.client_socket.send("UIdata".encode())

        message_length = self.client_socket.recv(4)
        message_length = struct.unpack('>I', message_length)[0]
        response = b""

        while len(response) < message_length:
            part = self.client_socket.recv(message_length - len(response))
            if not part:
                break
            response += part

        received_data = response.decode()
        print("Receiving Success")
        try:
            received_data = json.loads(received_data)
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            return None
        return received_data

    def close_connection(self):
        self.client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    client = UI_client()

    try:
        received_data = client.receive_data()  
        app.run(debug=True)  
    except KeyboardInterrupt:
        client.close_connection()
