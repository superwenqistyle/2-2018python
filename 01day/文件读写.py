f = open("1.text","w")
content=f.write("The life is short,you need python")
print(content)
f.close()


f = open("1.text","r")
content=f.read()
print(content)
f.close()


f=open("1.text","a")
content=f.write("哈哈,瞬间就没了")
print(content)
#content1=f.read()
#print(content1)
f.close()

