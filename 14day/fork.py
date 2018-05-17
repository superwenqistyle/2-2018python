import os
ret=os.fork()
if ret == 0:
	print("子进程是%d pid=%d ppid=%d"%(ret, os.getpid(), os.getppid()))
else:
	print("父进程是%d pid=%d ppid=%d"%(ret, os.getpid(), os.getppid()))
