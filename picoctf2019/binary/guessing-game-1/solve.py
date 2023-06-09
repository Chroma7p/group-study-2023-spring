import socket
import time
ip='jupiter.challenges.picoctf.org'
port=42953
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((ip, port))
time.sleep(1)
print(sc.recv(1024))

for i in range(1000):
    sc.sendall("1\n".encode("utf-8"))
    print(f"{i}:{sc.recv(1024)}")
    time.sleep(0.2)
