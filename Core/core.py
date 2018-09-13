import sqlite3
from SQL import sqlite as sql
from Rpc import rpc

def find_op_result(block_trans):
    block_trans_result = {}
    for key, trans in block_trans.items():
        trans_result = transaction_contens_op_result(trans)
        if len(trans_result) > 0:
            block_trans_result.update({key:trans_result})
    return block_trans_result

def save_result_in_databse(__databaseFile, find_block_trans):
    connection = sqlite3.connect(__databaseFile)
    sql.initTabel(connection)
    for key_b, trans in find_block_trans.items():
        block_number=key_b
        create_date="1961-10-25" #TODO
        sql.addBlock(connection,block_number, create_date)

        for key_t, value in trans.items():
            transaction_id= key_t
            version=2 #TODO
            tx_size=200 #TODO
            vin_size=300 #TODO
            vout_size=400 #TODO
            op_result= get_op_result(value)
            sql.addTrans(connection,block_number, transaction_id, version, tx_size ,vin_size, vout_size,op_result)

    connection.close()

def transaction_contens_op_result(trans):
    trans_result = {}
    for key, value in trans.items():
        for i in range(len(value["vout"])):
            op_result = get_op_result(value)
            if "" != op_result:
                trans_result.update({key:value})
    return trans_result

def get_op_result(value):
    op_result = ""
    for i in range(len(value["vout"])):
        potential_op_result = value["vout"][i]["scriptPubKey"]["asm"]
        #if potential_op_result.startswith('0496b53'): #For Block 1 to find a transcation
        if potential_op_result.startswith('OP_RETURN'):
            #add every op_result to the object
            if "" == op_result:
                op_result = str(potential_op_result)
            else:
                op_result = op_result + ", " + str(potential_op_result)

    return op_result 