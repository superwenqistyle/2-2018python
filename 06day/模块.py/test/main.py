from message import *
try:
	test1()
	#test2()
	#test3()

except Exception as result:
	print("异常捕获")
else:
	print("运行正常")
finally:
	print("运行结束")
