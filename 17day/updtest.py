from socket import *
from threading import Thread
from time import ctime

Id=""
port=0
updSocket=None

def send():
	while True:
		message=input("请输入内容:")
		updSocket.sendto(message.encode("gb2312"),(Id,port))

def receive():
	while True:
		content=updSocket.recvfrom(1024)
		print("%s-%s\n请输入内容:"%(content[0].decode("gb2312"),content[1][0]),end="")	
	
def main():
	global Id
	global port
	global updSocket
	Id = input("输入对方的id:")
	port = int(input("输入对方的端口号:"))
	updSocket = socket(AF_INET,SOCK_DGRAM)
	updSocket.bind(("",6666))
	t = Thread(target=send)
	t1 = Thread(target=receive)
	t.start()
	t1.start()
	t.join()
	t1.join()

if __name__ == "__main__":
	main()	



