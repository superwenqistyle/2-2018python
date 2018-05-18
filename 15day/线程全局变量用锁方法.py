import threading 
from threading import Thread,Lock
import time

num=0
def w1():
	global num
	#mutex.acquire()
	for temp in range(1000000):
		num += 1
	print("进程:%s num:%d"%(threading.current_thread().name,num))
	#mutex.release()
def w2():
	global num
	#mutex.acquire()
	for temp in range(1000000):
		num += 1
	print("进程:%s num:%d"%(threading.current_thread().name,num))
	#mutex.release()
mutex=threading.Lock()
t1 = threading.Thread(target=w1)
t1.start()
#time.sleep(2)
t1.join()

t2 = threading.Thread(target=w2)
t2.start()
