from typing import Mapping
from pwn import *

s = remote('46.101.8.93',32583)

symbols = [b'*',b'/',b'+',b'-']

def calc(num1, num2, symbols):
    # print(num1, symbols, num2)
    if(symbols == b'+'):
        return (num1 + num2)
    elif(symbols == b'-'):
        return (num1-num2)
    elif(symbols == b'*'):
        return (num1*num2)
    elif(symbols == b'/'):
        return (num1/num2)
    else:
        log.warning("something wrong at symbols !")
        return 0
def clear_multi_divide(element_of_ques):
    i = 0
    while (i <= len(element_of_ques)-1):
        if(element_of_ques[i]==b'='):
            break
        elif(element_of_ques[i] == b'*'):
            num1 = int(element_of_ques[i-1])
            num2 = int(element_of_ques[i+1])
            element_of_ques[i-1] = num1*num2
            del element_of_ques[i]
            del element_of_ques[i]
            i-=1
        elif(element_of_ques[i] == b'/'):
            num1 = int(element_of_ques[i-1])
            num2 = int(element_of_ques[i+1]) 
            element_of_ques[i-1] = num1/num2
            del element_of_ques[i]
            del element_of_ques[i]
            i-=1
        # print(element_of_ques)
        i+=1
    log.info("kiem chung sau rut gon: %s"%element_of_ques )
    return element_of_ques
def do_exercise(element_of_ques):
    element_of_ques = clear_multi_divide(element_of_ques) # xu ly tat ca cac phep tinh uu tien
    calc_result = -2341
    remember_symbols = ''
    for i in element_of_ques:
        if i!=b'=' and i != b'':
            if i in symbols:
                if remember_symbols == '':
                    remember_symbols = i
                else:
                    log.warning("2 symbols contigous !")
            else:
                i = int(i)
                #not in symbols
                if(calc_result == -2341): #mean not set first number
                    calc_result = i 
                else: #not first number
                    if(remember_symbols == ''): #  mean 2 number contigous?
                        log.warning("2 number contigous !")
                    else: # yes, normal flow code
                        calc_result = calc(calc_result,i,remember_symbols)
                        remember_symbols = ''
        else:
            break
    return calc_result

isContinue = 1
while(isContinue):
    s.recvuntil("Question")
    ques_num  = s.recvline()
    if(b'777' in ques_num):
        pause()

    s.recv(1)
    ques = s.recvline()
    log.info("%s: %s"%(ques_num,ques))
    element_of_ques  = ques.split(b' ')
    # print(element_of_ques)
    rs = int(do_exercise(element_of_ques))
    log.info("Answer: %d"%rs)
    s.sendlineafter("Answer:",str(rs))
    s.recvline()
    s.recvline()
    if b'Pass' not in s.recvline():
        isContinue = 0

s.interactive()
s.close()