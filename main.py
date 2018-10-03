from rpc import rpc
from Core import core
from Diagram import diagram
import config

###Parametet
# Name of the database 
__databaseFile = config.CONFIG['database_file_name']


#The first block to analyze
#__start_block =1
__start_block = config.CONFIG['start_block']

#The last block to analyze
#__end_block =1
__end_block = config.CONFIG['end_block']

#Get all Blocks and transactions in range of __start_block to __end_block
block_trans = {}

#while __start_block < __end_block + 1:
  #  block_trans.update(rpc.get_transactions(__start_block)[0])
   # __start_block += 1

#Filter all transactions that contain a field OP_RETURN 
#find_block_trans = core.find_op_return(block_trans)
 
#Save all transaction with a OP_RETURN field
#core.save_result_in_database(__databaseFile, find_block_trans)

# create diagram by using created database
diagram.create_diagrams()
