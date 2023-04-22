from string import ascii_lowercase, ascii_uppercase

s="cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

low=list(ascii_lowercase)
up=list(ascii_uppercase)

l=len(low)

ans=""
for c in s:
    if c in low:
        ans+=low[(low.index(c)+13)%l]
    elif c in up:
        ans+=up[(up.index(c)+13)%l]
    else:
        ans+=c
print(ans)