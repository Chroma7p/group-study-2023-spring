from string import ascii_lowercase

cipher_txt="dspttjohuifsvcjdpoabrkttds"

low=list(ascii_lowercase)
l=len(low)


for i in range(26):
    ans=""
    for c in cipher_txt:
        ans+=low[(low.index(c)+i)%l]
    print(ans)
