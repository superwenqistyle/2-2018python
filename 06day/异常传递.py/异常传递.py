import time
try:
	f=open("card.data","r")
	try:
		while True:
			content=f.readline()
			if len(content) == 0:
				break
			time.sleep(2)
			print(content)
	except Exception as result:
		print(result)
	finally:
		f.close()
		print("文件关闭")
except Exception as result:
	print("异常捕获成功")
