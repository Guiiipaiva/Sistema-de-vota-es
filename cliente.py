import socket

# Pede o IP do computador onde o servidor.py está rodando
HOST = input("Digite o IP do servidor (ou Enter para 127.0.0.1): ").strip() or "127.0.0.1"
PORTA = 5005

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((HOST, PORTA))

    voto = input("Digite o seu voto (1, 2 ou 3): ")
    cliente.sendall(voto.encode())

    mensagem = cliente.recv(1024).decode()
    print("\n" + mensagem)

except ConnectionRefusedError:
    print("Erro: Não foi possível conectar. Verifique se o servidor está rodando e se o IP está correto.")
except TimeoutError:
    print("Erro: Tempo esgotado. Verifique o firewall ou se os computadores estão na mesma rede.")
finally:
    cliente.close()
