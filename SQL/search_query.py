#SQL-Statments are private and doesn`t exist a set function

count_number_of_op_return = """SELECT block_number, create_date , COUNT(*) Count_Duplicate
FROM tx , block
WHERE block_number = block_nummber
GROUP BY block_nummber
ORDER BY COUNT(*) DESC;"""

content_op_return = "SELECT op_return FROM tx"

count_same_op = "SELECT op_return, COUNT(*) FROM tx GROUP BY op_return HAVING COUNT(*) > 1"

select_analyze_op = "SELECT transaction_id , tx_value, op_return FROM tx"

def get_count_number_of_op_return():
    return count_number_of_op_return

def get_content_op_return():
    return content_op_return