from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 准备接收方的地址
sendAddr = ('192.168.56.1', 8080)

#3. 从键盘获取数据
sendData = input("请输入要发送的数据:")

#4. 发送数据到指定的电脑上
udpSocket.sendto(sendData.encode("gb2312"), sendAddr)

#5. 关闭套接字
udpSocket.close()
