import matplotlib.pyplot as pyplot
from SQL import search_query as sql
import seaborn as sb
import numpy as np
import pandas as ps
import sqlite3



# connect the sqllite database and return connection
def create_diagrams():
    connection = sqlite3.connect("blockchain.db")
    diagram_history_op_return(connection)
    diagram_content_OP_RETURN(connection)


# create a chart showing the use of the OP_RETURN field in relation to time
def diagram_history_op_return (connection):
    # create dataframe by using pandas with corresponding SQL statement and the connection to database
    read_data = ps.read_sql_query(sql.count_number_of_op_return, connection)
    
    # get corresponding columns for the axes
    data = ps.DataFrame(read_data,columns=['create_date','Count_Duplicate'])
    # x-axis: get create_date of blocks that ar containing OP_RETURNS in datetime 
    x_val = ps.Series(ps.to_datetime(data['create_date']))
    # y-axis: get number of OP_RETURNS in a Block depending on create_date as an array
    y_val = np.array(data['Count_Duplicate'])

    # bulid with the values for x and y an series for plotting 
    s = ps.Series(y_val, index=x_val)
    # plot line diagram with corresponing x and y values and show it
    #s.plot()
    #pyplot.show()




# create a chart showing the content of the OP_RETURN fields in relation to number of the content
def diagram_content_OP_RETURN (connection):
    # create dataframe by using pandas with corresponding SQL statement and the connection to database
    read_data = ps.read_sql_query(sql.content_op_return, connection)
    # put values in data frame in an array
    list_str_op_retrun = np.array(read_data)

    # values for diagram with content of OP_RETURN an number of different contents
    result_array = analyze_op_hex(list_str_op_retrun)
    # get object for y-axisl    
    y_val = [x for x,_ in result_array]
    # get values for x-axis
    x_val = [y for _,y in result_array]

    #plot bar chart with corresponing x and y values and show it
    f, (ax1,ax2,ax3) = pyplot.subplots(3, 1, figsize=(7, 5), sharex=True)
    sb.barplot(x=y_val, y=x_val, palette="rocket", ax=ax1)
    ax1.axhline(0, color="k", clip_on=True)
    ax1.set_ylabel("Qualitative")
    
    sb.despine(bottom=True)
    pyplot.setp(f.axes, yticks=[])
    pyplot.tight_layout(h_pad=2)
    pyplot.show()



# funtion to analyse the op-return content
def analyze_op_hex (op_array):
    clean_list = []
    # remove all 'OP_RETURN' as word in array and store hex in new array 'clean_list'
    for i in op_array:
        for opR in i:
            clean_list = np.append(clean_list , np.array(opR.replace('OP_RETURN ', '')))
    print(clean_list)

    ############# analyze part here #############


    # return a list with number of different OP_RETURN field contents
    content = [[1,'a'],[2,'b'],[3,'c'],[4,'d']]
    return content
    
    

