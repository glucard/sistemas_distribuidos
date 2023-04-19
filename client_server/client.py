import socket
import threading
from Crypto.Cipher import AES

key = b'Sixteen byte key'

def receiveMsg_thread(s):
    print(s)
    while True:
        data = s.recv(1024)
        msg = do_decrypt(data)
        print(f'Mensagem recebida: {msg}, encrypted: {data}')

def do_encrypt(msg):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')

    while len(bytes(msg, encoding='utf-8')) % 16 != 0:
        msg = msg + ' '
    ciphertext = obj.encrypt(msg)

    return ciphertext

def do_decrypt(ciphertext):
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')

    message = obj2.decrypt(ciphertext)
    return message

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Envia uma mensagem para o servidor

x = threading.Thread(target=receiveMsg_thread, args=(s, ))
x.setDaemon(True)
x.start()
while True:
    msg = input("Mensagem: ")
    encrypt_msg = do_encrypt(msg)
    s.sendall(encrypt_msg)

    if msg == 'stop':
        print("Client parando...")
        break

s.close()