import socket
import threading

def recieve_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print('\n' + message.decode('utf-8'))
        except KeyboardInterrupt:
            print('Отключено от сервера!')
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 13123))
    print(f'Подключено к серверу!')

    recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
    recieve_thread.start()

    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                print('Отключение от сервера...')
                client_socket.close()
                break

            client_socket.sendall(message.encode('utf-8'))
    except KeyboardInterrupt:
        print('Принудительное отключение клиента')
        client_socket.close()

start_client()

