import time
import threading
g_num=0
def test1(num):
	global g_num
	#上锁
	for i in range(num):
	
		mutex.acquire()
		g_num += 1
		mutex.release()
	print("---in test1 g_num=%d---" % g_num)

def test2(num):
	global g_num
	for i in range(num):
	
		mutex.acquire()
		g_num += 1
		mutex.release()
	print("---in test2 g_num=%d---"% g_num)
#创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()
def main():
	#target指定这个线程去哪个函数执行代码
	#args传递参数过去
	t1 = threading.Thread(target=test1,args=(1000000,))
	t2 = threading.Thread(target=test2,args=(1000000,))
	t1.start()
	t2.start()
	time.sleep(5)
	print("---in main Thread g_num=%d---"% g_num)

if __name__=="__main__":
	main()
