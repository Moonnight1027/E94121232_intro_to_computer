index = ['國文','英文','數學','自然','社會']                            #設定list
stuA = [50, 60, 70, 80, 90]
stuB = [57, 86, 73, 82, 43]
stuC = [97, 96, 86, 97, 83]
dict0 = {"index" : index, "stuA" : stuA, "stuB" : stuB, "stuC" : stuC}

averageA = 0                                                            #設定參數
averageB = 0
averageC = 0

chinese = 0
english = 0
math = 0
science = 0
society = 0

for i in range(5):                                                      #利用for迴圈計算各生平均成績
    averageA = averageA + dict0["stuA"][i]
    averageB = averageB + dict0["stuB"][i]
    averageC = averageC + dict0["stuC"][i]
averageA = averageA/5
averageB = averageB/5
averageC = averageC/5

chinese = (stuA[0] + stuB[0] + stuC[0])/3                               #計算各科平均成績
english = (stuA[1] + stuB[1] + stuC[1])/3
math = (stuA[2] + stuB[2] + stuC[2])/3
science = (stuA[3] + stuB[3] + stuC[3])/3
society = (stuA[4] + stuB[4] + stuC[4])/3

    
print(f"A學生平均成績 : {averageA}")                                    #輸出結果
print(f"B學生平均成績 : {averageB}")
print(f"C學生平均成績 : {averageC}")
print()
print(f"國文平均成績 : {chinese}")
print(f"英文平均成績 : {english}")
print(f"數學平均成績 : {math}")
print(f"自然平均成績 : {science}")
print(f"社會平均成績 : {society}")
print()
print(f"dict0 = {dict0}")