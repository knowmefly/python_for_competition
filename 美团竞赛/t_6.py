#coding:utf-8
import sys
if __name__ == '__main__':
	line = sys.stdin.readline().strip().split()
	a = int(line[0])
	b = int(line[1])
	div = str(a/b)
	zero = '00000000000000000000000000000'
	s = div.split('.')[1] + zero
	k = sys.stdin.readline().strip()

	if k in s:
		for i in range(len(s)):
			if k[0] == s[i] :
				nPos = i+1
				break
		print (nPos)
	else:
		print(-1)
