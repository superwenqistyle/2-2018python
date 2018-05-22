def test1():
	return "1"
def test2():
	return "2"
def test3():
	return "3"
def test4():
	return "4"
def test5():
	return "5"
def unknow():
	return "输入真确的信息"
dic={
	"1":test1,
	"2":test2,
	"3":test3,
	"4":test4,
	"5":test5
}
temp=input("输入1~5之间的数")
k=dic.get(temp,unknow)()
print(k)
