class Dog():
	def __init__(self):
		pass
	def __del__(self):
		print("数据正在清空....")
hashiqi=Dog()
zhangao=hashiqi
del hashiqi
#print("哈士奇好惨")
#del zhangao
print("藏獒好惨")
