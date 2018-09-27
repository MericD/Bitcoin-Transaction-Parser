
import matplotlib.pyplot as pyplot
import pandas as ps
from datetime import datetime
import sqlite3
from SQL import search_query as sql

# connect the sqllite database
# read data from sqllite database with corresponding sql statment (filter)

def read_blabla():
    connection = sqlite3.connect("blockchain.db")
    read_data = ps.read_sql_query(sql.count_number_of_op_return, connection)
    print(read_data)
    data = ps.DataFrame(read_data,columns=['block_number','Count_Duplicate'])
    print(data)
    data.plot()
    pyplot.show()

# data = [go.Scatter(x = read_data. , y = read_data['Count_Duplicate'])]
# py.plot(data)

#def drawPlot():
#dataset = ps.read_csv("test.txt", sep="|", header=0, encoding="utf8")

#var = dataset.groupby('ZEIT').Umsatz.sum()
#fig = pyplot.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.set_xlabel('Umsatz')
#ax1.set_ylabel('Standort')
#var.plot(kind='line')
#pyplot.show()


#dates = []
#for year in range(2012, 2018):
# for month in range(1, 12):
# dates.append(dt.datetime(year=year, month=month, day=1))
#
#plt.plot(dates[:9], y)

