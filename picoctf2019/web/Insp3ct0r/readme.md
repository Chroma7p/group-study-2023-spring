# Insp3ct0r

## 問題
> Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ (link) or http://jupiter.challenges.picoctf.org:41511

> Kishor Balanから、以下のコードの検査が必要かもしれないとの情報がありました

## 見てみる
とりあえずデベロッパーツールでページのソースコードを見てみると、インデックスのほかに`myjs.js`、`mycss.css`があることがわかる。
HTMLを見ると
```
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

jsを見ると
```
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */
```

cssを見ると
```
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

順番通りに直すと
```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}
```