#coding:utf-8
import sys

if __name__ == '__main__':
	line = sys.stdin.readline().strip().split()
	n = int(line[0])
	m = int(line[1])
	k = int(line[2])

	e = 1
	plan = 0
	for i in range(k):
		line = sys.stdin.readline().strip().split()
		mei = int(line[0])
		tuan =int(line[1])
		
		e_a = mei * m + tuan * (n-m)
		if e_a>=e:
			e = e_a
			plan = i

	#输出规划
	initial_value = 0
	buy = [initial_value for i in range(k)]
	buy[plan] = n
	for i in buy:
		print(i, end=" ")