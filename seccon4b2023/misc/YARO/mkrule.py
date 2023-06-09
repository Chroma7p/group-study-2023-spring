

import socket
import time

# サーバーに接続
ip='yaro.beginners.seccon.games'
port=5003



rule="""\
rule {CHAR} {
    strings:
        ${CHAR} = "{CHAR}"
    condition:
        ${CHAR}
}
"""
alp1="abcdef"
alp11="ghijkl"
alp2="nopqrs"
alp22="tuvwxyz"
alp3="ABCDEF"
alp33="GHIJKL"
alp4="NOPQRS"
alp44="TUVWXYZ"
alp5="012345"
alp55="6789{}_"
ans=[]

def search(char1,alp):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((ip, port))
    sc.recv(4096)
    rules=""
    for char2 in alp:
        rules+=rule.replace("{CHAR}", char1+char2)
    rules+="\n"
    sc.sendall(rules.encode())

    res = sc.recv(4096)
    dec=res.decode()
    resspr=dec.split("\n")
    #print(dec.split("\n")[-5:])
    for i in resspr[-10:]:
        if "flag.txt" in i and "Found" in i:
            ans.append(i.split(":")[2].strip(" "))
            print(ans)
            break
    time.sleep(1)

alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"

for i in alp:
    for j in alp:
        print(i+j)
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sc.connect((ip, port))
        sc.recv(4096)
        nrule=rule.replace("{CHAR}", i+j)
        sc.sendall(nrule.encode())
        res = sc.recv(4096)
        dec=res.decode()
        resspr=dec.split("\n")
        #print(dec.split("\n")[-5:])
        for x in resspr[-10:]:
            if "flag.txt" in x and "Found" in x:
                ans.append(x.split(":")[2].strip(" "))
                print(ans)
                break
        time.sleep(1)

print(ans)
    
    

