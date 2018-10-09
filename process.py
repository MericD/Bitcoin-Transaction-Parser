import threading 
import main
import config



threads = []
result =[]

def fun_thrd(s,e):
    result.append(main.thread_fun(s,e))


e = 315000
r = 2000
#while (e < 400000) or (len(result) != 0):
#    if(e<400000):
#        # start threads 
#        for k in range(10):
#            s = e + 1 
#            e = e + r 
#            thr = threading.Thread(target=fun_thrd, args=(s,e))
#            threads.append(thr)
        # Start them all
#        for thread in threads:
#            thread.start()
#        for t in threads:
#            t.join()


    # store in sqlite
#    for i in result:
#        main.write_sql(config.CONFIG['database_file_name'], i)

#    threads = []
#    result = []

