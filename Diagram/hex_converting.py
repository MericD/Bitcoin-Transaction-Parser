import numpy as np
import binascii as by
import string
from SQL import sqlite as sql
import sqlite3
from rpc import rpc
from Core import core as c

__ASCII__= 'ascii'

rpc_connection = rpc.start_connection_to_rpc()

f=open('o.txt','w')
f1=open('a.txt','w')
f2 = open('b.txt','w')


# save undefinable OP_RETURN fields in an additional table for more analysis
# databse table contains only the transaction id, block number and 
# transaction value of the corresponding op_return field 
def save_op_sql(numarray):
    connection = sqlite3.connect('blockchain.db')
    sql.initTabel(connection)
  
    raw_tx = rpc.decoded_transactions_address(rpc_connection, numarray[1])
    arr=[]
    b = 0.0
    a = []
    arr = numarray[2].split(", ")
    print(arr)


    for i in range(len(arr)):
        if 'E' in arr[i]:
            b = arr[i][0]
            b = float(b)
        else:
            b = float(arr[i])
        a.append(b)


        
    block_number = numarray[0] 
    transaction_id  =  numarray[1]
    tx_value = a
    op_return = 'OP_RETURN ' + numarray[3]
    op_length = numarray[4]
    address_info = c.get_address_of_op_tx(raw_tx)
    tx_address = address_info[0]
    address_number = address_info[1]

    sql.addOP(connection, transaction_id, block_number, tx_value, op_return, op_length, tx_address, address_number)
    connection.close()



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
        if not(is_hex(j)):
            # check content is 'OP_RETURN'
            if is_OP(j):
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
                if check_website(bin_dec):
                    count_http = count_http + 1
                # check if content is document/proof of existent etc. 
                elif is_metadata(bin_dec):
                    count_doc = count_doc + 1
                # check content is digit
                elif  hex_int(bin_dec):
                    count_dig += 1
                # check content is text message
                elif  (is_ascii(bin_dec)) and ((' ' in bin_dec)):
                    count_txt = count_txt + 1
                elif (is_ascii(bin_dec) and no_digit(bin_dec)):
                    count_txt = count_txt + 1
                elif is_ascii(bin_dec):
                    # check if content is not definable but is ascii
                    if is_text(bin_dec):
                        count_txt= count_txt +1
            except:
                try:
                    # check binary data contains url 
                    if check_website(str(binary)):
                        count_http = count_http + 1 
                    # check binary data contains document 
                    elif is_metadata(str(binary)):
                        count_doc = count_doc + 1
                    # else binary data not definable
                    elif  hex_int(str(binary)):
                        count_dig += 1
                    elif is_ascii(str(binary)) and is_text(str(binary.decode(__ASCII__))):
                        count_txt = count_txt + 1
                # hex not decodable 
                except:
                    if is_metadata_hex(j):
                        count_doc = count_doc +1
                    else:
                        #f.write("%s\n" % str(binary))
                        count_ud = count_ud +1
                        i.append(len(j)/2)
                        save_op_sql(i)


    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error',     'Not Hex',    'Odd Lenght', 'Website',   
        'Number',  'Text',    'DOCPROOF', 'Not decodable']

    #  (_,y) part of a tuple --> name of found contents
    y = [count_op, count_error, count_not_hex, count_odd,    count_http, 
        count_dig, count_txt, count_doc,  count_ud]

    f.write("%s\n" % str(y))

    # concatinate found solutions in a list and return it
    ascii = list(zip(x,y))
    return ascii



# check if given object contains only hex
def is_hex(op):
    if all(c in string.hexdigits for c in str(op)):
        return True
    else:
        return False

# check if hex is a OP_RETURN
def is_OP(op):
    if 'OP_RETURN' in str(op):
        return True
    else:
        return False





# check if hex is a website/Email
def check_website(bin_dec):
    sub = ('https', 'http', 'www.', '.com', '.org')
    if any(i in str(bin_dec) for i in sub):
        return True
    else:
        return False




# check if hex is a document
def is_metadata(bin_dec):
    sub = ('** PROOF.COM **','DOCPROOF','FACTOM00' ,'Factom!!', 'Fa', 'CryptoTests-', 'CryptoProof-', 'STAMPD##', 'BITPROOF', 
            'ProveBit', 'RMBe', 'RMBd', 'ORIGMY', 'LaPreuve', 'UNicDC','POET', 'EXONUM', 'BARD','omni', 'ASCRIBE', 
          'CNTRPRTY','SLDX:', 'CC', 'SPK', 'S1', 'S2', 'S3', 'S4', 'S5', 'BS', 'FA' ,'OA', 'id', 'MG', 'EW', 'SB.D', 
          'SW', 'DS' , 'OC', 'Mined by 1hash.com', 'FluxST', 'XY','XW', 'SS', 'KMD', 'OKT', 'CP110400', 'XX','TBT-T') 
    
    if any(str(bin_dec).startswith(i) for i in sub):
        return True
    elif any(i in str(bin_dec) for i in sub):
        return True
    elif any(bin_dec.startwith("b'"+i) for i in sub):
        return True
    elif any(bin_dec.startwith("b"+str('"')+i) for i in sub):
        return True
    else:
        return False






# check if hex is a integer
def hex_int(digit):
    sub = ('1','2','3','4','5','6','7','8','9','0') 
    count = 0 
    for i in sub:
        if i in digit:
            count += 1 
        else:
            break 
    if count == len(digit):
        return True
    else:
        return False 
         


# check if hex is ascii and contains only letters or words --> TEXT
def no_digit(bin_dec):
    sub = ('1','2','3','4','5','6','7','8','9','0') 
    if any(i in bin_dec for i in sub):
        return False
    else:
        return True



# check if hex is ascii --> TEXT
def is_ascii(bin_dec):
    if(all(ord(char) < 128 for char in bin_dec)):
        return True
    else:
        return False



# personal dictionary to find some words in OP_Retrun and clasify it as text
def is_text(bin_dec):
    sub = ('bitc0in','est','usd','USD','uds','script','bitcamp','_SUCKS','NVBT','Satoshi','d-r1',
        's-r1', '!','"','#', '$', '%', '&','*','-','==','&','(',')','.', 'undefined', 'lol', 'tt2', 
        'PropertyProtected', 'data', '_', 'link', '?', '|', 'KC{','tt3', 'Bitcoin over capacity',
        'Bitcoin: A Peer-to-Peer Electronic Cash System')
    if any(i in bin_dec for i in sub):
        return True
    elif (len(bin_dec) ==1) and (' ' in bin_dec):
        return True
    else:
        return False


#check is metadata starter
def is_metadata_hex(hex_str):
    hex_start = ('455720', '4f410100', '444f4350524f4f46','53422e44', '554e6963444320', '4352454400010004','6964', 
               'aa21a9','1f00', '5808', '5808' , '53504b', '4f43')

    if any(str(hex_str).startswith(i) for i in hex_start):
        return True
    else:
        return False


