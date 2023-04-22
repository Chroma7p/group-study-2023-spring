# caesar

## 問題
> Decrypt this message.

>このメッセージを解読してください。

```
picoCTF{dspttjohuifsvcjdpoabrkttds}
```

## 解く
問題名通りシーザー暗号と思われるので、1文字ずつずらしてみる

```python
from string import ascii_lowercase

cipher_txt="dspttjohuifsvcjdpoabrkttds"

low=list(ascii_lowercase)
l=len(low)


for i in range(26):
    ans=""
    for c in cipher_txt:
        ans+=low[(low.index(c)+i)%l]
    print(ans)
```

結果
```
dspttjohuifsvcjdpoabrkttds
etquukpivjgtwdkeqpbcsluuet
furvvlqjwkhuxelfrqcdtmvvfu
gvswwmrkxlivyfmgsrdeunwwgv
hwtxxnslymjwzgnhtsefvoxxhw
ixuyyotmznkxahoiutfgwpyyix
jyvzzpunaolybipjvughxqzzjy
kzwaaqvobpmzcjqkwvhiyraakz
laxbbrwpcqnadkrlxwijzsbbla
mbyccsxqdrobelsmyxjkatccmb
nczddtyrespcfmtnzyklbuddnc
odaeeuzsftqdgnuoazlmcveeod
pebffvatgurehovpbamndwffpe
qfcggwbuhvsfipwqcbnoexggqf
rgdhhxcviwtgjqxrdcopfyhhrg
sheiiydwjxuhkrysedpqgziish
tifjjzexkyvilsztfeqrhajjti
ujgkkafylzwjmtaugfrsibkkuj
vkhllbgzmaxknubvhgstjcllvk
wlimmchanbylovcwihtukdmmwl
xmjnndiboczmpwdxjiuvlennxm
ynkooejcpdanqxeykjvwmfooyn
zolppfkdqeboryfzlkwxngppzo
apmqqglerfcpszgamlxyohqqap
bqnrrhmfsgdqtahbnmyzpirrbq
crossingtherubiconzaqjsscr
```

他は単語になっていないので最後の`crossingtherubiconzaqjsscr`が答え

## 答え
```
picoCTF{crossingtherubiconzaqjsscr}
```

## 追記
crossing the rubiconで一つの慣用句らしい。  
ユリウス・カエサルが内乱を起こすときにルビコン川を渡ったことに由来する、もう後には引けない事を推し進めるようなことを言うらしい。  
この時、「alea iacta est（賽は投げられた）」も言ったらしい。