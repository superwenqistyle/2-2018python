import os
file_name=input("输入要修改的文件名")
files=os.listdir(file_name)
for temp in files:
	old_name=file_name+"/"+temp
	new_name=file_name+"/"+"super"+temp
	os.rename(old_name,new_name)

