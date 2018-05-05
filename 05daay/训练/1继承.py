class Father():
	def __init__(self):
		self.property=3
	def __str__(self):
		return "有%d种特长"%(self.property)
	def python(self):
		print("我是python全栈工程师")
class Mother():
	def __init__(self):
		self.skills=3
	def __str__(self):
		return "我会%d种专业技能"%self.skills
	def sing(self):
		print("我会唱歌")

class Son(Father,Mother):
	def program(self):
		print("我对编程感兴趣")
	def python(self):
		print("我会python和java")
xiaoming=Son()
xiaoming.python()
xiaoming.sing()
xiaoming.program()
print(xiaoming)
