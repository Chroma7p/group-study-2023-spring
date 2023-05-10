from pwn import *

pc = process("./chall")
# pc = remote("",)
with open("cat","rb") as f:
    shell_code = f.read()  # PUT YOUR SHELL CODE HERE
pc.sendline(shell_code)
pc.interactive()
