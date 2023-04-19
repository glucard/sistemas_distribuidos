import socket
import threading
from Crypto.Cipher import AES

key = b'Sixteen byte key'

conns = []

def chat_thread(conn, addr):
    while True:
        data = conn.recv(1024)
        msg = do_decrypt(data)
        print(f'Mensagem recebida: {msg}, encrypted: {data}')
        
        # Envia uma resposta para o cliente
        for conn_ in conns:
            if conn == conn_:
                continue
            conn_.sendall(data)
        if msg == 'stop':
            conn.sendall('Servidor parando...'.encode())
            break

        # Fecha a conexão
    conn.close()


def do_encrypt(msg):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(msg)
    return ciphertext

def do_decrypt(ciphertext):
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    message = obj2.decrypt(ciphertext)
    return message


HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta que o servidor vai escutar

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o objeto socket ao endereço e porta especificados
s.bind((HOST, PORT))

# Define o limite máximo de conexões simultâneas
s.listen(5)

print(f'Servidor escutando na porta {PORT}...')

# Aguarda uma conexão

while True:
    conn, addr = s.accept()
    conns.append(conn)
    print(f'Conectado por {addr}')  
    x = threading.Thread(target = chat_thread, args=(conn, addr,))
    x.setDaemon(True)
    x.start()