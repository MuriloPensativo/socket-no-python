import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão...')

conn, address = s.accept()
print('conectado na porta ', address)

while 1:
    data = conn.recv(1024)
    if not data:
        print('fechando a conexão')
        conn.close()
        break
    conn.sendall(data)