import numpy as np
import binascii as by


def check_hex(arrayList):
    asciilst = ("ascii",hex_ascii(arrayList))
    intlst = ("Integer", hex_int(arrayList))
    hexlst = [[asciilst],[intlst]]
    return hexlst



def hex_int(arrayList):
    counter=0
    for i in arrayList:
        print(len(i))
        #if len(i)%10 == 0:
        counter = counter +1
        print(i)        
    return counter


def hex_ascii(arrayList):
    counter = 0
    ascii = []
    for i in arrayList:
        bin = by.a2b_hex(i)  
        print(bin)
        #ascii_con = by.b2a_uu(bin)
        #print(ascii_con)
        ascii = np.append(ascii, bin)

    print (ascii)
