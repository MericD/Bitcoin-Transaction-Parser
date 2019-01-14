import numpy as np
import binascii as by
from Diagram import helper_func as hf
from Diagram import hex_config as hc
from Diagram import frequenzy_table as ft
import array
import magic 



f = open('unknown_magic.txt', 'w')
f1 = open('undef_magic.txt', 'w')
f2 = open('undef.txt', 'w')


__ASCII__= 'ascii'
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
    # c[11] count content  data 
    c = np.array(12)   
    c.astype(int)
    c= array.array('i',(0 for _ in range(12)))
    unknown_content =[]
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
                print(i[1])
                f.write("%s\n" % str(j))
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
                elif hf.is_metadata(bin_dec) or hf.is_metadata(str(j)):
                    c[5] = c[5] + 1
                    i.append(len(j)/2)
                    hf.save_op_sql(i)
                elif  hf.hex_int(bin_dec):
                    c[6] = c[6] +1
                # check content is hexstring
                elif hf.is_hex_op(bin_dec):
                    c[9] = c[9] +1
                    print(i[1])
                elif str(bin_dec).startswith('"') and str(bin_dec).endswith('"'):
                    b = str(bin_dec)[1:-1]
                    if hf.is_hex_op(b):
                        c[9] = c[9] +1
                elif any(i in bin_dec for i in hc.data):
                    c[11] = c[11] +1
                # unknown ascii string 
                elif len(bin_dec) == 1 and ' ' in bin_dec:
                    c[0] = c[0] + 1
                elif any(i in bin_dec for i in hc.text_check):
                    c[7] = c[7] + 1
                elif hf.unknown_ascii(bin_dec):
                    c[10] = c[10] + 1                 
                elif  (' ' in bin_dec) or (len(bin_dec)==1):
                        #i.append(len(j)/2)
                        #hf.save_op_sql(i)
                    c[7] = c[7] + 1
                else:
                    c[10] = c[10] + 1
            except:
                a = str(binary)[2:-1]
                # check binary data contains url 
                if hf.check_website(a):
                    c[4] = c[4] + 1 
                # check binary data contains document 
                elif hf.is_metadata(a) or hf.is_metadata(str(j)):
                    c[5] = c[5] + 1
                    i.append(len(j)/2)
                    hf.save_op_sql(i)
                # check content is digit
                elif  hf.hex_int(a):
                    c[6] = c[6] +1
                # check content is hexstring
                elif hf.is_hex_op(a):
                    c[9] = c[9] +1
                elif str(a).startswith('"') and str(a).endswith('"'):
                    b = str(a)[1:-1]
                    if hf.is_hex_op(b):
                        c[9] = c[9] +1
                elif any(i in a for i in hc.text_check):
                    c[7] = c[7] + 1
                    #    i.append(len(j)/2)
                    #    hf.save_op_sql(i)
                elif hf.unknown_ascii(a) and ('\\' not in a):
                    c[10] = c[10] + 1                 
                else:
                    c[8] = c[8] + 1
                
    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error', 'Not Hex', 'Odd Lenght', 'Website',   
        'Metadata', 'Digit', 'Text', 'Undefinable', 'Ascii hexstring', 'Unknown ascii', 'File']
    print(c)
    # concatinate found solutions in a list and return it
    ascii = list(zip(x,c))
    return ascii


def cat_metadata(bin_dec):
    docproof =0
    factom=0
    omni=0
    ascribe =0
    oa=0
    ida = 0
    s = 0
    ew=0
    kc=0
    copy=0
    if bin_dec.startswith('DOCPROOF'):
        docproof = docproof +1
    elif bin_dec.startswith('FACTOM00') or bin_dec.startswith('Factom!!') or bin_dec.startswith('Fa') or bin_dec.startswith('FA'):
        factom = factom +1
    elif bin_dec.startswith('omni'):
        omni = omni +1
    elif bin_dec.startswith('ASCRIBE'):
        ascribe = ascribe + 1
    elif bin_dec.startswith('OA'):
        oa=oa+1
    elif bin_dec.startswith('id'):
        ida=ida+1
    elif bin_dec.startswith('S1') or bin_dec.startswith('S2') or bin_dec.startswith('S3') or bin_dec.startswith('S4')or bin_dec.startswith('S5'):
        s = s+1
    elif bin_dec.startswith('EW'):
        ew=ew+1
    elif bin_dec.startswith('KC'):
        kc=kc+1
    elif bin_dec.startswith('CC'):
        kc=kc+1
    elif bin_dec.startswith('@COPYROBO'):
        copy=copy+1
    elif bin_dec.startswith('SPK'):
        copy=copy+1


#    metadata = ('TTB-T','SKYE','KEYSTAMP','LICTIP10','** PROOF.COM **', 'CryptoTests-', 'CryptoProof-', 'STAMPD##', 'BITPROOF', 
#            'ProveBit', 'RMBe', 'RMBd', 'ORIGMY', 'LaPreuve', 'UNicDC','POET', 'EXONUM', 'BARD','', , 
#          'CNTRPRTY','SLDX:', 'SPK',  'BS', '' ,'', '', 'MG', 'SB.D', 
#          'SW', 'DS' , 'OC', 'Mined by 1hash.com', 'FluxST', 'XY','XW', 'SS', 'KMD', 'OKT', 'CP110400', 'XX') 



    