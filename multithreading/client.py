import socket
import threading
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def handle_client():
    i = 0
    host = "localhost"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    connected = True
    while connected and i < 1000:
        i += 1
        msg = get_random_string(random.randint(3,20))
        client.sendall(msg.encode())

    msg = client.recv(1024)
    print(f"{msg.decode()}")

    client.sendall("quit".encode())
    client.close()

threads = []
for i in range(100):
    thread = threading.Thread(target=handle_client)
    thread.daemon = True
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print("ended")