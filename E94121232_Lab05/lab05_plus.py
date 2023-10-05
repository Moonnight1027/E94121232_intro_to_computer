dict0 = {}                          #設定空字典

for i in range(4):                  
    n = input("Enter Keys: ")       #輸入key
    str0 = input("Enter Values: ")  #輸入整行value
    dict0[n] = str0.split(', ')     #用split將字串轉為list，並加入字典
    
print(dict0)                        #將字典印出