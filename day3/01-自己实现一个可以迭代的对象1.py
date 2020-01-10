from collections import Iterable,Iterator
class Classmate(object):
	def __init__(self):
		self.names = list()
	
	def add(self,name):
		self.names.append(name)
	
	def __iter__(self):
		"""如果想要一个对象成为一个可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
		return ClassIterator()
class ClassIterator(object):
	def __iter__(self):
		pass
	
	def __next__(self):
		pass

classmate = Classmate()

classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

#print("判断classmate是否是可以迭代的对象：",isinstance(classmate,Iterable))
#classmate_iterator = iter(classmate)
#print("判断classmate_iterator是否是迭代器：",isinstance(classmate_iterator,Iterator))

for name in classmate:
	print(name)
