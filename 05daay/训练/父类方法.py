class Father(object):
	instance=8
	def __new__(cls):
		print("要返回了...")
		return object.__new__(cls)
		print("第一次返回")
		return super().__new__(cls)
		print("第二次返回")
	def __init__(self):
		self.skills=6
		print("father的方法")
	def __str__(self):
		return "我会的技能有%d种"%self.skills
	def __del__(self):
		print("del功能要执行了.....")
	@classmethod
	def song(cls):
		print("唱歌")
	@staticmethod
	def directory():
		print("打印目录")
class Son(Father):
	def __init__(self):
		super().__init__()
		Father.__init__(self)
	def operate(self):
		print("我的操作猛如虎")
xiaoming=Son()
print(id(xiaoming))


