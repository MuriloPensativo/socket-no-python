import socket

HOST = '127.0.0.1'
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

namefile = str(input('Escreva o nome do arquivo a ser enviado: '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while True:
        data = client.recv(250000000)
        if not data:
            break
        file.write(data)

print(f'Arquivo "{namefile}" recebido.')