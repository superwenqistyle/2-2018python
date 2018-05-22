#再议服务器
from socket import *

tcp=socket(AF_INET,SOCK_STREAM)
tcp.bind(("",6666))
tcp.listen(5)
while True:
	newsocket,clientaddr=tcp.accept()
	print(clientaddr)
	while True:
		content=newsocket.recv(1024)
		if len(content) > 0:
			print(content.decode("gb2312"))
		else:
			break
		senddate=input("输入要发送的内容")
		newsocket.send(senddate.encode("gb2312"))
		
	newsocket.close()
tcp.close()
