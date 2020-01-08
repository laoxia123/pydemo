import multiprocessing

def download_from_web(q):
	data = [11,22,33,44]
	for temp in data:
		q.put(temp)
def analysis_data(q):
	"""数据处理"""
	waitting_analysis_data = list()
	while True:
		data = q.get()
		waitting_analysis_data.append(data)
		if q.empty():
			break
	print(waitting_analysis_data)
def main():
	#1.创建一个队列
	q=multiprocessing.Queue()	
	#2.创建多个进程，将队列的引用当做实参进行传递到里面
	p1=multiprocessing.Process(target=download_from_web,args=(q,))
	p2=multiprocessing.Process(target  =  analysis_data,args=(q,))
	p1.start()
	p2.start()

if __name__=="__main__":
	main()
