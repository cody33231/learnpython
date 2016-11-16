#-*- coding:utf-8 –*-
def change(f):  
    return (f-32)*(5.0/9.0)  
if __name__=='__main__':  
    ss = input("请输入华氏温度：")  
    print change(ss)