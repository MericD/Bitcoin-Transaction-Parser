import numpy as np
import binascii as by
from Diagram import helper_func as hf

__ASCII__= 'ascii'

f = open('o.txt','w')
f1 = open('a.txt','w')
# analyze content of OP_RETURN fields
def check_hex(arrayList):
    # parameters for counting different contents
  
    # c[0] count content with only 'OP_RETURN '
    # c[1] count error content
    # c[2] count content not hex
    # c[3] count content odd length
    # c[4] count content website
    # c[5] count content  metadata
    # c[6] count content  digit
    # c[7] count content  text
    # c[8] count content  undefinable

    c = np.zeros(9)   



    # in given array[array] check what content an OP_RETRUN has
    for i in arrayList:
        j = i[3]     
        # check given item is type of hex
        if not(hf.is_hex(j)):
            # check content is 'OP_RETURN'
            if hf.is_OP(j):
                c[0] = c[0] + 1
            # check content is '[error]'
            elif '[error]' in str(j):
                c[1] = c[1] + 1
            else:
                c[2] = c[2] + 1  

        
        # hex is odd length add '0' at beginning
        elif len(j) %2 != 0:
            j = '0' + j
            c[3] = c[3] +1
        # hex is even length check content of OP_RETURN hex
        
        
        
        else:
            # convert hexstring to binary data
            binary = by.unhexlify(j) 
            try: 
                #convert binary data to ascii
                bin_dec =binary.decode(__ASCII__)     
                # check content is website/email address
                if hf.check_website(bin_dec):
                    c[4] = c[4] + 1
                # check if content is document/proof of existent etc. 
                elif hf.is_metadata(bin_dec):
                    c[5] = c[5] + 1
                # check content is digit
                elif  hf.hex_int(bin_dec):
                    c[6] = c[6] +1
                # check content is text message
                elif  (hf.is_ascii(bin_dec)) and (' ' in bin_dec):
                    c[7] = c[7] + 1
                elif (hf.is_ascii(bin_dec) and hf.no_digit(bin_dec)):
                    c[7] = c[7] + 1
                elif hf.is_text(bin_dec):
                    # check if content is not definable but is ascii
                    c[7]= c[7] +1
            
            
            except:
                a = str(binary)[2:-1]
                try:
                    # check binary data contains url 
                    if hf.check_website(str(binary)):
                        c[4] = c[4] + 1 
                    # check binary data contains document 
                    elif hf.is_metadata(str(binary)):
                        c[5] = c[5] + 1
                # hex not decodable 
                except:
                    if hf.is_metadata_hex(j):
                        c[5] = c[5] +1
                    # else binary data not definable
                    elif hf.hex_int(a):
                        c[6] = c[6] + 1
                    elif hf.is_hex_op(a) or hf.undef_hexstring(a):
                        c[8] = c[8] +1
                        i.append(len(j)/2)
                        hf.save_op_sql(i)
                    elif hf.is_ascii(a) and hf.no_digit(a):
                        c[7] = c[7] + 1
                    elif hf.is_ascii(a) and not(hf.no_digit(a)):
                        c[7] = c[7] +1
                    elif hf.is_text(a):
                        c[7] = c[7] + 1
                    else:
                        c[8] = c[8] +1
                        i.append(len(j)/2)
                        hf.save_op_sql(i)

    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error',     'Not Hex',    'Odd Lenght', 'Website',   
        'Number',  'Text',    'DOCPROOF', 'Not decodable']

    # concatinate found solutions in a list and return it
    ascii = list(zip(x,c))
    return ascii

