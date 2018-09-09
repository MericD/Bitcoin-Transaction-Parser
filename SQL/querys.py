#SQL-Statments are private and doesn`t exist a set function
__create_table_qy = """CREATE TABLE if not exists blockchain ( block_nummber INTEGER PRIMARY KEY, create_date DATE);"""
    
__add_block_qy = """INSERT INTO blockchain (block_nummber, create_date) VALUES ({block_number},"{create_date}");"""

__select_table_qy = """SELECT * FROM blockchain;"""

# Returns the query to generate the table.
def get_create_table_query():
    return __create_table_qy

# Returns the query to add a block to the table
def get_add_block_query(bn,cd):
    return __add_block_qy.format(block_number=bn,create_date=cd) 

# Returns the query to select the table
def get_select_table():
    return __select_table_qy
