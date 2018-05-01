class SweetPotato():
	def __init__(self):
		self.cooklevel=0  #默认"生的"
		self.cookstr="生的"
		self.condiments=[]
	def __str__(self):
		return self.cookstr+str(self.condiments)
	def cooktime(self,time):
		self.cooklevel+=time
		if self.cooklevel > 0 and self.cooklevel <= 3:
			self.cookstr="半生不熟"
		elif self.cooklevel > 3 and self.cooklevel <= 6:
			self.cookstr="熟了"
		else:
			self.cookstr="糊了"
	def condiment(self,shicai):
		self.condiments.append(shicai)
		
		
digua=SweetPotato()
digua.cooktime(1)
digua.condiment("盐")
print(digua)

digua.cooktime(2)
digua.condiment("芥末")
print(digua)

digua.cooktime(1)
digua.condiment("辣椒")
print(digua)




