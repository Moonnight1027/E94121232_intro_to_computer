def gcd(a,b):                                   #將gcd 與gcd1組合 gcd負責輸出結果 gcd1負責求出最大公因數 gcd以gcd1算出之結果進行輸出
    if gcd1(a, b) == 1:
        print(f"{a}和{b}互質")
        return 1
    elif gcd1(a, b) != 0 and gcd1(a, b) > 1:
        print(f"{a}和{b}的gcd={gcd1(a, b)}")
    else:
        print("0沒有gcd")
        
def gcd1(a, b):                                 #設立以遞迴求出最大公因數之函式gcd1
    GCD = 0
    if a == 0 or b == 0:                        #當 a或b =0 沒有最大公因數
        return GCD
    elif a % b == 0:                            #上面三個為終止條件
        GCD = b
        return GCD
    elif b % a == 0:
        GCD = a
        return GCD
    elif a > b:                                 #下面兩個繼續遞迴
        return gcd1(a % b, b)
    else:
        return gcd1(a, b % a)
    
ans1 = gcd(80, 20)                              
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)
