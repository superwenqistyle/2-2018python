oldfile_name=input("输入要备份的文件名:")
old_file=open(oldfile_name,"r")
position=oldfile_name.rfind(".")
newfile_name=oldfile_name[:position]+"备份"+oldfile_name[position:]
new_file=open(newfile_name,"w")
while True:
	content=old_file.read(1)
	if len(content) == 0:
		break
	new_file.write(content)
old_file.close()
new_file.close()
