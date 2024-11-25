import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12453))
server_socket.listen(1)

print('Сервер ожидает клиента!')
client_socket, client_address = server_socket.accept()
print(f'Клиент покдлючисля {client_address}')

while True:
    data = client_socket.recv(1024).decode('utf-8')
    if data == '1':
        break
    print(f'Клиент отправил вам сообщение {data}')

    data = ''

    response = input('Введите сообщение: ')
    client_socket.sendall(response.encode('utf-8'))

client_socket.close()
server_socket.close()
print('Сервер закрыт!')