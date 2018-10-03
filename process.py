from threading import Thread 
import main

e = 321000
r = 2000

for i in range(10):
    s = e 
    e = e + r 
    Thread(target=main.thread_fun, args=(s, e )).start()
