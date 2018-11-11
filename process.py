import threading 
import main
import config



threads = []
result =[]
#c = 0
# call method from main and store result of threads in array
#def fun_thrd(s,e):
#    result.append(main.thread_fun(s,e))
#    c = c+1
    
# range of blocks threads search for transactions with OP_RETURN    e= end of range
# r is range for each thread to search 
e = 226000
r = 1

# search while you reach last block in range 
#while (e < 546000):
#    if(e< 546000):
#        # start threads 
        # k is number of threads that are startet per while-loop
#        for k in range(60):
            # s = start of searchable range
#            s = e + 1 
#            e = e + r 
            # call 10 threads with different ranges and the function fun_thrd
#            thr = threading.Thread(target=fun_thrd, args=(s,e))
#            threads.append(thr)
        # Start them all
#        for thread in threads:
#            thread.start()
#        for t in threads:
#            t.join()


    # store in sqlite
#    while True:
#        if c == 60:
#            break
#        else:
#            pass

#    for i in result:
#        pritn("inn")
#        main.write_sql(config.CONFIG['database_file_name'], i)

    # set thread array and result to default 
    #result = []
    #threads = []
    #c=0

