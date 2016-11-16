#-*- coding:utf-8 –*-
test_list = []
while True:
	n = int(raw_input("请输入一些数字，输入0时结束:"))
	if n == 0:
		break
	test_list.append(n)
test_list.sort(reverse=False)
print test_list


#reverse=True 降序
#reverse=false 升序

#b

'''list2 = []
while  True:
	num = int(raw_input('Please input numbers, end with 0:'))
	if num == 0:
		break
	else:
		list2.append(num)
list2.sort()
print list2'''

