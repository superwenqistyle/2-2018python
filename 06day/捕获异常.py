try:
	print("开始执行:",center(10,"*"))
	print(num)
except SyntaxError:
	print("出错了")
except Exception as result:
	print("错误类型是:%s"%result)
finally:
	print("*"*10)
