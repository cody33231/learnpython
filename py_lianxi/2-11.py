print '\n choose 1 to calculate the five number;\n choose 2 to calculate the average of the five number;\n choose 3 to quit the program'  
while True:  
    total=0  #
    flag=int(raw_input('Enter your choice:'))  
    if flag==1:  
        num=[int(raw_input('Enter the first number:')),int(raw_input('Enter the second number:')),int(raw_input('Enter the third number:')),int(raw_input('Enter the forth number:')),int(raw_input('Enter the fifth number:'))]  
        for x in num:  
            total+=x  
        print total  
        break
    if flag==2:  
        num=[int(raw_input('Enter the first number:')),int(raw_input('Enter the second number:')),int(raw_input('Enter the third number:')),int(raw_input('Enter the forth number:')),int(raw_input('Enter the fifth number:'))]  
        for x in num:  
            total+=x  
        print float(total/5)  
        break
    if flag==3:  
        break  
    else:  
        print 'Your have enter the wrong number,please try again'  