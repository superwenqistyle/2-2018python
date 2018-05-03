class animal():
	def __del__(self):
		print("眼光不错")
	
car=animal()
cat=car
del car
print("-------")
del cat
print("-------")
#__del__()作为魔法方法：在所以指向内存操作的键数结束运行后del才运行
