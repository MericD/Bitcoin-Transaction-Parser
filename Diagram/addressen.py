from SQL import undef_qu as sql
import sqlite3
import pandas as ps

f=open("a.txt",'w')

def change_tx():
    connection = sqlite3.connect("db2.db")
    tx_add_analyser(connection)



def tx_add_analyser(connection):
    read_data = ps.read_sql_query(sql.get_check_tx_add(), connection)
    read_data.sort_values("block_number", inplace=True)
    t1 = [tuple(x) for x in read_data.values]
    t2 = t1[:-1]
    t1_a = t1[::-1]
    t2_a = t2[::-1]
    end = {}
    in_end = {}
    xprev = ''
    key = 1
    res_a = []

    t1_a = t1_a[::-1]
    #t1_a = [('bf4108c758d28d0b1938874b3b4ebb287a9543c8be0958caf3f3bb98351c58ae', '45e6b5b21f26ddd2061f2346e758fda031095a48dad13ed23c66de60422dc79b', 545995), 
    #('94b57ae6600f0e1665f55d1c2d5c5a33628b6c45d7ef235d1914f1239b33996e', '223304e8e70b8fcd6abb53656e31f38a7ae94b0f63580dea4fc0276b36e2418f', 545995), 
    #('223304e8e70b8fcd6abb53656e31f38a7ae94b0f63580dea4fc0276b36e2418f', 'a9aa9b6fd9581bcb55339a980c4d4601dc4984679db372ceba27984632280451, bf4108c758d28d0b1938874b3b4ebb287a9543c8be0958caf3f3bb98351c58ae', 545995), 
    #('45e6b5b21f26ddd2061f2346e758fda031095a48dad13ed23c66de60422dc79b', 'fa96b663ee5ebc2bcb55d2e15521737996d1298f847ce0ac55421ec812624600', 545994), 
    #('6ae7aa9aad11282716ff87285fb3d7b657c56e7ef6dfe235f49931fa22b27e27', '69789eed2ae8b14d394cd390ae740255c66ca0fcb42e9415a8c7edcb2381ecc2', 545978), 
    #('a9aa9b6fd9581bcb55339a980c4d4601dc4984679db372ceba27984632280451', '6ae7aa9aad11282716ff87285fb3d7b657c56e7ef6dfe235f49931fa22b27e27', 545978)]
   


    f.write("%s\n" % str(t1_a))
    t2_a = t1_a[1:]
    rem_res = () 

    while len(t1_a) !=0 or len(t1_a)!=0:
        res_a.append(t1_a[0])
        res = searcher(t2_a, t1_a[0][1])
        
        while True:
            if xprev != res[2]:
                if len(res[0]) != 0:
                    res_a.append(res[0])
                if len(res[1]) != 0:
                    if rem_res == ():
                        rem_res = res[1]
                    else:    
                        rem_res = rem_res +res[1]
                res = searcher(t2_a, res[2])
                xprev = res[2]
            elif xprev == res[2]:
                if len(res[0]) != 0:
                    res_a.append(res[0])
                if len(res[1]) != 0:
                    if rem_res == ():
                        rem_res = res[1]
                    else:    
                        rem_res = rem_res +res[1]
                break
        
        t1_a = t1_a[1:]
        in_end[len(res_a)] = res_a
        end[key] = in_end
        f.write("%s\n" % (str(key)+ " --> "+str(in_end)))
        end.update({key:res_a})
        key = key+1
        for x in rem_res:
            if x in t1_a:
                t1_a.remove(x) 
        for y in rem_res:
            if y in t2_a:
                t2_a.remove(y) 
        rem_res = ()
        res_a = []
        in_end = {}

    print(end)



def searcher(t2, prev):
    a = []
    remover = []
    prev_starter = prev
    axx = splitter(prev_starter)
    for i in axx:
        prev_starter = i
        for j in range(len(t2)):
            if (prev_starter in t2[j][0]):
                a.append(t2[j])
                remover.append(t2[j])
                #t2.remove(t2[j])
                if len(axx) <= 1:
                    prev_starter = t2[j][1]
                else:
                    prev_starter = t2[j][1]
                    axx.append(t2[j][1])
    
                
    return a, remover, prev_starter


def splitter(str_in):
    a = str_in.split(",")
    return a

