#-*- coding:utf-8 –*-
import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print "Welcome to the Identifier Checker V1.0"
print "Pls input the test string"
myInput = raw_input("Identifier to test?\n")
if myInput in keyword.kwlist:
    print "Invalid : The string is keyword"
else:
    if myInput[0] not in alphas:
        print "The string is Not Valid, the first symbol must be letters or '_' "
    else:
        for otherchar in myInput[1:]:
            if otherchar not in alphas + nums:
                print "Invalid: 其余字符串必须是字母、数字或者下划线"
                break
            else:
                print "The test string is Valid"