def timefun(foo):
	def wrappedfunc(a,b):
		print("%s called at %s"%(func.__name__, ctime()))
		print(a, b)
		func(a, b)
    return wrappedfunc

@timefun
def foo(a, b):
    print(a+b)
