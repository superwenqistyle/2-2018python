class animal():
	def __init__(self):
		self.__feature=100
		print("特点有%d"%self.__feature)
	def getfeature(self,feature):
		return "特点有%d"%self.__feature
	def shot(self,hero):
		print("%s比巴雷特太强大"%hero)
	def __skills(self,skill):
		self.skill=skill
		return "技能有%d"%self.skill
	def publicskills(self,skill):
		return self.__skills(skill)
class rover(animal):
	pass

land_rover=rover()	
land_rover.shot("超人")
#land_rover.__skills(9999)
#land_rover.publicskills(9999)
print(land_rover.publicskills(9999))
