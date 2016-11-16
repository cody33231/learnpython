def time(h,m):
	min = h * 60 + m 
	return min
while True:
		h = input("put h:")
		m = input("put m:")
		if h > 0 and m > 0:  #(h < 23 and h > 1) and(m < 60 and m > -1):
			print 'The time is %d minuters' % time(h,m)  
		else:
			print 'input error'			


















