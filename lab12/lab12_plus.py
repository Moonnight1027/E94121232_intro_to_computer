# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np			#引入模組

with open('oddExperiment.txt', 'r') as file:	#讀取資料
	lines = file.readlines()
x = []						#將資料填入X Y的list
y = []
for line in lines:
    if line.startswith('y'):
        continue
    data = line.split()
    x.append(int(data[1]))
    y.append(float(data[0]))

plt.scatter(x, y, label='data') #畫出各點

coeff_linear = np.polyfit(x, y, deg=1)	#利用np.polyfit與np.poly1d 找出最符合資料分布的一階多項式及二階多項式
poly_linear = np.poly1d(coeff_linear)

coeff_quadratic = np.polyfit(x, y, deg=2)
poly_quadratic = np.poly1d(coeff_quadratic)

lse_linear = mean_squared_error(y, poly_linear(x))	#計算LSE
lse_quadratic = mean_squared_error(y, poly_quadratic(x))

plt.plot(x, poly_linear(x), label=f'Fit of degree 1, LSE = {lse_linear:.5f}', color='red')
plt.plot(x, poly_quadratic(x), label=f'Fit of degree 2, LSE = {lse_quadratic:.5f}', color='purple')
plt.legend(loc='upper center')		#繪出圖形並加上圖例
plt.title('oddExperiment Data')
plt.savefig('lab12_plus.png')		#儲存圖形
plt.show()				#顯示圖形

