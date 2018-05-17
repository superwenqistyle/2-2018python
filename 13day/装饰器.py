def Bar(py):
	def Dog(fun):
		def wark():
			print("hahah")
			print(py)
			fun()
		return wark
	return Dog
@Bar("k")
def test():
	print("ssssss")
test()
	
