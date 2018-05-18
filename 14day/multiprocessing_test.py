:x
import time
import os
def test(agrs):
	for temp in range(5):
		time.sleep(1)
		print("子进程是:%s ppid=%d pid=%d"%(agrs,os.getppid(),os.getpid()))
p = Process(target=test,args=("python",))
p.start()

p.join(3)
print("不等你了")
