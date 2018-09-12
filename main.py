from SQL import sqlite as sql
from rpc import rpc

print("The block analysis begins.")

block_trans = rpc.get_transactions()
print(block_trans)

#TODO find OP_RESULT, etc 

#TODO save it in database
sql.initTabel()
sql.addBlock(2,"1961-10-25")
sql.selectTable()