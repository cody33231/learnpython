#-*- coding:utf-8 –*-
'''years = int(raw_input('input years'))

if years % 4 == 0 and years % 100 != 0:
	print 'yes'
elif
	years % 400 == 0'''



'''year = int(raw_input("plear input year:"))
	
if year % 400 == 0:
	print "This is a leap year!"
elif year % 4 == 0 and year % 100 != 0:
	print "This is a leap year!"
else:
	print "This is not a leap year."'''


x = input("plz input year:")
if x % 4 == 0 and x % 100 != 0:
    print " %d 是闰年" % (x)
elif x % 400 == 0:
	print " %d 是闰年" % (x)
else:
	print " %d 不是闰年" % (x)