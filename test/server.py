import socket
import threading

# Dictionary to store client sockets and their corresponding usernames
clients = {}

def handle_client(client_socket, username):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.startswith('@'):  # Private message
            recipient, private_message = message[1:].split(':', 1)
            if recipient in clients:
                recipient_socket = clients[recipient]
                recipient_socket.send(f'Private message from {username}: {private_message}'.encode('utf-8'))
            else:
                client_socket.send(f"Recipient '{recipient}' not found.".encode('utf-8'))
        elif message == 'bye':
            break
        else:  # Broadcast message
            broadcast_message = f'{username}: {message}'
            broadcast_to_all(broadcast_message.encode('utf-8'))

    client_socket.close()
    del clients[username]

def broadcast_to_all(message):
    for client_socket in clients.values():
        client_socket.send(message)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print("Server started. Listening on port 8000.")

    while True:
        client_socket, address = server_socket.accept()
        username = client_socket.recv(1024).decode('utf-8')
        print("Connected to client:", username)
        clients[username] = client_socket
        threading.Thread(target=handle_client, args=(client_socket, username)).start()

start_server()
