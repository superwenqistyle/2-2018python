from multiprocessing import Pool
import os
def test(i):
	for temp in range(3):
		print("%d第%d次 pid=%d"%(i,temp,os.getpid()))
p=Pool(3)
print("*"*10)
for i in range(10):
	p.apply(test,(i,))
	print("#"*10)
p.close()
print("start.........")
p.join()
print("end..........")
