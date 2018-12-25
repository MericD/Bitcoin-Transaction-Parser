  # a private (SQL statment) query for selecting cloums in table tx and block 
# count dublicates in tx where block_number in block = block_number in tx
__count_number_of_op_return = """SELECT block_number, tx_time , COUNT(*) Count_Duplicate
FROM filter_op
GROUP BY block_number
ORDER BY COUNT(*) DESC;"""


  # a private (SQL statment) query for selecting cloums in table tx and block 
# count dublicates in tx where block_number in block = block_number in tx
__count_daily_op_return = """SELECT tx_time , COUNT(*) Count_Duplicate
FROM filter_op
GROUP BY tx_time
ORDER BY COUNT(*) DESC;"""

__check_tx_add = """SELECT transaction_id , prev_tx, block_number 
FROM filter_op;"""


# Returns the query counts the number of blocks with transactions with 
# an op_return field depending to created date of the block
def get_count_number_of_op_return():
    return __count_number_of_op_return

def get_count_daily_op_return():
    return __count_daily_op_return

def get_check_tx_add():
    return __check_tx_add
