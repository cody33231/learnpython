#-*- coding:utf-8 –*-
#1
'''a = int(raw_input('put zhe frist number:'))
b = int(raw_input('put zhe second number:'))

if a % b == 0:
	print 'true'
else:
	a % b != 0
	print 'flase'''

#2

def num(num1,num2):  
	if (num1%num2==0) or (num2%num1==0):  
		return True  
	else:  
		return False  
num1 = input("请输入第一个数：")  
num2 = input("请输入第二个数：")  
print num(num1,num2)