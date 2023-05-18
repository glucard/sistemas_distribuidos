import socket
import threading
# Importing the library
import psutil
from sys import getsizeof
from matplotlib import pyplot as plt
 
# Calling psutil.cpu_precent() for 4 seconds

class Server:
    def __init__(self, host, port):
        self.host = "localhost"
        self.port = 12345

        self.cpu_ps = []
        self.memory_ps = []
        self.net_ps = []
        self.received = 0

        self.threads = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))

    def start(self):

        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.host}:{self.port}.")

        handles = [self.handle_report]
        for h in handles:
            thread = threading.Thread(target=h)
            thread.daemon = True
            thread.start()
            self.threads.append(thread)

        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        while True:
            msg = conn.recv(1024)
            if not msg or msg == b"quit":
                break
            else:
                self.received += getsizeof(msg)
                #print(f"[{addr}] {msg.decode()}")
                conn.sendall(msg[::-1])

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

    def handle_report(self):
        while True:
            self.cpu_ps.append(psutil.cpu_percent(1))
            self.memory_ps.append(psutil.virtual_memory()[3]/1000000000)
            self.net_ps.append(psutil.net_io_counters().bytes_sent / (1024 ** 2))

host = "localhost"
port = 12345
server = Server(host, port)
t = threading.Thread(target=server.start, daemon=True)
t.start()

while True:
    s = input("Command:")
    if s == 'quit':
        print(f"{server.received} bytes received")
        break


plt.subplot(3, 1, 1)
plt.plot(server.cpu_ps, label="CPU usage")
plt.ylabel('CPU usage (%)')
#plt.xticks()

plt.subplot(3, 1, 2)
plt.plot(server.memory_ps, label="Memory usage")
plt.ylabel('Memory (Gbs)')

plt.subplot(3, 1, 3)
plt.plot(server.net_ps, label="Network usage")
plt.ylabel('Network usage (Gbs)')
plt.show()