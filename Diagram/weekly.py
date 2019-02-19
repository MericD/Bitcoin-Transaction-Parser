import matplotlib.pyplot as pyplot
from SQL import querys as sql
from Diagram import hex_converting
import seaborn as sb
import numpy as np
import pandas as ps
import sqlite3
import datetime
import config

save_plots = 'plots/'
__databaseFile = config.CONFIG['database_file_name']
sb.set(style="dark", color_codes=True)

# connect the sqllite database and return connection
def diagram_weekly():
    connection = sqlite3.connect(__databaseFile)
    avarage_line_plot(connection)

# converte datetime
def unix_to_date(timestamp):
    d = datetime.datetime.fromtimestamp((timestamp))
    formatted_time = d.strftime('%Y-%m-%d')
    return formatted_time
# 
def weekley_epoch(start_date):
    date_1 = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = date_1 + datetime.timedelta(days=1)
    date_1 = date_1.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    return end_date

def avarage(intarray):
    avg_weekly= sum(intarray) / len(intarray)
    return avg_weekly

# sort dataframe by date
def sort_db(dataframe):
     df = dataframe.sort_values(by=['tx_time'])
     return df



# create a chart showing the use of the OP_RETURN field in relation to time
def weekly_avarage_clc (connection):
     avarage_year2013 = []
     avarage_year2014 = []
     avarage_year2015 = []
     avarage_year2016 = []
     avarage_year2017 = []
     avarage_year2018 = []  

    # create dataframe by using pandas with corresponding SQL statement and the connection to database
     read_data = ps.read_sql_query(sql.get_count_daily_op_return(), connection)
     data = sort_db(read_data)
     t1 = [tuple(x) for x in data.values]
     array_av = []
     x=0
     i = 0
     while t1[i+1][0] not in t1[-1][0]:
               if x == 0:
                    end = weekley_epoch(t1[0][0])
                    array_av.append(t1[i][1])

               if str(end) in t1[i+1][0]:              
                    array_av.append(t1[i+1][1])
                    i = i+1
                    x = x+1
                    end = weekley_epoch(end)
               else:
                    array_av.append(0)
                    x = x+1
                    end = weekley_epoch(end)
               
               if (t1[-1][0] == str(end)):
                    break
               if len(array_av) == 7:
                    if "2013" in end:
                         avarage_year2013.append(avarage(array_av))
                    elif "2014" in end:
                         avarage_year2014.append(avarage(array_av))
                    elif "2015" in end:
                         avarage_year2015.append(avarage(array_av))
                    elif "2016" in end:
                         avarage_year2016.append(avarage(array_av))
                    elif "2017" in end:
                         avarage_year2017.append(avarage(array_av))
                    elif "2018" in end:
                         avarage_year2018.append(avarage(array_av))
                    array_av = []
     array_all = []
     array_all.append(avarage_year2013)
     array_all.append(avarage_year2014)
     array_all.append(avarage_year2015)
     array_all.append(avarage_year2016)
     array_all.append(avarage_year2017)
     array_all.append(avarage_year2018)

     print(len(avarage_year2015))
     print(array_tup(avarage_year2013))
     return array_all


