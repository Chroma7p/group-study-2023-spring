from string import ascii_uppercase

cipher_txt="UFJKXQZQUNB"
key="SOLVECRYPTO"

alp=list(ascii_uppercase)

l=len(alp)

ans=""
for i in range(len(s1)):
    ans+=alp[(l+alp.index(cipher_txt[i])-alp.index(key[i]))%l]
print(ans)



