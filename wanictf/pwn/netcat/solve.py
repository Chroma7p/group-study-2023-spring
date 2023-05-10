

from netcat import Netcat
import time

# start a new Netcat() instance
nc = Netcat('netcat-pwn.wanictf.org', 9001)

for i in range(100):
    time.sleep(0.2)
    read_txt=nc.read().decode("utf-8")
    time.sleep(0.2)
    print(read_txt+"\n"+"- "*20)
    for s in read_txt.split("\n"):
        try:
            s=s.split(" ")
            ans=int(s[0])+int(s[2])
            nc.write(ans)
        except:
            pass
print(nc.read().decode("utf-8")+"\n"+"- "*20)
nc.write("ls")
time.sleep(0.2)
print(nc.read().decode("utf-8")+"\n"+"- "*20)

