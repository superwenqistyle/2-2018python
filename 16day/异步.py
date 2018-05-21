from multiprocessing import Pool
import time
import os

def w1():
	print("执行w1函数")
	print("pid:%d ppid:%d"%(os.getpid(),os.getppid()))
	time.sleep(1)
	return "the life is short, you need python"
def w2(args):
	print("w2开始时执行")
	time.sleep(1)
	print("pid:%d ppid:%d"%(os.getpid(),os.getppid()))

p=Pool()
p.apply_async(func=w1,callback=w2)
p.close()
#time.sleep(4)
print("主进程")
print("pid:%d"%os.getpid())
print("ppid:%d"%os.getppid())
p.join()
#print("pid:%d"%os.getpid())

