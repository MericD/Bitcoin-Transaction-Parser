#SQL-Statments are private and doesn`t exist a set function

# a  private (SQL statment) query for creating table block --> contains generel information of the blockchain blocks
# block_number - the blocknumber 
# created date of corresponding block

__create_table_qy = """CREATE TABLE if not exists block ( 
    block_nummber INTEGER PRIMARY KEY, 
    create_date DATE
);"""

# a private (SQL statment) query for creating table tx --> contains information of corresponding transaction with columns 
# version integer - version number of transaction
# tx_size integer - size of transaction in byte
# vin_size integer - number of elements in vin
# vout_size integer - number of elements in vout
# tx_time - transaction time
# tx_value - sent Bitcoin
# op_return text - additional information in a transaction and need not be specified
# block_number - block number where the corresponding transaction is save
#
# block_number column referes to the column  block_number of table block

__create_tx_table_qy = """CREATE TABLE IF NOT EXISTS tx (
	transaction_id text INTEGER PRIMARY KEY,
	version integer,
	tx_size integer,
	vin_size integer,
	vout_size integer,
        tx_time integer,
        tx_value text,
	op_return text,
	block_number integer,
	FOREIGN KEY (block_number) REFERENCES block (block_number)
        );"""
  

  # a private (SQL statment) query for selecting cloums in table tx and block 
# count dublicates in tx where block_number in block = block_number in tx
__count_number_of_op_return = """SELECT block_number, create_date , COUNT(*) Count_Duplicate
FROM tx , block
WHERE block_number = block_nummber
GROUP BY block_nummber
ORDER BY COUNT(*) DESC;"""

# a private (SQL statment) query for selecting columns in tx 
# remove specific sting 'OP_RETURN' in ich line in column op_return
__rmv_op_and_analyze_hex = "SELECT block_number, transaction_id, tx_value, REPLACE(op_return, 'OP_RETURN ', '') FROM tx"

# a private (SQL statment) query for creating table filter_op 
# contains information of corresponding transaction with columns
# block_number - number of the block
# transaction_id - ID of transaction
# tx_value - sent Bitcoin
# op_return - additional information in a transaction and need not be specified
# op_length length of op_retun field
__filtered_OP = """CREATE TABLE IF NOT EXISTS filter_op(
                transaction_id text INTEGER PRIMARY KEY,
                tx_value real,
                 op_return text,
                 op_length integer,
                 tx_address text,
                 address_number integer,
                 block_number integer);"""


#"""CREATE TABLE IF NOT EXISTS filter_op (
#block_number integer INTEGER PRIMARY KEY,
#transaction_id text,
#tx_value text,
#op_return text,
#op_length integer,
#tx_address text,
#address_number integer,
#FOREIGN KEY (transaction_id) REFERENCES tx (transaction_id));"""



# SQL statment to add corresponding transaction information in filter_op 
__add_op_qy = """INSERT INTO filter_op 
    ( block_number, transaction_id, tx_value, op_return, op_length, tx_address, address_number) 
    VALUES 
    ( "{transaction_id}","{block_number}", "{tx_value}", "{op_return}", "{op_length}", "{tx_address}", "{address_number}")
;"""

# SQL statment to add corresponding block information in table-block 
__add_block_qy = """INSERT INTO block 
    (block_nummber, create_date) 
    VALUES 
    ({block_number},"{create_date}")
;"""

# SQL statment to add corresponding transaction information in table-tx 
__add_tx_qy = """INSERT INTO tx 
    (transaction_id, version, tx_size ,vin_size, vout_size, tx_time, tx_value, op_return, block_number) 
    VALUES 
    ("{transaction_id}", {version}, {tx_size}, {vin_size}, {vout_size}, {tx_time}, "{tx_value}", "{op_return}", {block_number})
;"""


# Returns the query counts the number of blocks with transactions with 
# an op_return field depending to created date of the block
def get_count_number_of_op_return():
    return __count_number_of_op_return

# Returns the query to get a transaction and the information of it to the table filtered_OP
def get_rmv_op_and_analyze_hex():
    return __rmv_op_and_analyze_hex

# Returns the query to get the filtered transactions with undefinable op_returns
def get_create_filtered_OP():
    return __filtered_OP

# Returns the query to add a transaction with undefinable op_returns to table filtered_OP
def get_add_filtered_OP( tx_id, bn, tx_v, tx_op_return, op_l, tx_a, a_num):
    return __add_op_qy.format(transaction_id = tx_id, block_number = bn, tx_value=tx_v, op_return=tx_op_return, op_length=op_l, tx_address = tx_a, address_number=a_num) 



# Returns the query to generate the table
def get_create_table_query():
    return __create_table_qy

# Returns the query to add a block and create date to the table-block
def get_add_block_query(bn,cd):
    return __add_block_qy.format(block_number=bn,create_date=cd) 

# Returns the query to generate the table transcation
def get_create_tx_table_query():
    return __create_tx_table_qy

# Returns the query to add a transaction and the information of it to the table-tx
def get_add_tx_query(tx_id, tx_v, tx_s ,tx_vin_size, tx_vout_size, tx_ti, tx_val, tx_op_return, tx_block_id):
    return __add_tx_qy.format(transaction_id=tx_id, version=tx_v, tx_size=tx_s, vin_size=tx_vin_size, vout_size=tx_vout_size, tx_time=tx_ti, tx_value=tx_val, op_return=tx_op_return, block_number=tx_block_id) 



