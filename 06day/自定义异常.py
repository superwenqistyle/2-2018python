class ShowError(Exception):
	def __init__(self,length,atleast):
		self.length=length
		self.atleast=atleast
def main():
	try:
		str=input("请输入")
		if len(str)<3:
			raise ShowError(len(str),3)
	except ShowError as result:
		print("输入的长度是%d位,需要的额长度是%d位"%(result.length,result.atleast))
		print("抓住异常")
main()
