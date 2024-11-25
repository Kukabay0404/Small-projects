import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket = ('127.0.0.1', 56789)
client_socket.connect(server_socket)
print('Покдлючено к серверу')

while True:
    message = input()
    client_socket.sendall(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    if not response:
        break
    print(f'Сервер ответил: {response}')

    response = ''

client_socket.close()