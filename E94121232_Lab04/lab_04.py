list = []                                       #設定參數
chinese = 0
math = 0
english = 0
average = 0

student = ('A','B','C')
for n in student:                               #輸入參數
    print(f"輸入{n}學生的成績")
    
    chinese = int(input(f"請輸入{n}學生的國文成績:"))               
    math = int(input(f"請輸入{n}學生的數學成績:"))
    english = int(input(f"請輸入{n}學生的英文成績:"))
    average = (chinese + math + english)/3
    average = round(average,1)                  #取平均值至小數點後第1位
    
    list.append(f'{n}')                         #將參數加入list
    list.append(chinese)
    list.append(math)
    list.append(english)
    list.append(average)
    
    print(f"國文:{chinese}")                    #輸出分數
    print(f"數學:{math}")
    print(f"英文:{english}")
    
print(list[0:5])                                #輸出結果
print(list[5:10])
print(list[10:15])