#-*- coding:utf-8 –*-
#1
'''y = float(raw_input('please input dollors:'))
if y >= 1:
	print 'too high'
else:
	y = y * 100 #1美分个数
   	a = y // 25  #25美分个数
   	b = (y - a*25) // 10 # 10美分个数
   	c = (y - a *25 - b * 10) // 5  #5美分个数
   	d = y - a*25 - b*10 - c*5  #除去
   	s = a + b + c + d
   	print "%d" % (s)'''
#2
'''n = float(raw_input("input dollors:"))  
while n >= 0:
	break
def money(num):  
    num = num *100  
    a = num // 25  
    b = (num - a *25)//10  
    c = (num - a* 25 - b *10) //5  
    d = (num -a * 25 - b * 10 - c * 5)  
    return a+b+c+d  

print money(n)'''  
#3
'''dollar = float(raw_input("Input the money that less than 1 dollar:"))
if dollar >= 1:
    print "money is too large."
elif 0 < dollar < 1:
    temp = int(dollar * 100)
    (N25, temp) = divmod(temp, 25)
    print "%d 25 coins." %N25
    (N10, temp) = divmod(temp, 10)
    print "%d 10 coins." %N10
    (N5, temp) = divmod(temp, 5)
    print "%d 5 coins." %N5
    (N1, temp) = divmod(temp, 1)
    print "%d 1 coins." %N1
else:
    print "You must input larger than 0."
except ValueError, e:
    print "You must input a digits."'''