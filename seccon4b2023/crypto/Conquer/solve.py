from random import getrandbits
from Crypto.Util.number import *
from flag import flag

def ROL(bits, N):
    for _ in range(N):
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits

def ROL_REVERSE(bits,N):
    N=N%length
    for _ in range(length-N):
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits

for i in range(-10,11):
    key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
    cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379


    length=cipher.bit_length()
    length+=i
    print("key =", key)
    print("cipher =", cipher)
    print("length =",length)
    cipher ^= key

    for j in range(32):
        key = ROL_REVERSE(key, pow(cipher, 3, length))
        cipher ^= key



    try:
        print(long_to_bytes(cipher).decode())
        print(i)
    except:
        pass

