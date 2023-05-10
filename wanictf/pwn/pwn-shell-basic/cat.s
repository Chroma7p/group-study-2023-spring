mov    ecx,esp
push   eax  ; null
push   ecx  ; file
push   ebx  ; /bin/cat
mov    ecx,esp ; {/bin/cat,file,null}
xor eax,eax
add eax,0xb
int 0x80