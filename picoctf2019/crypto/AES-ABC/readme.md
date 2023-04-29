# AES-ABC

## 問題文

> AES-ECB is bad, so I rolled my own cipher block chaining mechanism - Addition Block Chaining!  
> You can find the source here: aes-abc.py.  
> The AES-ABC flag is body.enc.ppm

> AES-ECBはダメなので、独自のブロックチェーン暗号機構 - Addition Block Chainingを開発しました！  
> ソースはこちら：aes-abc.py  
> AES-ABCのフラグはbody.enc.ppm

## .ppmってなに
参考: [碧色工房 - PNM(PPM/PGM/PBM)ファイルフォーマット](https://www.mm2d.net/main/prog/c/image_io-01.html)  


Portable Pixmap Format
画像ファイルの形式の一つ。  
ヘッダーが以下のように構成されている。
```
P<x>
<width> <height>
<max>
```
`P<x>`が形式を表すマジックナンバーになっている。
今回はP6でPPMのバイナリ形式であることを示している。  
`<width>`,`<height>`は画像の横幅縦幅を示している。  
`<max>`は色を示す値の最大値。今回は255。

それ以降にデータが記述されているが1行のデータ列になっており、widthとheightによって画像の形が決まる。
1byteで1色、3byteで1ピクセルを表す

## AES-ECBってなに
### AESとは
Advanced Encryption Standard  
共通鍵暗号方式のブロック暗号(平文をある程度の長さに区切ってそのブロックごとに暗号化する)の一つ。
aes-abc.pyの8行目の`BLOCK_SIZE = 16`が今回のブロックの大きさになる。
これはブロック長が16byteであることを示す。
鍵の長さも同じになる。
ブロックと鍵をNbyte*Nbyteの行列とみなして様々な計算を通し暗号化する。
とてもそう簡単に破れるものではない。

### ECBとは
Electronic CodeBook  
ブロック暗号における暗号化のモードの一つ。
単純にブロックごとに区切ってそれを鍵に基づいて暗号化するだけのモード。
同じ鍵に対して同じブロックは同じ結果となるため、同じブロックが続く平文などでは特に内容の推測が容易になってしまうので、`AES-ECB is bad`なのである。
画像に対して行うと、形式によるが同じ色が広く使われている部分において**同じブロックが同じ結果**になり、色は変われど**中の情報をある程度見ることが出来る**可能性がある。

### つまり
この問題はppmの画像をAESの変換に加えて何らかの操作(block-chaining)を加えて暗号化したので、それをAESで暗号化したところまで戻してflag入りの画像を覗こうという問題と思われる。


## aes-abc.pyを見てみる
### メイン部分

```python
if __name__=="__main__":
    with open('flag.ppm', 'rb') as f:
        header, data = parse_header_ppm(f)
    
    iv, c_img, ct = aes_abc_encrypt(data)

    with open('body.enc.ppm', 'wb') as fw:
        fw.write(header)
        fw.write(c_img)

```

flag.ppmのファイルポインタをparse_header_ppmに渡しheaderを取り出した後、dataを暗号化してbody.enc.ppmにheaderと暗号を書き出している。
つまり、暗号化されたbody.enc.ppmからflag.ppmを復元することが目的となる。

### headerの切り離し

```python
def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n')+1:]


def parse_header_ppm(f):
    data = f.read()

    header = ""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data
```

最初の3行をheaderとして切り出している。
headerは取り出したものがそのまま保存されているのでこれはflag.ppmと共通であることがわかる。

### 暗号化部分

```python 
def aes_abc_encrypt(pt):
    cipher = AES.new(KEY, AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt)) # padで長さがBLOCK_SIZEの倍数になるように穴埋めして暗号化

    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)] # ブロックごとに分割
    iv = os.urandom(16) # 長さ16のランダムなバイト列を生成
    blocks.insert(0, iv) # それを先頭に挿入
    
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16) # 前のブロック
        curr_blk = int(blocks[i+1].encode('hex'), 16) # 今のブロック

        n_curr_blk = (prev_blk + curr_blk) % UMAX # 二つのブロックを足して16byteにするために剰余を取る
        blocks[i+1] = to_bytes(n_curr_blk) #それをto_bytesを通してbyte列に変換して次のブロックに格納

    ct_abc = "".join(blocks)
 
    return iv, ct_abc, ct
```

分割したブロックを連鎖的に足していっているが、最初のブロックはそのままになっているので、そこから逆の操作を行っていけばとりあえず ほぼAES直後に戻せそう……?

AES-ABCの特徴的に画像なら情報が残ってそうなので戻してみる。

## AES後まで戻す

```python
def decyption(s):
    s=s.hex()
    #1byte(8bit)の文字をhexに変換しているのでblock_sizeが2倍になる
    blocks=[int(s[i*2*BLOCK_SIZE:(i+1)*2*BLOCK_SIZE],16) for i in range(len(s)//(BLOCK_SIZE*2))]
    # それぞれのブロックに対し後ろから
    for i in range(len(blocks)-1,0,-1):
        prev_blk=blocks[i-1] # ひとつ前のブロック
        curr_blk=blocks[i]   # 今のブロック
        n_curr_blk=(UMAX+curr_blk-prev_blk)%UMAX # 今のブロックから前のブロック分引く
        blocks[i]=n_curr_blk # その値を今のブロック部分に格納
        
    blocks=[to_bytes(i) for i in blocks] #各ブロックを文字列に戻す
    return "".join(blocks[1:]) # ブロックを合体させる
```

暗号化では各ブロックを a,b,cとしたとき、
```
0   1     2
------------
a   b     c
a a+b     c    1=0+1
a a+b a+b+c    2=1+2
```

という事行っている(mod 256^16しているが、ここでは計算に影響がないので割愛)

つまり、逆の操作を行っていけば

```
0   1     2
------------
a a+b a+b+c    
a a+b     c    2=2-1
a   b     c    1=1-0
```

このように変換前の状態を割り出せる。

## 画像を見てみる

```Python
import cv2
import matplotlib.pyplot as plt

plt.figure(figsize=(20,20))
img1=cv2.imread("body.enc.ppm")
ax1=plt.subplot(2,1,1)
ax1.imshow(img1)
img2=cv2.imread("body.dec.ppm")
ax2=plt.subplot(2,1,2)
ax2.imshow(img2)
plt.show()
cv2.imwrite("result.png",img2)
```
ppmのフォーマットが分かっても図示するのめんどくさいのでopencvに投げて表示

![result1](./decode_result.png)
![result1_only](./decode_result1_only.png)

右下にフラグっぽいのが出てきたけどめっちゃ重なってるので。

ヘッダーを
```
P6
1895 820
255
```
↓
```
P6
3600 410
255
```
に書き換えて再表示.

結果
![result](./decode_result2.png)

よ～～～～～く見ると下の方にflagが見える

## 答え
```
picoCTF{d0Nt_r0ll_yoUr_0wN_aES}
```

## 感想など
いつも解いた後にWriteUpを書いていたが後で考えるのも面倒だなと思い、WriteUpを書きながら解いたところ思考の整理がしやすく、意外にやりやすかった。
最後のFlagが思ったより見づらかったのでどこかで手順を間違えた気がするが、正解は出たのでよし。