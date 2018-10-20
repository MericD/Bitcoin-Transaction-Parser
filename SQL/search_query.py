#SQL-Statments are private and doesn`t exist a set function

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
__filtered_OP = """CREATE TABLE IF NOT EXISTS filter_op (
block_number integer INTEGER PRIMARY KEY,
transaction_id text,
tx_value text,
op_return text,
op_length integer,
tx_address text,
FOREIGN KEY (transaction_id) REFERENCES tx (transaction_id));"""



# SQL statment to add corresponding transaction information in filter_op 
__add_op_qy = """INSERT INTO filter_op 
    (block_number, transaction_id, tx_value, op_return, op_length, tx_address) 
    VALUES 
    ("{block_number}", "{transaction_id}", "{tx_value}", "{op_return}", "{op_length}", "{tx_address}")
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
def get_add_filtered_OP(bn, tx_id, tx_v, tx_op_return, op_l, tx_a):
    return __add_op_qy.format(block_number=bn, transaction_id=tx_id,  tx_value=tx_v, op_return=tx_op_return, op_length=op_l,tx_address = tx_a) 

