class Father(object):
	def __init__(self):
		self.skills=3
	def	python(self):
		print("The life is short,wo need python")
	def str(self):
		#return "我会%d种技能"%self.skills
		self.python()
		Father.python(self)
		super().python()
		#object.python()
	
		
son=Father()
son.python()
#Father.python(self)
#print(son)
son.str()
