f=open("test","r")
content=f.read(3)
print(content)
position=f.tell()
print(position)
f.seek(3,0)
content=f.read()
print(content)
f.close()


