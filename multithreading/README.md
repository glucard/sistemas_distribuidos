# Multithreading DDOS chat client-server
### Requirements:
 `pip install matplotlib psutil`
### How to use:
    excute server.py first
    then, after, execute client.py
    after client.py finished its execution, enter `quit` in server.py prompt line

### Report
 In this experiments I used a server to receive multiple connections from different clients.
 In total 1000 threads were created to simulate different 'users', each thread is programmed to send 100 random messages, total of 100_000 (100*1000) messages.
 The total bytes received from the server was 27512540 bytes.
 Here is a graph showing the memory usage in Gbs and the CPU usage in percentage (%).
 where the X axis is the time.
![usage](https://github.com/glucard/sistemas_distribuidos/blob/main/multithreading/imgs/usage.png)
![quit_received](https://github.com/glucard/sistemas_distribuidos/blob/main/multithreading/imgs/quitreceived.png)
