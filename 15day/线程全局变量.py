import threading
import time
list=[11,22,33,44,55,66]
def work():
	list[0]=88
	print("当前线程:%s list=%s"%(threading.current_thread().name,str(list)))
def work1():
	print("当前线程:%s list=%s"%(threading.current_thread().name,str(list)))

t=threading.Thread(target=work)
t.start()

time.sleep(5)

t1=threading.Thread(target=work1)
t1.start()
