length1 = input("請輸入第一個邊長")  
length2 = input("請輸入第二個邊長")
length3 = input("請輸入第三個邊長")
length1 = int(length1)  
length2 = int(length2)
length3 = int(length3)

if length1 <= 0 or length2 == 0 or length3 == 0: 
    print("這三個邊長不能構成一個合法的三角形")
elif length1+length2<=length3 or length1+length2<=length3 or length1+length2<=length3:   
    print("這三個邊長不能構成一個合法的三角形")
elif length1-length2>=length3 or length2-length1>=length3 or length2-length3>=length1:   
    print("這三個邊長不能構成一個合法的三角形")
elif length3-length2>=length1 or length3-length1>=length2 or length1-length3>=length2:
    print("這三個邊長不能構成一個合法的三角形")
elif length1 == length2 or length2 == length3 or length3 == length2: 
    if length1 == length2 == length3:
        print("這是一個正三角形")     
    else:
        print("這是一個等腰三角形")
else :
    print("這是一個一般三角形")