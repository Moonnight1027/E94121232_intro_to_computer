val = 0                                                 #設定參數
len_nums = 0

nums = input("請輸入一個數字串:")                       #輸入字串
val = (input("請輸入欲刪除之數字:"))
print(f"輸入的list為:{nums}，欲刪除之數字為:{val}")     
print("\n")
print("刪除後!")
print("\n")

nums = nums.strip(']')                                  #將string轉換為list
nums = nums.strip('[')
nums = nums.split(', ')

while True :                                            #利用while迴圈將欲刪除之數字刪除
    if val in nums:
        nums.remove(f'{val}')
    else:
        break
    
len_nums = len(nums)                                    
nums = '[' + ', '.join(nums) + ']'
print(f"list長度剩下:{len_nums}，list變成:{nums}")      #輸出剩餘長度/list
