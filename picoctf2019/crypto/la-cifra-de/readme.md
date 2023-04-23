# la cifra de

# 問題
> I found this cipher in an old book. Can you figure out what it says? Connect with nc jupiter.challenges.picoctf.org 32411.

> 私は古い本にこの暗号を見つけました。何が書いてあるかわかりますか?
> nc jupiter.challenges.picoctf.org 32411 に接続してください。

## 解く

接続すると暗号文が出る
```
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x7g996649}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.

Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.
```

括弧や数字が残っているあたり、単純なアルファベットのみの換字式暗号っぽい。
途中にある
```
pohzCZK{m311a50_0x_a1rn3x3_h1ah3x7g996649}
```
がFlagっぽい。
`picoCTF`が`pohzCZK`になるということはシーザー暗号は考えにくい。
一定周期で元の字が出てるあたり、Aが含まれる4文字周期とかのヴィジュネル暗号っぽい。

```
平文 p i c  o C T F
暗号 p o h  z C Z K
差分 0 6 5 11 0 6 5
鍵   A G F  L A G F
```

ということでFLAGを鍵として戻せばいけそう。

## 解読結果

```
It is interesting how in history people often receive credit for things they did not create

During the course of history, the Vigenère Cipher has been reinvented many times

It was falsely attributed to Blaise de Vigenère as it was originally described in 1553 by Giovan Battista Bellaso in his book La cifra del. Sig. Giovan Battista Bellaso

For the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649}

The first well-documented description of a polyalphabetic cipher however, was made around 1467 by Leon Battista Alberti.

The Vigenère Cipher is therefore sometimes called the Alberti Disc or Alberti Cipher.

In 1508, Johannes Trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the Vigenère Cipher.

Bellaso’s second booklet appeared in 1555 as a continuation of the first. The lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.
```

## 答え
```
picoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649}
```
bellaso or vigenere cipher?


## 追加情報

>The Vigenère cipher (French pronunciation: ​[viʒnɛːʁ]) is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.
>First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it resisted all attempts to break it until 1863, three centuries later. This earned it the description le chiffrage indéchiffrable (French for 'the indecipherable cipher'). Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. In 1863, Friedrich Kasiski was the first to publish a general method of deciphering Vigenère ciphers.
>In the 19th century, the scheme was misattributed to Blaise de Vigenère (1523–1596) and so acquired its present name.  
[Wikipedia - Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)


>In 1553, Giovan Battista Bellaso [Note: not “Belaso”, this was a typo, however much it gets repeated on the Internet and in library catalogues] published a cryptography manual called La Cifra del Sig. Giovan Battista Bel[l]aso, dedicated to Girolamo Ruscelli, followed by two other editions in 1555 and 1564. As with Alexander d’Agapeyeff, Simon Singh and countless others, his 1555 book and his 1564 book (Il Vero Modo di Scrivere in Cifra) included some challenge ciphers for readers to cut their teeth on.
[Cipher Mysteries - BELLASO CIPHERS](https://ciphermysteries.com/other-ciphers/bellaso-ciphers)

ヴィジュネルとベラソの関係性がよくわからないものの、ヴィジュネル暗号を開発したのは本来ベラソだったとか(真偽不明)、問題名になっている la cirfa de というワードはベラソの著書によるものらしいとか。

