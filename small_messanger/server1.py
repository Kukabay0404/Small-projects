import socket
import threading

clients = []

def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.sendall(message)
            except:
                clients.remove(client_socket)


def handle_clients(client_socket, client_address):
    print(f'Клиент {client_address} подключен!')
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break

            print(f'От клиента {client_address}: {message.decode('utf-8')}')

            broadcast(message, client_socket)
    except ConnectionResetError:
        print(f'Клиент {client_address} отключился!')
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()
        print(f'Клиент {client_address} отключен!')


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 13123))
    server_socket.listen(5)
    print('Сервер в ожидании клиентов!')

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_clients, args=(client_socket, client_address))
        client_thread.start()

start_server()
