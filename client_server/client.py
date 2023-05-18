import socket
import threading
from encrypt import do_decrypt, do_encrypt

def receiveMsg_thread(s):
    while True:
        # recebe a mensagem
        data = s.recv(1024)
        # verifica se a mensagem existe
        if not data:
            break

        msg = do_decrypt(data).decode("utf-8").strip()
        print(f'{msg}\nMensagem:')
    
    print("Conexão com o servidor encerrada")

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5003  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Envia uma mensagem para o servidor

print("Bem vindo ao chat!")
x = threading.Thread(target=receiveMsg_thread, args=(s, ))
x.setDaemon(True)
x.start()

while True:
    msg = input("\nMensagem:\n")
    encrypt_msg = do_encrypt(msg)
    s.sendall(encrypt_msg)

    if msg == 'stop':
        print("Client parando...")
        break

print("Finalizando execução...")
s.close()