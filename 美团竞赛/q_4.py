#coding:utf-8
import sys

if __name__ == '__main__':
	line = sys.stdin.readline().strip()
	r = int(line)
	s = sys.stdin.readline().strip().split()
	x1 = float(s[0])
	y1 = float(s[1])
	m = sys.stdin.readline().strip().split()
	x = float(m[0])
	y = float(m[1])

	dis = (x-x1)**2 + (y-y1)**2

	print(dis)