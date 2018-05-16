def fig(fun):
	def bibao(*args,**kwargs):
		print("hahha")
		print(*args)
		print(**kwargs)
		ret=fun(*args,**kwargs)
		return ret
	return bibao
@fig
def test(a,b):
	print("xixi")
	resolution=a+b
	return resolution
test(1,2)
print(test(1,2))	
	
