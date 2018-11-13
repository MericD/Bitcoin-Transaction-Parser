import numpy as np
import binascii as by
from Diagram import helper_func as hf

__ASCII__= 'ascii'

f = open('o.txt','w')
f1 = open('a.txt','w')
# analyze content of OP_RETURN fields
def check_hex(arrayList):
    # parameters for counting different contents
    count_http = 0
    count_txt = 0
    count_ud = 0
    count_dig = 0
    count_doc = 0
    count_op = 0
    count_odd = 0
    count_error = 0
    count_not_hex = 0

    # in given array[array] check what content an OP_RETRUN has
    for i in arrayList:
        j = i[3]     
        # check given item is type of hex
        if not(hf.is_hex(j)):
            # check content is 'OP_RETURN'
            if hf.is_OP(j):
                count_op = count_op + 1
            # check content is '[error]'
            elif '[error]' in str(j):
                count_error = count_error + 1
            else:
                count_not_hex = count_not_hex + 1  
        # hex is odd length add '0' at beginning
        elif len(j) %2 != 0:
            j = '0' + j
            count_odd = count_odd +1
        # hex is even length check content of OP_RETURN hex
        else:
            # convert hexstring to binary data
            binary = by.unhexlify(j) 
            try: 
                #convert binary data to ascii
                bin_dec =binary.decode(__ASCII__)     
                # check content is website/email address
                if hf.check_website(bin_dec):
                    count_http = count_http + 1
                # check if content is document/proof of existent etc. 
                elif hf.is_metadata(bin_dec):
                    count_doc = count_doc + 1
                # check content is digit
                elif  hf.hex_int(bin_dec):
                    count_dig += 1
                # check content is text message
                elif  (hf.is_ascii(bin_dec)) and (' ' in bin_dec):
                    count_txt = count_txt + 1
                elif (hf.is_ascii(bin_dec) and hf.no_digit(bin_dec)):
                    count_txt = count_txt + 1
                elif hf.is_text(bin_dec):
                    # check if content is not definable but is ascii
                    count_txt= count_txt +1
            except:
                a = str(binary)[2:-1]
                try:
                    # check binary data contains url 
                    if hf.check_website(str(binary)):
                        count_http = count_http + 1 
                    # check binary data contains document 
                    elif hf.is_metadata(str(binary)):
                        count_doc = count_doc + 1
                # hex not decodable 
                except:
                    if hf.is_metadata_hex(j):
                        count_doc = count_doc +1
                    # else binary data not definable
                    elif hf.hex_int(a):
                        count_dig = count_dig + 1
                    elif hf.is_hex_op(a) or hf.undef_hexstring(a):
                        count_ud = count_ud +1
                        i.append(len(j)/2)
                        hf.save_op_sql(i)
                    elif hf.is_ascii(a) and hf.no_digit(a):
                        count_txt = count_txt + 1
                    elif hf.is_ascii(a) and not(hf.no_digit(a)):
                        count_txt = count_txt +1
                    elif hf.is_text(a):
                        count_txt = count_txt + 1
                    else:
                        count_ud = count_ud +1
                        i.append(len(j)/2)
                        hf.save_op_sql(i)

    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error',     'Not Hex',    'Odd Lenght', 'Website',   
        'Number',  'Text',    'DOCPROOF', 'Not decodable']

    #  (_,y) part of a tuple --> name of found contents
    y = [count_op, count_error, count_not_hex, count_odd, count_http, 
        count_dig, count_txt, count_doc,  count_ud]

    # concatinate found solutions in a list and return it
    ascii = list(zip(x,y))
    return ascii

