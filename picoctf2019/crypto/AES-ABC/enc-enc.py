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

def enc(data):
    data=data.hex().encode("utf-8")
    return data

with open('body.enc.ppm', 'rb') as f:
    header, data = parse_header_ppm(f)
    data=enc(data)

with open('body.enc2.ppm', 'wb') as f2:
    f2.write(header)
    f2.write(data)