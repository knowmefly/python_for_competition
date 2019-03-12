#coding:utf-8
import sys

if __name__ == "__main__":
	a = sys.stdin.readline().strip().split()
	n = int(a[0])
	m = int(a[1])
    #初始化
	dis = 0
	values = 0
	dic = 0
    #打折优惠
	for i in range(n):
		line = sys.stdin.readline().strip().split()
		if int(line[1])==0:
			dis += int(line[0])
		else:
			dis = dis + int(line[0])*0.8
		values += int(line[0])
		total = dis
    #满减优惠
	for x in range(m):
		line = sys.stdin.readline().strip().split() 
		if int(line[0])<=values:
			dic = values - int(line[1])
            #最少消耗钱数判断
			if dic<=dis and dic<=total:
				total = dic
	print('%.2f' % total)