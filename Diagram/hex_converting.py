import numpy as np
import binascii as by
from Diagram import helper_func as hf
from Diagram import hex_config as hc
from Diagram import frequenzy_table as ft
import array



f = open('unknown_magic.txt', 'w')

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


    docproof = 0
    factom=0
    omni=0
    ascribe =0
    oa=0
    ida = 0
    s = 0
    ew=0
    kc=0
    copy=0
    cc=0
    other = 0
    bs =0

    xxxxxxx = 0
    spk=0
    samp =('S1', 'S2', 'S3', 'S4', 'S5')
    faco =('FACTOM00' ,'Factom!!', 'Fa','FA')
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
                # check if content is metadata
                if hf.is_metadata(bin_dec):
                    c[5] = c[5] + 1
                    #i.append(len(j)/2)
                    #hf.save_op_sql(i)
                    if bin_dec.startswith('DOCPROOF'):
                        docproof = docproof +1
                    elif any( i in bin_dec for i in faco):                        
                        factom = factom +1
                    elif bin_dec.startswith('omni'):
                        omni = omni +1
                    elif bin_dec.startswith('ASCRIBE'):
                        ascribe = ascribe + 1
                    elif bin_dec.startswith('OA'):
                        oa=oa+1
                    elif bin_dec.startswith('id'):
                        ida=ida+1
                    elif any( i in bin_dec for i in samp):
                        s = s+1
                    elif bin_dec.startswith('EW'):
                        ew=ew+1
                    elif bin_dec.startswith('KC'):
                        kc=kc+1
                    elif bin_dec.startswith('SPK'):
                        spk=spk+1
                    elif bin_dec.startswith('@COPYROBO'):
                        copy=copy+1
                    elif bin_dec.startswith('SPK'):
                        copy=copy+1
                    elif bin_dec.startswith('CC'):
                        cc=cc+1
                    elif bin_dec.startswith('BS'):
                        bs=bs+1
                    else:
                        other = other +1
                    #i.append(len(j)/2)
                    #hf.save_op_sql(i)
                # check content is website/email address
                elif hf.check_website(bin_dec):
                    c[4] = c[4] + 1
                elif  hf.hex_int(bin_dec):
                    c[6] = c[6] +1
                # check content is hexstring
                elif hf.is_hex_op(bin_dec):
                    c[9] = c[9] +1
                    xxxxxxx = xxxxxxx + (len(j)/2)
                elif str(bin_dec).startswith('"') and str(bin_dec).endswith('"'):
                    b = str(bin_dec)[1:-1]
                    if hf.is_hex_op(b):
                        c[9] = c[9] +1
                        xxxxxxx = xxxxxxx + (len(j)/2)
                elif any(i in bin_dec for i in hc.data):
                    c[11] = c[11] +1
                # unknown ascii string 
                elif len(bin_dec) == 1 and ' ' in bin_dec:
                    c[0] = c[0] + 1
                elif any(i in bin_dec for i in hc.text_check):
                    c[7] = c[7] + 1
                elif hf.unknown_ascii(bin_dec):
                    c[10] = c[10] + 1 
                    unknown_content.append(bin_dec)
                    f.write("%s\n" % str(bin_dec))    
                    f.write("%s\n" % str(j))        
                elif  (' ' in bin_dec) or (len(bin_dec)==1):
                    c[7] = c[7] + 1
                else:
                    c[10] = c[10] + 1
                    unknown_content.append(bin_dec)
                    f.write("%s\n" % str(bin_dec))    
                    f.write("%s\n" % str(j))   
            except:
                a = str(binary)[2:-1]
                # check binary data contains document 
                if hf.is_metadata(a):
                    c[5] = c[5] + 1
                    #i.append(len(j)/2)
                    #hf.save_op_sql(i)
                    if a.startswith('DOCPROOF'):
                        docproof = docproof +1
                    elif any( i in a for i in faco):
                        factom = factom +1
                    elif a.startswith('omni'):
                        omni = omni +1
                    elif a.startswith('ASCRIBE'):
                        ascribe = ascribe + 1
                    elif a.startswith('OA'):
                        oa=oa+1
                    elif a.startswith('id'):
                        ida=ida+1
                    elif any( i in a for i in samp):
                        s = s+1
                    elif a.startswith('EW'):
                        ew=ew+1
                    elif a.startswith('KC'):
                        kc=kc+1
                    elif a.startswith('@COPYROBO'):
                        copy=copy+1
                    elif a.startswith('SPK'):
                        copy=copy+1
                    elif a.startswith('CC'):
                        cc=cc+1
                    elif a.startswith('BS'):
                        bs=bs+1
                    elif a.startswith('BS'):
                        spk=spk+1
                    else:
                        other = other +1
                    #i.append(len(j)/2)
                    #hf.save_op_sql(i)
                # check binary data contains url 
                elif hf.check_website(a):
                    c[4] = c[4] + 1 
                # check content is digit
                elif  hf.hex_int(a):
                    c[6] = c[6] +1
                # check content is hexstring
                elif hf.is_hex_op(a):
                    c[9] = c[9] +1
                    xxxxxxx = xxxxxxx + (len(j)/2)
                elif str(a).startswith('"') and str(a).endswith('"'):
                    b = str(a)[1:-1]
                    if hf.is_hex_op(b):
                        c[9] = c[9] +1
                        xxxxxxx = xxxxxxx + (len(j)/2)
                elif any(i in a for i in hc.text_check):
                    c[7] = c[7] + 1
                elif hf.unknown_ascii(a) and ('\\' not in a):
                    unknown_content.append(bin_dec)
                    f.write("%s\n" % str(a))    
                    f.write("%s\n" % str(j))    
                    c[10] = c[10] + 1         
                        
                elif any( str(j).startswith(i) for i in hc.prefix_meta):
                    c[5] = c[5] + 1
                    other = other +1
                    #i.append(len(j)/2)
                    #hf.save_op_sql(i)
                else:
                    try:
                        c[8] = c[8] + 1   
                    except:
                        pass
    
    
    arr = []
    arr.append(docproof)
    arr.append(factom)
    arr.append(omni)
    arr.append(ascribe)
    arr.append(oa)
    arr.append(ida)
    arr.append(s)
    arr.append(ew)
    arr.append(kc)
    arr.append(copy)
    arr.append(spk)
    arr.append(other)
    arr.append(bs)

    #cc = np.sum(arr)

    #sss = ft.freq_tab(unknown_content)
    #print(sss)
    #print(sss[0])


    #print(xxxxxxx)
    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error', 'Not Hex', 'Odd Lenght', 'Website',   
        'Metadata', 'Digit', 'Text', 'Undefinable', 'Ascii hexstring', 'Unknown ascii', 'File']
    print(c)
    # concatinate found solutions in a list and return it
    ascii = list(zip(x,c))
    return ascii





