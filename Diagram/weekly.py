import matplotlib.pyplot as pyplot
from SQL import undef_qu as sql
from Diagram import hex_converting
import seaborn as sb
import numpy as np
import pandas as ps
import sqlite3
import threading 
import datetime



def unix_to_date(timestamp):
    d = datetime.datetime.fromtimestamp((timestamp))
    formatted_time = d.strftime('%Y-%m-%d')
    print(d)
    print(formatted_time)
    return formatted_time


def weekley_epoch(start_date):
    date_1 = start_date
    end_date = date_1 + datetime.timedelta(days=1)

    return end_date


# connect the sqllite database and return connection
def diagram_weekly():
    connection = sqlite3.connect("unknown_blockchain.db")
    diagram_history_weekly(connection)

def avarage(intarray):
    avg_weekly= sum(intarray) / len(intarray)
    return avg_weekly


def find_daily_usage():
    return 0

def sort_db(dataframe):
     df = dataframe.sort_values(by=['tx_time'])
     return df



# create a chart showing the use of the OP_RETURN field in relation to time
def diagram_history_weekly (connection):
    # create dataframe by using pandas with corresponding SQL statement and the connection to database
    read_data = ps.read_sql_query(sql.get_count_daily_op_return(), connection)
    data = sort_db(read_data)
    print(read_data)
    
