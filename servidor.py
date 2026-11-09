import socket
import threading

HOST = "0.0.0.0"
PORTA =5005

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(HOST, PORTA)
servidor.listen()

conexao, endereco = servidor.accept()

print("Cliente conectado:", endereco)

mensagem = conexao.recv(1024)

mensagem.decode()

conexao.sendall("Voto recebido!".encode())

conexao.close()