#SQL-Statments are private and doesn`t exist a set function
__create_table_qy = """CREATE TABLE blockchain ( block_nummber INTEGER PRIMARY KEY, create_date DATE);"""
    
__add_block_qy = """INSERT INTO blockchain (block_nummber, create_date) VALUES (1,"1961-10-25");"""

__select_table = """SELECT * FROM blockchain;"""

# Returns the query to generate the table.
def get_create_table_query():
    return __create_table_qy

# Returns the query to add a block to the table
def get_add_block_query():
    return __add_block_qy 

def get_select_table():
    return __select_table