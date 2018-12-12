import matplotlib.pyplot as pyplot
from SQL import undef_qu as sql
from Diagram import hex_converting
import seaborn as sb
import numpy as np
import pandas as ps
import sqlite3
import threading 
import datetime



# connect the sqllite database and return connection
def diagram_weekly():
    connection = sqlite3.connect("blockchain_un.db")
    diagram_history_weekly(connection)


def unix_to_date(timestamp):
    d = datetime.datetime.fromtimestamp((timestamp))
    formatted_time = d.strftime('%Y-%m-%d')
    return formatted_time


def weekley_epoch(start_date):
    date_1 = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = date_1 + datetime.timedelta(days=1)
    date_1 = date_1.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    return end_date

def avarage(intarray):
    avg_weekly= sum(intarray) / len(intarray)
    return avg_weekly


def sort_db(dataframe):
     df = dataframe.sort_values(by=['tx_time'])
     return df



# create a chart showing the use of the OP_RETURN field in relation to time
def diagram_history_weekly (connection):
    # create dataframe by using pandas with corresponding SQL statement and the connection to database
     read_data = ps.read_sql_query(sql.get_count_daily_op_return(), connection)
     data = sort_db(read_data)
     t1 = [tuple(x) for x in data.values]
     array_av = []
     avarage_res = []
     start = t1[0][0]
     x=1
     #while len(t1) !=0:
     #for i in range(1,len(t1)): 
     try:
          while t1[x][0] != t1[-1][0]:
               if x == 7 :
                    avarage_res.append(avarage(array_av))
                    array_av = []
                    x = 1
               end = weekley_epoch(start)
               if str(end) in t1[x][0]:
                    #if(len(array_av) != 7):
                    array_av.append(t1[x-1][1])
                    array_av.append(t1[x][1])
               #else:
               #     avarage_res.append(avarage(array_av))
               #     array_av = []
               else:
               #     if(len(array_av) != 7):
                         array_av.append(0)
               #     else:
               #          avarage_res.append(avarage(array_av))
               #          array_av = []
               start = end
               x = x+1

     except:          
          pass                    
          

     print(avarage_res)





    
