class Calculator(object):
	def __init__(self,num1=0,num2=0):
		#self.num1=num1
		#self.num2=num2
		self.num1=int(input("输入第一的数:"))
		self.num2=int(input("输入第二个数:"))
	def result(self):
		pass	
class Add(Calculator):
	def	result(self):
		return self.num1+self.num2
class Minus(Calculator):
	def result(self):
		return self.num1-self.num2
class Multiply(Calculator):
	def result(self):
		return self.num1*self.num2
class Divide(Calculator):
	def result(self):
		if num2 != 0:
			return self.num1/self.num2
class Oop():
	def init(self):
		while True:
			symbol=input("请输入要计算的符号:")
			if symbol == "+":
				return Add()
			elif symbol == "-":
				return Minus()
			elif symbol == "*":
				return Multiply()
			elif symbol == "/":
				return Divide()
		#	print(f)
		#	print(self.result())
while True:
	project=Oop()
#xiao=project.init("+")
#xiao.num1=1
#xiao.num2=2
#print(xiao.result())
#print(project)
	xiao=project.init()
	print(xiao.result())

		
	
