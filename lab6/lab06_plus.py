def function(str0):
    list0 = []                              #建立1個放全部組合的list
    if len(str0) == 0:                      #終止條件
        return ['']
    for i in range(0, len(str0)):
        a = str0[i]                         #按順序提取其中一個數字，其他數字排列完後跟原先提取數字組合，再提取下一位數字
        b = str0[0 : i] + str0[i+1 : ]      #剩餘字串丟回函式遞迴，b為去除第i個數後剩下的數字串
        for j in function(b):
            list0.append(a + j)
    return list0

str = input()
print(function(str))