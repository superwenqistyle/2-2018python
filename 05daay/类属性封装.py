class Datetest():
	def __init__(self,year,month,day):
		self.year=year
		self.month=month
		self.day=day
	def output(self):
		print("%s年%s月%s日"%(self.year,self.month,self.day))
	@classmethod
	def handledate(cls,date):
		a,b,c=date.split("-")
		return Datetest(a,b,c)
Datetest.handledate("2018-07-08").output()
