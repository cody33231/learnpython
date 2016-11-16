#1
'''def test(a,s,b):  
    if s == '+':  
        return a+b  
    elif s == '-':  
        return a-b  
    elif s == '*':  
        return a*b  
    elif s == '/':  
        return a // b  
    elif s == '%':  
        return a%b  
    elif s == '**':  
        return a**b  
    else:  
        return 0  
if __name__=='__main__':  
    ss = raw_input("input your expression:")  
    if len(ss) == 3:  
        print test(float(ss[0]),ss[1],float(ss[2]))  
    else:  
        print test(float(ss[0]),ss[1:3],float(ss[3])) '''
#2
print "Enter the expression"
expression = raw_input('>')

if len(expression.split('+')) == 2:
    try:
        splitExpression = expression.split('+')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m + n
    except ValueError, e:
        print "Input ValueError !"

elif len(expression.split('-')) == 2:
    try:
        splitExpression = expression.split('+')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m - n
    except ValueError, e:
        print "Input ValueError !"

elif len(expression.split('*')) == 2:
    try:
        splitExpression = expression.split('*')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m * n
    except ValueError, e:
        print "Input ValueError !"

elif len(expression.split('/')) == 2:
    try:
        splitExpression = expression.split('/')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m / n
    except ValueError, e:
        print "Input ValueError !"

elif len(expression.split('%')) == 2:
    try:
        splitExpression = expression.split('%')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m % n
    except ValueError, e:
        print "Input ValueError !"

elif len(expression.split('**')) == 2:
    try:
        splitExpression = expression.split('**')
        m = float(splitExpression[0])
        n = float(splitExpression[1])
        print m ** n
    except ValueError, e:
        print "Input ValueError !"

else:
        print "Input Error !"