# plooting yearly occurences of OP_RETURN in weekly avarage
def avarage_line_plot (connection):
     result_array = weekly_avarage_clc(connection)

     result_array2013 = array_tup(result_array[0])
     x_val13 = [x for x,_ in result_array2013]
     y_val13 = [y for _,y in result_array2013]

     result_array2014 = array_tup(result_array[1])
     x_val14 = [x for x,_ in result_array2014]
     y_val14 = [y for _,y in result_array2014]

     result_array2015 = array_tup(result_array[2])
     x_val15 = [x for x,_ in result_array2015]
     y_val15 = [y for _,y in result_array2015]

     result_array2016 = array_tup(result_array[3])
     x_val16 = [x for x,_ in result_array2016]
     y_val16 = [y for _,y in result_array2016]

     result_array2017 = array_tup(result_array[4])
     x_val17 = [x for x,_ in result_array2017]
     y_val17 = [y for _,y in result_array2017]

     result_array2018 = array_tup(result_array[5])
     x_val18 = [x for x,_ in result_array2018]
     y_val18 = [y for _,y in result_array2018]

     d13 = {'week': x_val13, 'avarage': y_val13}
     pdnumsqr13 = ps.DataFrame(d13)
     sb.lineplot(x='week', y='avarage', data=pdnumsqr13,label="2013")

     d14 = {'week': x_val14, 'avarage': y_val14}
     pdnumsqr14 = ps.DataFrame(d14)
     sb.lineplot(x='week', y='avarage', data=pdnumsqr14,label="2014")

     d15 = {'week': x_val15, 'avarage': y_val15}
     pdnumsqr15 = ps.DataFrame(d15)
     sb.lineplot(x='week', y='avarage', data=pdnumsqr15,label="2015")

     d16 = {'week': x_val16, 'avarage': y_val16}
     pdnumsqr16 = ps.DataFrame(d16)
     sb.lineplot(x='week', y='avarage', data=pdnumsqr16,label="2016")

     d17 = {'week': x_val17, 'avarage': y_val17}
     pdnumsqr17 = ps.DataFrame(d17)
     sb.lineplot(x='week', y='avarage', data=pdnumsqr17,label="2017")

     d18 = {'week': x_val18, 'avarage': y_val18}
     pdnumsqr18 = ps.DataFrame(d18)
     sb.lineplot(x='week', y='avarage', data=pdnumsqr18,label="2018")

     fig2 = pyplot.gcf()
     pyplot.draw()
     fig2.savefig(save_plots+'time_line_yearly.png', dpi = 1000)
     fig2.savefig(save_plots+'time_line_yearly.pdf', dpi = 1000)
     pyplot.close()
     
     # bar chart for every yar separatly
     bar1 = sb.barplot(x='week',y= 'avarage',data=pdnumsqr13, label="2013", color='#2A649F')
     fig = pyplot.gcf()
     pyplot.draw()
     fig.autofmt_xdate()
     fig.savefig(save_plots+'bar_chart_2013.png', dpi = 1000)
     fig.savefig(save_plots+'bar_chart_2013.pdf', dpi = 1000)
     pyplot.close()     

     sb.barplot(x='week',y= 'avarage',data=pdnumsqr14, label="2014", color= '#2A649F')
     fig = pyplot.gcf()
     pyplot.draw()
     fig.autofmt_xdate()
     fig.savefig(save_plots+'bar_chart_2014.png', dpi = 1000)
     fig.savefig(save_plots+'bar_chart_2014.pdf', dpi = 1000)
     pyplot.close()    

     sb.barplot(x='week',y= 'avarage',data=pdnumsqr15, label="2015", color='#2A649F')
     fig = pyplot.gcf()
     pyplot.draw()
     fig.autofmt_xdate()
     fig.savefig(save_plots+'bar_chart_2015.png', dpi = 1000)
     fig.savefig(save_plots+'bar_chart_2015.pdf', dpi = 1000)
     pyplot.close() 

     sb.barplot(x='week',y= 'avarage',data=pdnumsqr16, label="2016", color='#2A649F')
     fig = pyplot.gcf()
     pyplot.draw()
     fig.autofmt_xdate()
     fig.savefig(save_plots+'bar_chart_2016.png', dpi = 1000)
     fig.savefig(save_plots+'bar_chart_2016.pdf', dpi = 1000)
     pyplot.close() 

     sb.barplot(x='week',y= 'avarage',data=pdnumsqr17, label="2017", color='#2A649F')
     fig = pyplot.gcf()
     pyplot.draw()
     fig.autofmt_xdate()
     fig.savefig(save_plots+'bar_chart_2017.png', dpi = 1000)
     fig.savefig(save_plots+'bar_chart_2017.pdf', dpi = 1000)
     pyplot.close()  

     sb.barplot(x='week',y= 'avarage',data=pdnumsqr18, label="2018", color='#2A649F')
     fig = pyplot.gcf()
     pyplot.show()
     pyplot.draw()
     fig.autofmt_xdate()
     fig.savefig(save_plots+'bar_chart_2018.png', dpi = 1000)
     fig.savefig(save_plots+'bar_chart_2018.pdf', dpi = 1000)
     pyplot.close()    


def array_tup(array):
     con_arr = []
     x = 1
     for i in array:
          if len(array) <10 and x == 0:
               con_arr.append((52,i))
               x= x+1
          elif len(array) <10 :
               con_arr.insert(52-x,(52-x,i))
               x= x+1
          else:
               con_arr.append((x,i))
               x= x+1
     return con_arr



    
