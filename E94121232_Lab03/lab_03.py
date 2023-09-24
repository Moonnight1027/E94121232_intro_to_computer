number = input("please input a number :") #輸入數字
number = int(number)                      #將資料型態改為整數
if number % 2 == 1:                       #除2餘1為奇數 其它為偶數
    print("this is odd")
else:
    print("this is even")
    
E = input("please input your student ID first character :")
N = input("please input your student last 8 numbers :")
N = int(N)                                #將資料型態改為整數
if N % 2 == 1:                            #除2餘1為奇數 其它為偶數
    print("your student ID number is odd")
else:
    print("your student ID number is even")
    
E = str(E)                                #將資料型態改為字串
N = str(N)
print("your student ID is :"+E+N)         #輸出學號