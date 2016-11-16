#1
a = int(raw_input('input U number:'))

if a >= 90 and a <= 100:
	print 'a'
elif a >= 80 and a <= 89:
	print 'b'
elif a >= 70 and a <= 79:
	print 'c'
elif a >= 60 and a <= 69:
	print 'd'
elif a < 60:
	print 'f'
else:
	print 'number error'


#2
 x = input("plz input your score:")
    if x >= 60:
        if x >= 70:
            if x >= 80 :
                if x >= 90:
                    if x >= 100:
                        print "Ａ"
                    else:
                        print "Ｂ"
                else:
                    print "Ｃ"
            else:
                print "Ｄ"
        else:
            print "Ｅ"
    else:
        print "Ｆ"

#3
def grade(num):
        if 90 <= num <= 100:
            print 'A'
        elif 80 <= num <= 89:
            print 'B'
        elif 70 <= num <= 79:
            print 'C'
        elif 60 <= num <= 69:
            print 'D'
        elif 0 <= num <= 59:
            print 'F'
        else:
            print " The num is invalid."

     try:
            num = int(raw_input("Input a num:"))
            grade(num)
     except ValueError, e:
            print "You must input digits."