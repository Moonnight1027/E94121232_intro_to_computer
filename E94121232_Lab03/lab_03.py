number = input("please input a number :") 
number = int(number)                      
if number % 2 == 1:                       
    print("this is odd")
else:
    print("this is even")
    
E = input("please input your student ID first character :")
N = input("please input your student last 8 numbers :")
N = int(N)                                
if N % 2 == 1:                            
    print("your student ID number is odd")
else:
    print("your student ID number is even")
    
E = str(E)                                
N = str(N)
print("your student ID is :"+E+N)        