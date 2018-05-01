import os
name=input("输入要修改的文件夹名字")
f_ile=os.listdir(name)
os.chdir(name)
for temp in f_ile:
	position=temp.rfind(".")
	newname1=input("输入新的前缀")
	os.rename(temp[:position],newname1)
	
