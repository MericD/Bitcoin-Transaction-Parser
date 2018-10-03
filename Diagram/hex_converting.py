import numpy as np
import enchant as ec
import binascii as by
import matplotlib.pyplot as pyplot
from enchant.checker import SpellChecker




def check_hex(arrayList):
    return hex_ascii(arrayList)


def hex_ascii(arrayList):
    count_http = 0
    count_txt = 0
    count_ud = 0
    count_dig = 0


    for i in arrayList:
        #print("sratr for: " +str(i))
        try:
            binary = by.unhexlify(i)
            #print("CHECKER:" + str(binary))
            if (len(binary)%2 == 0) or (len(binary)%2 != 0):
                bin_dec =binary.decode('unicode-escape')

                if check_website(bin_dec):
                    count_http = count_http + 1
                elif hex_int(bin_dec):
                    count_dig += 1
                else:
                    try:
                        #print("---------------" + str(check_text(bin_dec)))
                        bin_dec.encode('ascii')
                        count_txt = count_txt + 1
                        #print("------------ TEXT -----------" + str(bin_dec))

                    except:
                        count_ud= count_ud + 1
                        #print("NOT -----------" + str(bin_dec))
                        
                    else:
                        if ( 2 <= len(bin_dec.split(" "))) or (bin_dec.encode('ascii')):
                            count_txt = count_txt + 1
        except:
            count_ud= count_ud + 1
            print("attentionnnnnnnnnnn----NOOOOOTTTT        " + str(bin_dec))


    x = ['Website', 'Digit', 'Text', 'Undefined']
    y = [count_http, count_dig, count_txt, count_ud]
    ascii = list(zip(x,y))
    #print (ascii)
    #print (ec.list_languages())
    return ascii



def isAscii(s):
    return all(ord(c) < 128 for c in s)


def check_website(bin_dec):
    sub = ('https:', 'http:', 'www.', '.com')
    if any(i in bin_dec for i in sub):
        return True
    else:
        return False



def hex_int(digit):
    sub = ('1','2','3','4','5','6','7','8','9','0') 
    count = 0 
    for i in sub:
        if i in digit:
            count += 1    
    if 0 < count and (digit.encode('ascii')):
        return True
    else:
        return False 
         
        
    


def check_text (hex_str):
    chkr = SpellChecker("en_UK","en_US", "en_AU", "fr_FR","de_DE")
    chkr.set_text(hex_str)
    is_word = 0
    for err in chkr:
        sug = err.suggest()[0]
        err.replace(sug)
        is_word = is_word + 1
    #Spellchecked = chkr.get_text()
    #print(Spellchecked)