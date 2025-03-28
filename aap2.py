import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                break
            print(msg)
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input("")
        if message.lower() == "exit":
            break
        client.send(message.encode('utf-8'))

    client.close()

start_client()