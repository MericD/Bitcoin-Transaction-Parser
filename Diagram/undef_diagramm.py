
import matplotlib.pyplot as pyplot
from SQL import undef_qu as sql
from SQL import querys as sq
from Diagram import hex_converting
import seaborn as sb
import numpy as np
import pandas as ps
import sqlite3
import threading 
import time

sb.set(style="whitegrid")


# connect the sqllite database and return connection
def create_diagrams():
    connection = sqlite3.connect("undef_blockchain.db")
    connection1 = sqlite3.connect("unknown_blockchain.db")
    connection2 = sqlite3.connect("blockchain.db")
    diagram_history_op_return(connection,connection1,connection2)


# create a chart showing the use of the OP_RETURN field in relation to time
def diagram_history_op_return (connection,connection1,connection2):
    # create dataframe by using pandas with corresponding SQL statement and the connection to database
    read_data = ps.read_sql_query(sql.get_count_number_of_op_return(), connection)
    read_data1 = ps.read_sql_query(sql.get_count_number_of_op_return(), connection1)  
    read_data2 = ps.read_sql_query(sq.get_count_number_of_op_return(), connection2)  

    # get corresponding columns for the axes
    data = ps.DataFrame(read_data,columns=['tx_time','Count_Duplicate'])
    data1 = ps.DataFrame(read_data1,columns=['tx_time','Count_Duplicate'])
    data2 = ps.DataFrame(read_data2,columns=['create_date','Count_Duplicate'])
    # x-axis: get create_date of blocks that ar containing OP_RETURNS in datetime 
    x_val = ps.Series(ps.to_datetime(data['tx_time']))
    x_val1 = ps.Series(ps.to_datetime(data1['tx_time']))
    x_val2 = ps.Series(ps.to_datetime(data2['create_date']))
    # y-axis: get number of OP_RETURNS in a Block depending on create_date as an array
    y_val2 = np.array(data2['Count_Duplicate'])

    # y-axis: get number of OP_RETURNS in a Block depending on create_date as an array
    y_val = np.array(data['Count_Duplicate'])
    y_val1 = np.array(data1['Count_Duplicate'])

    # bulid with the values for x and y an series for plotting 
    s = ps.Series(y_val, index=x_val)
    s1 = ps.Series(y_val1, index=x_val1)
    s2 = ps.Series(y_val2, index=x_val2)
    # plot line diagram with corresponing x and y values and show it
    s2.plot()
    s.plot()
    s1.plot()  
    
    # store current diagram, show it, store it as file and close it for drawing other diagrams
    fig1 = pyplot.gcf()
    pyplot.show()
    pyplot.draw()
    fig1.savefig('undef_history.png', dpi=100)
    pyplot.close()
