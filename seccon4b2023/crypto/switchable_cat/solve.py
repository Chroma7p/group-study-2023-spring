from Crypto.Util.number import *
from random import getrandbits
from os import urandom

seed = 219857298424504813337494024829602082766
cipher = 38366804914662571886103192955255674055487701488717997084670307464411166461113108822142059

class LFSR:
    """
    

    """
    def __init__(self):
        self.bits = 128
        self.rr = seed
        self.switch = 0
    def next(self):

        r = self.rr
        if self.switch == 0:
            b = ((r >> 0) & 1) ^ \
                ((r >> 2) & 1) ^ \
                ((r >> 4) & 1) ^ \
                ((r >> 6) & 1) ^ \
                ((r >> 9) & 1)
        if self.switch == 1:
            b = ((r >> 1) & 1) ^ \
                ((r >> 5) & 1) ^ \
                ((r >> 7) & 1) ^ \
                ((r >> 8) & 1)
        r = (r >> 1) + (b << (self.bits - 1))
        self.rr = r
        self.switch = 1 - self.switch
        return r & 1
    
    def gen_randbits(self, bits):
        key = 0
        for i in range(bits):
            key <<= 1
            key += self.next()
        return key
    
lfsr=LFSR()
s=set()
key=0
flen=(len(long_to_bytes(cipher))*8)
print(flen)
while 1:
    key<<=1
    key+=lfsr.next()
    key%=2**flen
    plain=cipher^key
    try:
        print(long_to_bytes(plain))
        if b"ctf4b" in long_to_bytes(plain):
            break
    except:
        #print(key)
        pass