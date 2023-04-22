# 13


## 問題
> Cryptography can be easy, do you know what ROT13 is?   
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

> 暗号は簡単に出来ます。 ROT13をご存知ですか?  
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}


## ROT13とは
rotation 13ということで文字を13つ分回転させる。
いわゆるシーザー暗号の一つ。
フラグ形式から回転させるベースは大文字は大文字、小文字は小文字でアルファベット内で回すことがわかる。

## 回転させる

```python
from string import ascii_lowercase, ascii_uppercase

s="cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

low=list(ascii_lowercase)
up=list(ascii_uppercase)

l=len(low)
key=13

ans=""
for c in s:
    if c in low:
        ans+=low[(low.index(c)+key)%l]
    elif c in up:
        ans+=up[(up.index(c)+key)%l]
    else:
        ans+=c
print(ans)
```

大文字、小文字のリストを作り、それぞれで13文字ずらして解答へ、それらに当てはまらない場合は元の文字を解答へ連結する。

## 答え

```
picoCTF{not_too_bad_of_a_problem}
```
