from socket import *
udpSocket=socket(AF_INET,SOCK_DGRAM)
sendaddr=("192.168.19.127",8080)
senddata=input("输入要发送的内容")
udpSocket.sendto(senddata.encode("gb2312"),sendaddr)
udpSocket.close()
