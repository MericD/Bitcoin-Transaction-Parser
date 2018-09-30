import numpy as np
import binascii as by
import matplotlib.pyplot as pyplot



def check_hex(arrayList):
    hex_ascii(arrayList)
    #hex_int(arrayList)
    #hex_large_size(arrayList)




def hex_ascii(arrayList):
    print(arrayList)
    count_http = 0
    count_txt = 0
    count_ud = 0
    ascii = []

    for i in arrayList:
        print(len(i))
        print("sratr for: " +str(i))
        bin1 = by.unhexlify(i)
        bin =bin1.decode('unicode-escape')

        print("--------------> :" +bin)

        if "https:" in bin:
            count_http = count_http + 1
            print("HTTPS:"+ str(count_http))
            
        elif "http:" in bin:
            count_http = count_http + 1
            print("HTTP:"+ str(count_http))

        else:
            try:
                bin.encode('ascii')
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
    print (ascii)



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


def hex_large_size(arrayList):
    counter = 0
    for i in arrayList:
        if 40 <= len(by.unhexlify(i)):
            counter = counter +1
            print( "Big size")
        else:
            print('small' + str(len(by.unhexlify(i))))
            pass    
    return counter 
       