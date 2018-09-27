#SQL-Statments are private and doesn`t exist a set function

count_number_of_op_return = """SELECT block_number, create_date , COUNT(*) Count_Duplicate
FROM tx , block
WHERE block_number = block_nummber
GROUP BY block_nummber
ORDER BY COUNT(*) DESC;"""


test= "SELECT block_nummber, create_date FROM block"

def get_count_number_of_op_return():
    return count_number_of_op_return