# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np			#引入模組

with open('Temperature.txt', 'r') as file:	#讀取資料
	lines = file.readlines()
temp_list = []
for line in lines:
    x = []						#將資料填入名叫temp_list的list
    if line.startswith('T') :
        continue
    data = line.split(', ')
    for i in range(12):
    	x.append(float(data[i+1]))
    temp_list.append(x)

years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021] #建立年分 月份 的資料

Month  = np.array(range(1,13))

for i in range(9):
        plt.plot(Month, temp_list[i], '-', label=years[i]) #畫出折線

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')	#添加標題 xy軸名稱
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(np.arange(1, 13))	#將x軸刻度從1~12完全展示
plt.legend(loc='lower center')	#調整圖例位置
plt.savefig('lab12_01.png')	#儲存圖片
plt.show()			#顯示圖片

month_mean = np.mean(temp_list, axis=0)	#計算月平均和年平均
all_mean = np.mean(temp_list)

plt.scatter(Month, month_mean, color='r')	#輸出點陣圖
plt.plot(Month, month_mean, '-')		#劃出折線
plt.axhline(y=all_mean, color='r', linestyle='--', label='Mean of 9 Years')	#畫出年平均線
for i, txt in enumerate(month_mean):		#加上每個點的數值
	plt.text(Month[i], txt, f'{txt:.2f}'.rstrip('0').rstrip('.'), color='black', ha='left', va='bottom')
plt.text(1, all_mean + 0.15, f'{all_mean:.2f}'.rstrip('0').rstrip('.'), color='black')	#加上年平均的數值

plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')	#增加標題 xy軸標題
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(np.arange(1, 13))	#調整xy軸的刻度
plt.ylim(16, 32)
plt.legend()
plt.savefig('lab12_02.png')
plt.show()

fig = plt.figure(figsize=(15,6))	#建立一個1x2的圖表
fig.add_subplot(1, 2, 1)
plt.subplot(1, 2, 1)			#先畫第一個位置
for i in range(9):
        plt.plot(Month, temp_list[i], '-', label=years[i])

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(np.arange(1, 13))
plt.legend(loc='lower center')

fig.add_subplot(1, 2, 2)		#再畫第二個位置
month_mean = np.mean(temp_list, axis=0)
all_mean = np.mean(temp_list)

plt.scatter(Month, month_mean, color='r')
plt.plot(Month, month_mean, '-')
plt.axhline(y=all_mean, color='r', linestyle='--', label='Mean of 9 Years')

for i, txt in enumerate(month_mean):
        plt.text(Month[i], txt, f'{txt:.2f}'.rstrip('0').rstrip('.'), color='black', ha='left', va='bottom')
plt.text(1, all_mean + 0.15, f'{all_mean:.2f}'.rstrip('0').rstrip('.'), color='black')

plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(np.arange(1, 13))
plt.ylim(16, 32)
plt.legend()

fig.savefig('lab12_03.png')	#儲存並輸出
plt.show()
