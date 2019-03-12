#coding:utf-8
import sys
import numpy as np

if __name__ == '__main__':
	line = sys.stdin.readline().strip().split()
	n = int(line[0])
	m = int(line[1])
	reco = int(line[2])
	t = '' 
	arr = np.zeros((n,m),dtype=int)


	for i in range(reco):
		re_n = sys.stdin.readline().strip().split() 
		
		i = int(re_n[0])
		j = int(re_n[1])
		z = int(re_n[2])
 
		#arr[i][j] = 1
		if z==0 :
			arr[i-1][j-1] = 1

	# print(arr)
	for i in arr:
		print(*i)