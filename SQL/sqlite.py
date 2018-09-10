from SQL import querys as qy
import sqlite3

__databaseFile = "blockchain.db"

def initTabel():
    connection = sqlite3.connect(__databaseFile)
    cursor = connection.cursor()

    print("Init Table")
    sql_command = str(qy.get_create_table_query())
    cursor.execute(sql_command)

    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()

def addBlock(block_number,create_date):
    connection = sqlite3.connect(__databaseFile)
    cursor = connection.cursor()

    print("Add block to table")
    sql_command = str(qy.get_add_block_query(block_number,create_date))
    try:
        cursor.execute(sql_command)
    except sqlite3.IntegrityError:
        print('Oops!  That was no valid number: '+ str(block_number))

    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()

def selectTable():
    connection = sqlite3.connect(__databaseFile)
    cursor = connection.cursor()

    print("Select table")
    sql_command = str(qy.get_select_table())
    cursor.execute(sql_command)

    print("Print table")
    result = cursor.fetchall()  
    for r in result:
        print(r)

    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()
