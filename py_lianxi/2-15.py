print 'Enter three numbers:'  
num1=int(raw_input())  
num2=int(raw_input())  
num3=int(raw_input())  
min=num1  
if min>num2:  
    min=num2  
    if min>num3:  
        print num3,num2,num1  
    elif num1>num3:  
        print num2,num3,num1  
    else:  
        print num2,num1,num3  
elif min>num3:  
    print num3,num1,num2  
elif num3>num2:  
    print num1,num2,num3  
else:  
    print num1,num3,num2  


#or
print 'Enter three numbers:'  
num1=int(raw_input())  
num2=int(raw_input())  
num3=int(raw_input())  
max=num1  
if max<num2:  
    max=num2  
    if max<num3:  
        print num3,num2,num1  
    elif num1<num3:  
        print num2,num3,num1  
    else:  
        print num2,num1,num3  
elif max<num3:  
    print num3,num1,num2  
elif num3<num2:  
    print num1,num2,num3  
else:  
    print num1,num3,num2  