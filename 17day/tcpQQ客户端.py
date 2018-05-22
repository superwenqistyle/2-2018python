from socket import *

tcp=socket(AF_INET,SOCK_STREAM)
sendaddr=("192.168.19.127",6666)
tcp.connect(sendaddr)
while True:
	senddate=input("输入发送内容")
	
	if len(senddate) > 0:
		tcp.send(senddate.encode("gb2312"))
	else:
		break
	content=tcp.recv(1024)
	print(content.decode("gb2312"))
tcp.close()
