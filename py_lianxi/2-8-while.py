'''subtot = 0
for i in range(5):
	subtot += int(raw_input('enter a number: '))
print subtot'''
#or
# uses sum() BIF and generator expressions
print sum(int(raw_input('enter a number: ')) for i in range(5))