import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()

    def run(self):
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"New client connected from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # TODO: Implement logic for handling client communication
        pass

if __name__ == '__main__':
    server = Server(host='localhost', port=8000)
    server.run()
