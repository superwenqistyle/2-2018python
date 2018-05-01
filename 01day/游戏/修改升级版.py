import os
filename=input("输入要修改的文件名")
position=os.getcwd()
files=os.listdir(filename)
os.chdir(position/filename)
for temp in files:
	os.rename(temp,"super"+temp)
