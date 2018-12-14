from rpc import rpc
from Core import core
from Diagram import diagram
from Diagram import undef_diagramm
import config


###Parameter
# name of the database 
#__databaseFile = config.CONFIG['database_file_name']
# the first block to analyze
#__start_block = config.CONFIG['start_block']
# the last block to analyze
#__end_block = config.CONFIG['end_block']

# get all Blocks and transactions in range of __start_block to __end_block
#block_trans = {}
#while __start_block < __end_block + 1:
#    block_trans.update(rpc.get_transactions(__start_block)[0])
#    __start_block += 1

# filter all transactions that contain a field OP_RETURN 
#find_block_trans = core.find_op_return(block_trans)

# save all transaction with a OP_RETURN field
#core.save_result_in_database(__databaseFile, find_block_trans)

# create diagram by using created database
diagram.create_diagrams()

#undef_diagramm.create_diagrams()
   # aray = [data.loc[1]]

#from Diagram import weekly 

#weekly.diagram_weekly()
