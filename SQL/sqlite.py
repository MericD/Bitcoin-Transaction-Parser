from SQL import querys as qy

def initTabel():
    print("We load the following statemant: " + str(qy.get_create_table_query()))