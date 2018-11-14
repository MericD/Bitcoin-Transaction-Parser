import numpy as np
import binascii as by
from Diagram import helper_func as hf

__ASCII__= 'ascii'

f = open('a.txt','w')
f1 = open('a1.txt','w')
f2 = open('a2.txt','w')
f3 = open('a3.txt','w')
f4 = open('a4.txt','w')
f5 = open('a5.txt','w')

# analyze content of OP_RETURN fields
def check_hex(arrayList):
  
    # c[0] count content with only 'OP_RETURN '
    # c[1] count error content
    # c[2] count content not hex
    # c[3] count content odd length
    # c[4] count content website
    # c[5] count content  metadata
    # c[6] count content  digit
    # c[7] count content  text
    # c[8] count content  undefinable
    # c[9] count content  ascii hexstring
    # c[10] count content  unknown ascii 
    c = np.zeros(11)   

    # in given array[array] get hexstring, store in j and check content an OP_RETRUN has
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
                # check if content is metadata
                elif hf.is_metadata(bin_dec):
                    c[5] = c[5] + 1
                    f.write("%s\n" % str(bin_dec))
                # check content is digit
                elif  hf.hex_int(bin_dec):
                    c[6] = c[6] +1
                # check content is hexstring
                elif hf.is_hex_op(bin_dec):
                    c[9] = c[9] +1
                    f1.write("%s\n" % str(bin_dec))
                # unknown ascii string 
                elif hf.unknown_ascii(bin_dec):
                    c[10] = c[10] + 1
                    f2.write("%s\n" % str(bin_dec))
                elif ' ' in a:
                    f3.write("%s\n" % str(bin_dec))
                else:
                    f4.write("%s\n" % str(bin_dec))


                # check content is text message
              #  elif  (hf.is_ascii(bin_dec)) and (' ' in bin_dec):
               #     c[7] = c[7] + 1
              #  elif (hf.is_ascii(bin_dec) and hf.no_digit(bin_dec)):
               #     c[7] = c[7] + 1
                #elif hf.is_text(bin_dec):
                 #   # check if content is not definable but is ascii
                  #  c[7]= c[7] +1
            
            
            except:
                a = str(binary)[2:-1]
                # check binary data contains url 
                if hf.check_website(a):
                    c[4] = c[4] + 1 
                # check binary data contains document 
                elif hf.is_metadata(a) or hf.is_metadata_hex(j):
                    c[5] = c[5] + 1
                    f.write("%s\n" % str(a))
                # check content is digit
                elif  hf.hex_int(a):
                    c[6] = c[6] +1
                # check content is hexstring
                elif hf.is_hex_op(a):
                    c[9] = c[9] +1
                    f1.write("%s\n" % str(a))
                elif len(a)>12 and hf.unknown_ascii(a):
                    c[10] = c[10] +1
                    f2.write("%s\n" % str(a))
                # not asci decodable
                elif ' ' in bin_dec:
                    f3.write("%s\n" % str(a))
                else:
                    c[8] = c[8] +1
                    #i.append(len(j)/2)
                    #hf.save_op_sql(i)
                    f5.write("%s\n" % str(a))
                #try:
                #    asc = by.a2b_uu(binary)
                #    f3.write("%s\n" % str(asc))
                #except:
                #    if hf.is_metadata(str(binary)):
                #        c[5] = c[5] + 1
                #    else:
                #        f4.write("%s\n" % str(binary))


              #  elif hf.is_ascii(a) and hf.no_digit(a):
               #     c[7] = c[7] + 1
               
               # elif hf.is_text(a):
                #    c[7] = c[7] + 1
               # else:
                #    c[8] = c[8] +1
                 #   i.append(len(j)/2)
                  #  hf.save_op_sql(i)

    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error',     'Not Hex',    'Odd Lenght', 'Website',   
        'DOCPROOF', 'Number',  'Text',  'Undecodable', 'Ascii hexstring', 'Unknown ascii']

    # concatinate found solutions in a list and return it
    ascii = list(zip(x,c))
    return ascii

