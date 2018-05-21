import threading 
import time

def w1():
	num = 1
	if threading.current_thread().name == "Thread-1":
		num += 1
		time.sleep(1)
		print("num1:%d"%num)
	else:
		print("num2:%d"%num)

t=threading.Thread(target=w1)
t.start()
t1=threading.Thread(target=w1)
t1.start()

