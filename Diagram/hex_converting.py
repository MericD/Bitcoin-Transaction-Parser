import numpy as np
import binascii as by
import matplotlib.pyplot as pyplot



def check_hex(arrayList):
    return hex_ascii(arrayList)


def hex_ascii(arrayList):
    count_http = 0
    count_txt = 0
    count_ud = 0

    for i in arrayList:
        print("sratr for: " +str(i))
        binary = by.unhexlify(i)
        bin_dec =binary.decode('unicode-escape')

        print("--------------> :" + bin_dec)

        if "https:" in bin_dec:
            count_http = count_http + 1
            print("HTTPS:"+ str(count_http))
            
        elif "http:" in bin_dec:
            count_http = count_http + 1
            print("HTTP:"+ str(count_http))
        else:
            try:
                bin_dec.encode('ascii')
                print(" ascii")
                count_txt = count_txt + 1
                print(count_txt)

            except UnicodeEncodeError:
                count_ud= count_ud + 1
                print("not ascii")
                print(count_ud)
            else:
                count_txt = count_txt + 1
                print("add 2. : " + str(count_txt))
    
    x = ['Website', 'Text/ Number', 'Undefined']
    y = [count_http, count_txt, count_ud]
    ascii = list(zip(x,y))
    print (ascii)
    return ascii



def isAscii(s):
    return all(ord(c) < 128 for c in s)



def hex_int(i):
    int_counter=0
    if int(i, 16):
        int_counter = int_counter + 1
        print("-------------INTEGER" + str(int(i, 16)))
    else:   
        print("---------------NOT INT------------")     
    return int_counter
