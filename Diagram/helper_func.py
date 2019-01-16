from Diagram import hex_config as hc
from SQL import sqlite as sql
from Core import core as c
from rpc import rpc
import sqlite3
import string
import datetime
from Diagram import weekly as w

__OP_PRETUN__= 'OP_RETURN'

# check if given object contains only hex
def is_hex(op):
    if all(c in string.hexdigits for c in str(op)):
        return True
    else:
        return False




# check if hex is a OP_RETURN
def is_OP(op):
    if __OP_PRETUN__ in str(op):
        return True
    else:
        return False



# check if hex is a website/Email
def check_website(bin_dec):
    if any(i in str(bin_dec) for i in hc.website):
        return True
    else:
        return False




# check if hex is a integer
def hex_int(digit):
    if all(i in hc.digit for i in digit):
        return True
    else:
        return False 
         



# check if hex is a document
def is_metadata(bin_dec):
    if any(str(bin_dec).startswith(i) for i in hc.metadata):
        return True
    elif (len(bin_dec) ==1) and (' ' in bin_dec):
        return False
    #elif any(i in str(bin_dec) for i in hc.metadata):
    #    return True
    #elif any(bin_dec.startwith("b'"+i) for i in hc.metadata):
    #    return True
    #elif any(bin_dec.startwith("b"+str('"')+i) for i in hc.metadata):
    #    return True
    else:
        return False





#check is metadata starter prefix in hexstring
def is_metadata_hex(hex_str):
    if any(str(hex_str).startswith(i) for i in hc.prefix_meta):
        return True
    elif any(str(hex_str).startswith("b"+"'"+i) for i in hc.prefix_meta):
        return True
    elif any(str(hex_str).startswith("b"+'"'+i) for i in hc.prefix_meta):
        return True
    else:
        return False




def is_hex_op(binary):
    if all(i in hc.hex_dig for i in binary):
        return True
    elif any(str(binary).startswith(i) for i in hc.hex_string_prefix):
        if binary.startswith('XLX'):
            return True
        else:
            for i in hc.hex_string_prefix:
                if binary.startswith(i):
                    binary = binary[len(i):]
                    break
            if all(i in hc.hex_dig for i in binary):    
                return True
    else:
        return False



# find all unknown ascii 
def unknown_ascii(bin_dec):
    alpha = hc.lower_alph + hc.upper_alph + hc.digit #+ hc.symbol
    if ' ' not in bin_dec:
        if all(i in alpha for i in bin_dec):
            return True
        elif any(str(bin_dec).startswith(i) for i in hc.unknown_ascii_word_prefix):
            #for i in hc.unknown_ascii_word:
            #    if bin_dec.startswith(i):
            #        bin_dec = bin_dec[len(i):]
            #        break
            #if all(i in alpha for i in bin_dec):    
            return True
        elif any(i in bin_dec for i in hc.unknown_ascii_word):
            return True
        else:
            return False





def spacer(binary):
    c =0
    for i in binary:
        if i == ' ':
            c = c+1
    if c > 3:
        return True
    else: 
        return False





# check if hex is ascii and contains only letters or words
def no_digit(bin_dec):
    if any(i in bin_dec for i in hc.digit):
        return False
    else:
        return True



# check if hex is ascii 
def is_ascii(bin_dec):
    if(all(ord(char) < 128 for char in bin_dec)):
        return True
    else:
        return False




# personal text checker to find some words in OP_Retrun and classify as text
def is_text(bin_dec):   
    if any(i in bin_dec for i in hc.text_check):
        return True
    elif (len(bin_dec) ==1) and (' ' in bin_dec):
        return True
    elif( bin_dec.startswith('@')):
        return True       
    else:
        return False



# save undefinable OP_RETURN fields in an additional table for more analysis
# databse table contains only the transaction id, block number and 
# transaction value of the corresponding op_return field 

rpc_connection = rpc.start_connection_to_rpc()

def save_op_sql(numarray):
    connection = sqlite3.connect('db1.db')
    sql.initTabel(connection)

    raw_tx = rpc.decoded_transactions_address(rpc_connection, numarray[1])
    senAdd = c.get_sender_address_of_op_tx(raw_tx)
    recAdd = c.get_address_of_op_tx(raw_tx)

    arr=[]
    b = 0.0
    a = []
    arr = numarray[2].split(", ")

    for i in range(len(arr)):
        if 'E' in arr[i]:
            b = arr[i][0]
            b = float(b)
        else:
            b = float(arr[i])
        a.append(b)
        

    block_number = numarray[0] 
    transaction_id  =  numarray[1]
    prev_tx_id = c.get_previous_txID_of_btc(raw_tx)
    tx_value = a
    op_return = __OP_PRETUN__ + ' ' + numarray[3]
    s_address= senAdd[0]
    op_length = numarray[4]
    r_address = recAdd[0]
    address_number = recAdd[1]
    tx_time = w.unix_to_date(int(rpc.get_all_transactions(rpc_connection,rpc.get_the_block_hash(rpc_connection,block_number))[1]))

    sql.addOP(connection, prev_tx_id, block_number, transaction_id, tx_value, op_return, op_length, s_address, r_address, address_number, tx_time)
    connection.close()
