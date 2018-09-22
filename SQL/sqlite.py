from SQL import querys as qy
import sqlite3

def initTabel(connection):
    cursor = connection.cursor()

    __execute_command(cursor,qy.get_create_table_query())
    __execute_command(cursor,qy.get_create_tx_table_query())
    
    # never forget this, if you want the changes to be saved:
    connection.commit()

def addBlock(connection, block_number, create_date):
    cursor = connection.cursor()

    print("Add block to table")
    
    __execute_command(cursor,qy.get_add_block_query(block_number,create_date))
    

    # never forget this, if you want the changes to be saved:
    connection.commit() 

def addTrans(connection,  block_number, transaction_id, version, tx_size ,vin_size, vout_size,op_return):
    cursor = connection.cursor()

    print("Add trans to table")
    __execute_command(cursor,qy.get_add_tx_query(transaction_id, version, tx_size ,vin_size, vout_size, op_return, block_number))
    
    # never forget this, if you want the changes to be saved:
    connection.commit()

def __execute_command(cursor, sql_command):
    try:
        sql_command = str(sql_command)
        cursor.execute(sql_command)
    except sqlite3.IntegrityError:
        print('Oops!  That was no valid number: '+ str(sql_command) + 'Maybe the PRIMARY KEY exist!')