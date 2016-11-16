s = raw_input('enter a string: ')
'''for eachChar in s:
	print eachChar # (does not print index)
#or'''
for i in range(len(s)):
	print i, s[i]
#or
'''i = 0
slen = len(s)
while i < slen:
print i, s[i]
#or
for i, x in enumerate(s):
print i, x'''