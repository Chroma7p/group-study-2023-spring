Why use p and q when I can use more? 

```

c: 11750963787398275598017156558691178453198396338704291985844171408080571428290553579308600211759961703487997477014314104425284513795123780207248536613317553552025532799334873346480625684637866342578520823529687350827961594573545893749921028675514232887454174636358542063204498250702097629240304775843404749268109914242092301610352335446151947304
n: 33360952998480141889211503674092249326411697168314459884109916296006473558253610953624900747601417492577638670724328387938334724940232695876046922382157561381901121851416503082399555411869464030506687752468837222628706902065727510391456430405021128843675333941824998049347960083969316885219120691891282905414440465093257563505575841591832240933
e: 65537
```

問題文からしてnにp,q意外の素数をたくさん用いているようです。まあおそらくここが突破口で、計算可能なくらい因数が小さくなっていそうなので、素因数分解してみる。
すると普通にできたのであとはdを計算する。totient関数の計算だけ二つの場合と比べ厄介ではあるが全部素数なので大丈夫。

```
picoCTF{too_many_fact0rs_4025135}
```