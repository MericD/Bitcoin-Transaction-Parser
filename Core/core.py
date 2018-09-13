import sqlite3
from SQL import sqlite as sql
from Rpc import rpc

def find_op_result(block_trans):
    block_trans_result = {}
    for key, trans in block_trans.items():
        trans_result = transaction_contens_op_result(trans)
        block_trans_result.update({key:trans_result})
    return block_trans_result

def save_result_in_databse(__databaseFile, find_block_trans):
    connection = sqlite3.connect(__databaseFile)
    sql.initTabel(connection)
    sql.addBlock(connection,1, "1961-10-25", "transaction_id2", 2, 200 ,300, 400, "op_result")
    sql.selectTable(connection)
    connection.close()

def transaction_contens_op_result(trans):
    trans_result = {}
    for key, value in trans.items():
        potential_op_result = value["vout"][0]["scriptPubKey"]["asm"]
        if potential_op_result.startswith('0496'):
            trans_result.update({key:value})
    return trans_result