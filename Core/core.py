import sqlite3
from SQL import sqlite as sql
from rpc import rpc
from Core import sender_add as addr
import time
import re



# find all transaction that contain an OP_RETURN field
# use dictionary (key) that contains all blocks and their transactions
def find_op_return(block_trans):
    #initialize a dictionary 
    block_trans_result = {}
    # find in dictionary-key ({block_number : trans_decoded}) all transactions with OP_RETURN
    for key, trans in block_trans.items():
        trans_result = transaction_contains_op_return(trans)
        if len(trans_result) > 0:
           # save found OP_RETURN in block_trans_result ({transactionID : content of OP_RETURN})
            block_trans_result.update({key:trans_result})
            #return new dictionary ({transactionID : decoded raw transaction information})
    return block_trans_result



# save all searched information in database file _databaseFIle
# find_block_trans contains ({transactionID : content of OP_RETURN})
def save_result_in_database(__databaseFile, find_block_trans):
    # opens a connection to the SQLite database file __databaseFile
    connection = sqlite3.connect(__databaseFile)
    # initialized SQL tables store in file __databaseFile
    sql.initTabel(connection)

    # search in dictionary ({key->block-number : value{key-> tx_ID : value->decoded raw transaction information}}) 
    for key_b, trans in find_block_trans.items():
       
        # the key of the dictionary find_block_trans is the blocknumber and store created-date of it
        block_number = key_b
        # set created date of block and convert int in time stamp
        create_date=time.ctime(int(rpc.get_transactions(key_b)[1]))
        # add information from dictionary to the created SQL table
        sql.addBlock(connection, block_number, create_date)

        # the specific value of the dictionary find_block_trans contains needed information for a transaction 
        # that contains an OP_RETURN field
        for key_t, value in trans.items():
            transaction_id = key_t
            version = value['version']
            tx_size = value['size']
            vin_size = len(value['vin'])
            vout_size = len(value['vout'])
            tx_time = 1 #value['time']
            tx_value = get_tx_value(value)
            op_return = get_op_return(value)
            # add information for transaction from dictionary value 
            # ({key->block-number : value -> decoded raw transaction information}) to the created SQL table
            sql.addTrans(connection,block_number, transaction_id, version, tx_size ,vin_size, vout_size, tx_time, tx_value, op_return)

    connection.close()



# filter all transactions that contains an OP_RETURN
def transaction_contains_op_return(trans):
    #initialize a dictionary 
    trans_result = {}
    # find in dictionary-key ({transactionID : decoded raw transaction information}) 
    for key, value in trans.items():
        # rearch in decoded raw transaction information in "vout" for OP_RETURN field
        for i in range(len(value["vout"])):
            #save found OP_RETURN in dictionary ({transactionID: OP_RETURN content})
            op_return = get_op_return(value)
            if "" != op_return:
                # update dictionary ({transactionID: OP_RETURN content}) 
                # if more than one OP_RETURN field is found in a transaction
                trans_result.update({key:value})
    # return dictionary ({transactionID: OP_RETURN content})
    return trans_result



# return all sent Bitcoin value fields in an transaction 
# value contains decoded raw transaction information 
def get_tx_value(value):
    tx_val = ""
    # search in "vout" (decoded raw transaction information) for value-field 
    for i in range(len(value["vout"])):
        potential_tx_value = value["vout"][i]["value"]
        # if no one value-field is found return empty string
        if "" == tx_val:
            tx_val = str(potential_tx_value)
        # else return value-field in transaction or add found value-field to tx_val
        else:
            tx_val = tx_val + ", " + str(potential_tx_value)
    return tx_val 



def get_previous_txID_of_btc(value):
    previous_txID = ""

    for i in range(len(value["vin"])):
        potential_tx_id = value["vin"][i]["txid"]
        if "" == previous_txID:
            previous_txID = str(potential_tx_id)
        else:
            previous_txID = previous_txID + ", " + str(potential_tx_id)
    return previous_txID 



# get OP_RETURN fields and content of them in a transaction
# value contains decoded raw transaction information 
def get_op_return(value):
    op_return = ""
    # search in "vout" (decoded raw transaction information) for OP_RETURN 
    for i in range(len(value["vout"])):
        potential_op_return = value["vout"][i]["scriptPubKey"]["asm"]
        #if potential_op_return.startswith('0496b53'): #For Block 1 to find a transcation
        # if you find a 'OP_RETURN' string in "vout"
        if potential_op_return.startswith('OP_RETURN'):
            # if no more OP_RETURN is found return the object
            if "" == op_return:
                op_return = str(potential_op_return)

             # else add every OP_RETURN to the object if one more is found 
            else:
                op_return = op_return + ", " + str(potential_op_return)
    # return string of found OP_RETURN fields
    return op_return 



# return addresses in a transaction
def get_address_of_op_tx(value):
    address = ""
    c = 0
    # search in "vout" (decoded raw transaction information) for value-field 
    for k , v in value.items():
        for i in range(len(v["vout"])):
            potential_tx_value = v["vout"][i]["scriptPubKey"]
            if 'addresses' in potential_tx_value:
                potential_tx_value = potential_tx_value["addresses"]
                for i in range(len(potential_tx_value)):
                    if "" == address:
                        address = str(potential_tx_value)
                        c = c+1
                    else:
                        address = address + ", " + str(potential_tx_value)
                        c = c+1
            else:
                pass
    return address,c


    # return addresses in a transaction
def get_sender_address_of_op_tx(value):
    address = ""
    a = ""
    potential_sender_add = ""
    # search in "vout" (decoded raw transaction information) for value-field 
    for k , v in value.items():
        for i in range(len(v["vin"])):
            potential_sender_add = v["vin"][i]
            if 'scriptSig' in potential_sender_add:
                potential_sender_add = potential_sender_add["scriptSig"]["asm"]
                potential_sender_add = re.sub(r'.*]', '', potential_sender_add)
                if " " in potential_sender_add:
                    potential_sender_add.replace(" ", "")
                    a = addr.PubkeyToAddress(potential_sender_add)
                    if "" == address:
                        address = str(a)
                    else:
                        address = address + ", " + str(a)
                else: 
                    address = "p2pk address"
            else: 
                address = "new coin!"
    return address, potential_sender_add