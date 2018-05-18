import threading,time
def sing():
	print("正在唱歌")
	time.sleep(1)
def dance():
	print("正在跳舞")
	time.sleep(1)
if __name__ == "__main__":
	for temp in range(5):
		t1=threading.Thread(target=sing)
		t2=threading.Thread(target=dance)
		t1.start()
		t2.start()

