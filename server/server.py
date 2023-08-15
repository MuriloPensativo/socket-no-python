import socket

HOST = 'localhost'
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)
print('Aguardando conexão...')

connection, address = server.accept()
print('conectado na porta ', address)

namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)
    print('Envio concluído')
