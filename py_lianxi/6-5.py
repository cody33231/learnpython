#-*- coding:utf-8 –*-
def sh_str(str):
	n = len(str)
	list = []	
	if n % 2 == 0:
		for i in range(0,n/2):
			list.append(str[i])
			list.append(str[n-i-1])
	else:
		for i in range(0,int(n/2)+1):
			if i != int(n/2):
				list.append(str[i])
				list.append(str[n-i-1])
			else:
				list.append(str[int(n/2)])
	return list	
	
if __name__ == '__main__':
	string = raw_input('enter:\n')
	print sh_str(string)     #这个地方我很好奇，当这个print去掉以后，运行界面没有结果