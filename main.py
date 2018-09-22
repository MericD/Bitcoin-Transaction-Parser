from rpc import rpc
from Core import core
import config

###Parametet
# Name of the database
__databaseFile = config.CONFIG['database_file_name']


#The first block witch be analyzed
#__start_block =1
__start_block = config.CONFIG['start_block']

#The last block witch be analyzed
#__end_block =1
__end_block = config.CONFIG['end_block']

#Get all Blocks and transactions
block_trans={}

while __start_block < __end_block + 1:
    block_trans.update(rpc.get_transactions(__start_block))
    __start_block += 1

#Filter all transaction witch doesn`t include an op_result
find_block_trans = core.find_op_result(block_trans)
 
#Save all transaction with an op_result
core.save_result_in_databse(__databaseFile, find_block_trans)
