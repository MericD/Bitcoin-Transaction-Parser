#SQL-Statments are private and doesn`t exist a set function
__create_table_qy = """CREATE TABLE if not exists blockchain ( 
    block_nummber INTEGER PRIMARY KEY, 
    create_date DATE
);"""

__create_tx_table_qy = """CREATE TABLE IF NOT EXISTS tx (
	transaction_id text INTEGER PRIMARY KEY,
	version integer,
	tx_size integer,
	vin_size integer,
	vout_size integer,
	op_result text,
	block_number integer,
	FOREIGN KEY (block_number) REFERENCES block (block_number)
);"""
   
__add_block_qy = """INSERT INTO blockchain 
    (block_nummber, create_date) 
    VALUES 
    ({block_number},"{create_date}")
;"""

__add_tx_qy = """INSERT INTO tx 
    (transaction_id, version, tx_size ,vin_size, vout_size, op_result, block_number) 
    VALUES 
    ("{transaction_id}", {version}, {tx_size}, {vin_size}, {vout_size}, "{op_result}", {block_number})
;"""

__select_table_qy = """SELECT * FROM blockchain;"""

__select_table_tx_qy = """SELECT * FROM tx;"""


# Returns the query to generate the table.
def get_create_table_query():
    return __create_table_qy

# Returns the query to add a block to the table
def get_add_block_query(bn,cd):
    return __add_block_qy.format(block_number=bn,create_date=cd) 

# Returns the query to select the table
def get_select_table():
    return __select_table_qy

# Returns the query to generate the table transcation.
def get_create_tx_table_query():
    return __create_tx_table_qy

# Returns the query to add a tx to the table
def get_add_tx_query(tx_id, tx_v, tx_s ,tx_vin_size, tx_vout_size, tx_op_result, tx_block_id):
    return __add_tx_qy.format(transaction_id=tx_id, version=tx_v, tx_size=tx_s, vin_size=tx_vin_size, vout_size=tx_vout_size, op_result=tx_op_result, block_number=tx_block_id) 

def get_select_table_tx():
    return __select_table_tx_qy


