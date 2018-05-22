from socket import *

tcpSocket=socket(AF_INET,SOCK_STREAM)
tcpSocket.bind(("",6666))
tcpSocket.listen(5)
newSocket,addr=tcpSocket.accept()
print(addr)
while True:
	content=newSocket.recv(1024)
	print(content.decode("gb2312"))
newSocket.close()
tcpSocket.close()

