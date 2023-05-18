import socket
import threading
from encrypt import do_decrypt, do_encrypt

conns = []

def chat_thread(conn, addr):
    while True:
        # recebe a mensagem
        data = conn.recv(1024)
        # verifica se a mensagem existe
        if not data:
            break

        # encripta
        msg = do_decrypt(data).decode("utf-8") 
        print(f'from {addr} encrypted: {data}')
        resend_msg = do_encrypt('De '+str(addr)+': '+msg)
        # Envia uma resposta para o cliente
        for conn_ in conns:
            if conn == conn_:
                continue
            conn_.sendall(resend_msg)
        
        # caso a mensagem for 'stop', finaliza tal cliente
        if msg == 'stop':
            break

        # Fecha a conexão
    print(f"Encerrando {addr}...")
    conns.remove(conn)
    conn.close()

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5003  # Porta que o servidor vai escutar

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