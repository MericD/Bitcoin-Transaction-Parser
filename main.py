from SQL import sqlite as sql
from bitcoinrpc import rpc

print("The block analysis begins.")

#TODO get transaction raw information for block 1

#TODO find OP_RESULT, etc 

#TODO save it in database
sql.initTabel()
sql.addBlock(2,"1961-10-25")
sql.selectTable()