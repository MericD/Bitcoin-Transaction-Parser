import sqlite3
from SQL import sqlite as sql

def find_op_result(block_trans):
    print("find op result")
    return "find op result"

def save_result_in_databse(__databaseFile, find_block_trans):
    connection = sqlite3.connect(__databaseFile)
    sql.initTabel(connection)
    sql.addBlock(connection,1, "1961-10-25", "transaction_id2", 2, 200 ,300, 400, "op_result")
    sql.selectTable(connection)
    connection.close()