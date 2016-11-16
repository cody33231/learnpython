number = 1
while number == 1:
	a = int(raw_input('put u number:'))
	if a < 0 :
		print "too low"
	elif a > 100 :
		print "too high"
	elif a > 0 and  a < 100:
		break
print "ok"

