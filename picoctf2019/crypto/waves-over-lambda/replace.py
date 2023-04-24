s="""\
-------------------------------------------------------------------------------
cxhybgpt jmbm vt rxib awgy - abmqimhcr_vt_c_xomb_wgndkg_xyangihbga
-------------------------------------------------------------------------------
dmpemmh it pjmbm egt, gt v jgom gwbmgkr tgvk txnmejmbm, pjm dxhk xa pjm tmg. dmtvkmt jxwkvhy xib jmgbpt pxympjmb pjbxiyj wxhy zmbvxkt xa tmzgbgpvxh, vp jgk pjm maamcp xa nglvhy it pxwmbghp xa mgcj xpjmb't rgbhtghk momh cxhovcpvxht. pjm wgermbpjm dmtp xa xwk amwwxetjgk, dmcgitm xa jvt nghr rmgbt ghk nghr ovbpimt, pjm xhwr citjvxh xh kmcl, ghk egt wrvhy xh pjm xhwr biy. pjm gccxihpghp jgk dbxiyjp xip gwbmgkr g dxs xa kxnvhxmt, ghk egt pxrvhy gbcjvpmcpibgwwr evpj pjm dxhmt. ngbwxe tgp cbxtt-wmyymk bvyjp gap, wmghvhy gygvhtp pjm nvffmh-ngtp. jm jgk tihlmh cjmmlt, g rmwwxe cxnzwmsvxh, g tpbgvyjp dgcl, gh gtcmpvc gtzmcp, ghk, evpj jvt gbnt kbxzzmk, pjm zgwnt xa jghkt xipegbkt, bmtmndwmk gh vkxw. pjm kvbmcpxb, tgpvtavmk pjm ghcjxb jgk yxxk jxwk, ngkm jvt egr gap ghk tgp kxeh gnxhytp it. em mscjghymk g ame exbkt wgfvwr. gapmbegbkt pjmbm egt tvwmhcm xh dxgbk pjm rgcjp. axb txnm bmgtxh xb xpjmb em kvk hxp dmyvh pjgp ygnm xa kxnvhxmt. em amwp nmkvpgpvom, ghk avp axb hxpjvhy dip zwgcvk tpgbvhy. pjm kgr egt mhkvhy vh g tmbmhvpr xa tpvww ghk msqivtvpm dbvwwvghcm. pjm egpmb tjxhm zgcvavcgwwr; pjm tlr, evpjxip g tzmcl, egt g dmhvyh vnnmhtvpr xa ihtpgvhmk wvyjp; pjm ombr nvtp xh pjm mttms ngbtj egt wvlm g ygifr ghk bgkvghp agdbvc, jihy abxn pjm exxkmk bvtmt vhwghk, ghk kbgzvhy pjm wxe tjxbmt vh kvgzjghxit axwkt. xhwr pjm ywxxn px pjm emtp, dbxxkvhy xomb pjm izzmb bmgcjmt, dmcgnm nxbm txndbm mombr nvhipm, gt va ghymbmk dr pjm gzzbxgcj xa pjm tih."""

alp={"p":"t",
    "j":"h",
    "m":"e",
    "b":"r",
    "o":"v",
    "r":"y",
    "x":"o",
    "y":"g",
    "i":"u",
    "z":"p",
    "g":"a",
    "c":"c",
    "v":"i",
    "h":"n",
    "t":"s",
    "a":"f",
    "w":"l",
    "q":"q",
    "k":"d",
    "d":"b",
    "e":"w",
    "n":"m",
    "s":"t",
    "l":"k",
    "u":"x",
    "f":"z",
}

ans=["*"]*len(s)

for i,c in enumerate(s):
    for cc in [",",".","'",";","-","!","?"," ","\n","_"]:
        if c==cc:
            ans[i]=cc
            break


for i in alp:
    for j in range(len(s)):
        if s[j]==i:
            ans[j]=alp[i]
print(s)
print("".join(ans))
