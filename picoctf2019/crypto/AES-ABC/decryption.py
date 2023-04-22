import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n

    decoded = s_n

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0: 
        decoded = "0" * (BLOCK_SIZE - pad) + decoded
    return decoded

def decyption(s):
    s=s.hex()
    #1byte(8bit)の文字をhexに変換しているのでblock_sizeが2倍になる
    blocks=[int(s[i*2*BLOCK_SIZE:(i+1)*2*BLOCK_SIZE],16) for i in range(len(s)//(BLOCK_SIZE*2))]
    for i in range(len(blocks)-1,0,-1):
        prev_blk=blocks[i-1]
        curr_blk=blocks[i]
        n_curr_blk=(UMAX+curr_blk-prev_blk)%UMAX
        blocks[i]=n_curr_blk
        #print(blocks[i])

    blocks=[to_bytes(i) for i in blocks]
    return "".join(blocks[1:])

def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index(b'\n') + 1], s[s.index(b'\n')+1:]

def parse_header_ppm(f):
    data = f.read()
    #print(data)

    header = b""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data

with open('body.enc.ppm', 'rb') as f:
    header, data = parse_header_ppm(f)
    data=decyption(data)

with open('body.dec.ppm', 'wb') as f2:
    f2.write(header)
    f2.write(data.encode())