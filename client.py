import socket

def main():
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    # connection to hostname on the port.
    client_socket.connect(('localhost', 12345))

    # Receive no more than 1024 bytes
    msg = client_socket.recv(1024)

    client_socket.close()

    print(msg.decode('ascii'))

if __name__ == '__main__':
    main()
