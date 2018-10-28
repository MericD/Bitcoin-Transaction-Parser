import numpy as np
import binascii as by
import string
from SQL import sqlite as sql
import sqlite3
from rpc import rpc
from Core import core as c

__ASCII__= 'ascii'


#rpc_connection = rpc.start_connection_to_rpc()




# save undefinable OP_RETURN fields in an additional table for more analysis
# databse table contains only the transaction id, block number and 
# transaction value of the corresponding op_return field 
#def save_op_sql(numarray):
x = {'39e4439fab8b65a319584d51f69439264d235964467ef5305149805f045e4dc6': {'hash': '39e4439fab8b65a319584d51f69439264d235964467ef5305149805f045e4dc6', 'size': 275, 'vsize': 275, 'locktime': 0, 'version': 1, 'vin': [{'sequence': 4294967295, 'vout': 0, 'txid': '0c9df6a2c82cca4ea85ac80e7e8efafa9b2adcbbec879ea4ac62e8a40afc771f', 'scriptSig': {'hex': '483045022100b74a195d84c5a9550dfcfd0cd1409ab56139de46535099049a4704b62da1392502200ae5dfbd9f75d8629b07f225cd52d7ad435876bd9b489178edbf4d7dc76db6e6012103d6445fd89e2a7b64de3210cbe07938e3388fd19c6d5f469abaa02b78436195fb', 'asm': '3045022100b74a195d84c5a9550dfcfd0cd1409ab56139de46535099049a4704b62da1392502200ae5dfbd9f75d8629b07f225cd52d7ad435876bd9b489178edbf4d7dc76db6e6[ALL] 03d6445fd89e2a7b64de3210cbe07938e3388fd19c6d5f469abaa02b78436195fb'}}], 'txid': '39e4439fab8b65a319584d51f69439264d235964467ef5305149805f045e4dc6', 'vout': [{'value': '0E-8', 'scriptPubKey': {'type': 'nulldata', 'hex': '6a26069a9ec2600321764f132fcae2e7df2069a32538c5ae489f3e5f0dd2c3e057c1efe608be74de', 'asm': 'OP_RETURN 069a9ec2600321764f132fcae2e7df2069a32538c5ae489f3e5f0dd2c3e057c1efe608be74de'}, 'n': 0}, {'value':'0.00080000', 'scriptPubKey': {'type': 'pubkeyhash', 'hex': '76a914a7552d89b0e655b8c6199899669792cb54d954c588ac', 'addresses': ['1GFmtJKoYtGkXJWSXUZgxnyjqd6itJGxvn'], 'asm': 'OP_DUP OP_HASH160 a7552d89b0e655b8c6199899669792cb54d954c5 OP_EQUALVERIFY OP_CHECKSIG', 'reqSigs': 1}, 'n': 1}, {'value': '0.00010000', 'scriptPubKey': {'type': 'pubkeyhash', 'hex': '76a914f96b59fb1c136df27642f746813a32e9d80e54a288ac', 'addresses': ['1PjorgKWXFFBaLDiW5EXJPViVPo3fu1zYB'], 'asm': 'OP_DUP OP_HASH160 f96b59fb1c136df27642f746813a32e9d80e54a2 OP_EQUALVERIFY OP_CHECKSIG', 'reqSigs': 1}, 'n': 2}]}}

    #raw_tx = rpc.decoded_transactions_address(rpc_connection, numarray[1])

connection = sqlite3.connect('blochckain.db')
sql.initTabel(connection)
block_number = 1 #numarray[0] 
transaction_id  =  'a' #numarray[1]
tx_value = '1a'#numarray[2]
op_return = 'b'#'OP_RETURN ' + numarray[3]
op_length = 2#numarray[4]
tx_address = c.get_address_of_op_tx(x)

sql.addOP(connection,block_number, transaction_id, tx_value, op_return, op_length, tx_address)
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
    count_asset = 0
    count_ascii = 0

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
                elif docproof(bin_dec):
                    count_doc = count_doc + 1
                # check if content is asset/app 
                elif is_assets(bin_dec):
                    count_asset = count_asset +1
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
                        count_ascii = count_ascii +1
                    else:
                        count_txt = count_txt + 1
            except:
                try:
                    # check binary data contains url 
                    if check_website(str(binary)):
                        count_http = count_http + 1 
                    # check binary data contains document 
                    elif docproof(str(binary)):
                        count_doc = count_doc + 1
                    # check binary data contains assets/Apps 
                    elif is_assets(str(binary)):
                        count_asset = count_asset +1
                    # else binary data not definable
                    elif  hex_int(str(binary)):
                        count_dig += 1
                    elif is_ascii(str(binary)) and is_text(str(binary.decode(__ASCII__))):
                        count_txt = count_txt + 1
                    else:
                        count_ud = count_ud +1
                        i.append(len(j)/2)
                        #save_op_sql(i)
                # hex not decodable 
                except:
                    #f.write("%s\n" % str(binary))
                    count_ud = count_ud +1
                    i.append(len(j)/2)
                    #save_op_sql(i)


    #  (x,_) part of a tuple --> number of found contents
    x = ['Empty',  'Error',     'Not Hex',    'Odd Lenght', 'Website',   
        'Number',  'Text',    'DOCPROOF', 'Assets',  'Ascii Unknown',    'Not decodable']

    #  (_,y) part of a tuple --> name of found contents
    y = [count_op, count_error, count_not_hex, count_odd,    count_http, 
        count_dig, count_txt, count_doc,   count_asset, count_ascii, count_ud]

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


# check if hex is a document
def docproof(bin_dec):
    sub = ('DOCPROOF','FACTOM00' ,'Factom!!', 'Fa', 'CryptoTests-', 
        'CryptoProof-', 'STAMPD##', 'BITPROOF', 'ProveBit', 'RMBe', 'RMBd', 'ORIGMY', 'LaPreuve', 'UNicDC',
        'S1', 'S2', 'S3', 'S4', 'S5', 'BS', 'FA' )   
    if any(str(bin_dec).startswith(i) for i in sub):
        return True
    elif any(str(bin_dec).startswith('b"'+i)  for i in sub):
        return True
    elif any(str(bin_dec).startswith("""b'"""+i)  for i in sub):
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

# check if hex contains one of assets/App --> then it is an assets/App
def is_assets(bin_dec):
    sub = ('CNTRPRTY','SLDX:', 'CC', 'SPK', 'OA', 'omni', 'ASCRIBE', 'id', 'MG', 'EW',
        'SB.D', '1f00', '5888', '5808' )   
    try:
        if any(str(bin_dec).startswith(i) for i in sub):
            return True
        elif str(bin_dec).startswith('@') and bin_dec.encode('ascii'):
            return True
        elif any(str(bin_dec).startswith('b"'+i) for i in sub):
            return True
        elif any(str(bin_dec).startswith("""b'"""+i)  for i in sub):
            return True
    except:
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
        'PropertyProtected', 'data', '_', 'link', '?', '|', 'KC{','tt3', 'Bitcoin over capacity')
    if any(i in bin_dec for i in sub):
        return True
    elif (len(bin_dec) ==1) and (' ' in bin_dec):
        return True
    else:
        return False


