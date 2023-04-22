# Easy 1

## 問題
>The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

>ワンタイムパッドは暗号的に安全であっても、鍵を知っているとそうはいきません。あなたはこれを解くことができますか？SOLVECRYPTOの鍵でUFJKXQZQUNBを得るために、暗号化された旗と鍵、そして表をお渡ししました。この表を使って解くことができるでしょうか？

```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

いわゆるヴィジュネル暗号。
おそらくシーザー暗号に次いで有名な秘密鍵暗号方式の一つ。

```
???????????
UFJKXQZQUNB
     ↓
SOLVECRYPTO
```
というわけである。

暗号化の手順はアルファベットの配列を考えたときに
```
(平文のN文字目のインデックス+鍵のN文字目のインデックス)%26=暗号文のN文字目のインデックス
```
になる。

逆の手順を踏むなら

(26+暗号文のN文字目のインデックス-鍵のN文字目のインデックス)%26=平文のN文字目のインデックス

となり、機械的に解読できる。


```Python
from string import ascii_uppercase

cipher_txt="UFJKXQZQUNB"
key="SOLVECRYPTO"

alp=list(ascii_uppercase)

l=len(alp)

ans=""
for i in range(len(s1)):
    ans+=alp[(l+alp.index(cipher_txt[i])-alp.index(key[i]))%l]
print(ans)

```

この書き方はシーザー暗号などでも応用できるので、覚えておくと楽

## 答え

```
picoCTF{CRYPTOISFUN}
```