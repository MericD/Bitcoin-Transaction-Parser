from Rpc import rpc
from Core import core

__databaseFile = "blockchain.db"
find_block_trans = {}
print("The block analysis begins.")

block_trans = rpc.get_transactions(1)

find_block_trans = core.find_op_result(block_trans)
 
core.save_result_in_databse(__databaseFile, find_block_trans )