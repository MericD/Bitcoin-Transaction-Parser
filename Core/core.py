import sqlite3
from SQL import sqlite as sql
from rpc import rpc
import time

def find_op_return(block_trans):
    block_trans_result = {}
    for key, trans in block_trans.items():
        trans_result = transaction_contens_op_return(trans)
        if len(trans_result) > 0:
            block_trans_result.update({key:trans_result})
    return block_trans_result

def save_result_in_databse(__databaseFile, find_block_trans):
    connection = sqlite3.connect(__databaseFile)
    sql.initTabel(connection)
    for key_b, trans in find_block_trans.items():
        block_number=key_b
        create_date=time.ctime(1410356926)
        sql.addBlock(connection,block_number, create_date)

        for key_t, value in trans.items():
            transaction_id= key_t
            version= value['version']
            tx_size=value['size']
            vin_size=len(value['vin'])
            vout_size=len(value['vout'])
            op_return= get_op_return(value)
            sql.addTrans(connection,block_number, transaction_id, version, tx_size ,vin_size, vout_size,op_return)

    connection.close()

def transaction_contens_op_return(trans):
    trans_result = {}
    for key, value in trans.items():
        for i in range(len(value["vout"])):
            op_return = get_op_return(value)
            if "" != op_return:
                trans_result.update({key:value})
    return trans_result

def get_op_return(value):
    op_return = ""
    for i in range(len(value["vout"])):
        potential_op_return = value["vout"][i]["scriptPubKey"]["asm"]
        #if potential_op_return.startswith('0496b53'): #For Block 1 to find a transcation
        if potential_op_return.startswith('OP_RETURN'):
            #add every op_return to the object
            if "" == op_return:
                op_return = str(potential_op_return)
            else:
                op_return = op_return + ", " + str(potential_op_return)

    return op_return 
