import os
name=input("输入修改的文件名:")
files=os.listdir(name)
os.chdir(name)
for temp in files:
	os.rename(temp,"精品"+temp)
