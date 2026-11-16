import socket

HOST = "127.0.0.1"
PORTA = 5005

# Cria o socket utilizando IPv4 e TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORTA))

voto = input("Digite o seu voto: ")
voto = voto.encode()

cliente.sendall(voto)

mensagem = cliente.recv(1024)
mensagem = mensagem.decode()
print(mensagem)

cliente.close()
