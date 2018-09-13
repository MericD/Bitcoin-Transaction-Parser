from SQL import querys as qy
import sqlite3

__databaseFile = "blockchain.db"

def initTabel():
    connection = sqlite3.connect(__databaseFile)
    cursor = connection.cursor()

    execute_command(cursor,qy.get_create_table_query())
    execute_command(cursor,qy.get_create_tx_table_query())
    
    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()

def addBlock(block_number, create_date, transaction_id, version, tx_size ,vin_size, vout_size,op_result):
    connection = sqlite3.connect(__databaseFile)
    cursor = connection.cursor()

    print("Add block to table")
    
    execute_command(cursor,qy.get_add_block_query(block_number,create_date))
    execute_command(cursor,qy.get_add_tx_query(transaction_id, version, tx_size ,vin_size, vout_size, op_result, block_number))
    

    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()

def selectTable():
    connection = sqlite3.connect(__databaseFile)
    cursor = connection.cursor()

    execute_command(cursor,qy.get_select_table())
    print_table(cursor)

    execute_command(cursor,qy.get_select_table_tx())
    print_table(cursor)

    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()

def execute_command(cursor, sql_command):
    try:
        sql_command = str(sql_command)
        cursor.execute(sql_command)
    except sqlite3.IntegrityError:
        print('Oops!  That was no valid number: '+ str(sql_command) + 'Maybe the PRIMARY KEY exist!')

def print_table(cursor):
    print("Print table")
    result = cursor.fetchall()  
    for r in result:
        print(r)