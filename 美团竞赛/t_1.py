#coding:utf-8
import sys
if __name__ == '__main__':
	line = sys.stdin.readline().strip().split()
	T = int(line[0]) 
	list1 = ['A','B','C','G','H','I']
	list2 = ['D','E','F','J','K','L','P','Q','R','S']
	list3 = ['M','N','O','T','U','V']
	list4 = ['W','X','Y','Z']
	for i in range(T):
		n = 0
		movie = sys.stdin.readline().strip()
		for let in movie:
			if let in list1:
				n_1 = 1
			elif let in list2:
				n_1 = 2
			elif let in list3:
				n_1 = 3
			elif let in list4:
				n_1 =4
				
	print(n_1+n)