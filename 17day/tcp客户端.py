from socket import *

tcpSocket=socket(AF_INET,SOCK_STREAM)
sendaddr=("192.168.1.111",6688)
print("***1****")
tcpSocket.connect(sendaddr)
print("****2***")
while True:
	senddate=input("输入发送的数据")
	tcpSocket.send(senddate.encode("gb2312"))
	recvdate=tcpSocket.recv(1024)
	print(recvdate.decode("gb2312"))
tcpSocket.close()
