# sum-o-primes

> We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

```python
p = get_prime(1024)
q = get_prime(1024)

x = p + q
n = p * q

e = 65537

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)

c = pow(FLAG, e, n)

print(f'x = {x:x}')
print(f'n = {n:x}')
print(f'c = {c:x}')

```

問題文通り、RSA暗号におけるpとqの和であるxを表示している。

つまり、2数の和と積が存在しているため、元の数を推測できる。
(解と係数の関係)

```
ax^2+bx+c=0の解をalpha,betaとしたとき
alpha+beta=-b/a
alpha*beta=c/a
```
つまりaを1で固定して置き換えた
```
x^2-(alpha+beta)*x+(alpha*beta)=0
-> x^2-(p+q)*x+(p*q)=0
```
の解がp及びqとなる


後は解の公式に突っ込んで計算
```
p=(x+math.isqrt(x**2-4*n))//2
q=n//p

```

数字から文字に戻すのはこれが楽っぽい
```
print(bytes.fromhex(hex(m)[2:]).decode())
```

## 答え
```
picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_24929c45}
```
please no give congruence of squares

