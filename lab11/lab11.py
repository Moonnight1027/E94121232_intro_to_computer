# 客語沉浸式教學計畫
# https://data.gov.tw/dataset/162621

import pymysql.cursors
import requests
import json

test = requests.get("https://cloud.hakka.gov.tw/Pub/Opendata/DTST20230500090.json")	#從選定資料集的 API 端點獲取資料
r = json.loads(test.text)								#解析 JSON 響應，獲取一個 Python 數據結構

try:
    connection = pymysql.connect(host='localhost',  					#伺服器/主機
                                 user='E94121232',       				#資料庫的帳號
                                 password='0000', 					#資料庫的密碼
                                 database='wordpress',     				#資料庫的名稱
                                 cursorclass=pymysql.cursors.DictCursor)
    print("連線成功")     
except Exception as error: 								#當錯誤產生時進行處理
    print(error)


with connection:
    with connection.cursor() as cursor:

        sql = "INSERT INTO `客語沉浸式教學計畫` (`YYYROC`, `county`, `township`, `school_name`) VALUES (%s, %s, %s, %s)"	#使用 PyMySQL 執行這些 INSERT 查詢，將獲取的資料填充到 MySQL 資料表中
        for i in range( len( r ) ):
            cursor.execute(sql, (r[i]['YYYROC'],r[i]['county'],r[i]['township'],r[i]['school_name']))

    connection.commit()
    cursor.close()
