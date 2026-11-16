import socket
import threading

HOST = "0.0.0.0"
PORTA = 5005

# Cria o socket utilizando IPv4 e TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORTA))

votos = {
    "1": 0,
    "2": 0,
    "3": 0
}

# Bloqueio para evitar que duas threads alterem os votos ao mesmo tempo
lock = threading.Lock()

def atender_cliente(conexao, endereco):
    print("Cliente conectado:", endereco)

    mensagem = conexao.recv(1024)

    mensagem = mensagem.decode()
    mensagem = mensagem.strip()

    if mensagem in votos:

        # Protege a atualizacao dos votos e a montagem da apuracao
        with lock:
            votos[mensagem] += 1

            # Monta a apuracao com a quantidade de votos de cada candidato
            resultado = []
            for candidato, quantidade in votos.items():
                resultado.append(f"Candidato {candidato}: {quantidade}")

            mensagem = "Voto recebido!\n" + "\n".join(resultado)

        # Envia a confirmacao e a apuracao para o cliente
        conexao.sendall(mensagem.encode())

    else:
        # Informa ao cliente que o voto enviado nao e valido
        conexao.sendall("Voto invalido!".encode())

    # Encerra a conexao com esse cliente
    conexao.close()


while True:

    # Aceita uma nova conexao e obtem o endereco do cliente
    conexao, endereco = servidor.accept()

    # Cria uma thread para atender o cliente sem bloquear os demais
    threading.Thread(
        target=atender_cliente,
        args=(conexao, endereco)
    ).start()
