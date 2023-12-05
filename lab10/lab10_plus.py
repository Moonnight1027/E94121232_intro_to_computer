#coding=utf-8
import random                                   #添加random模組
from flask import *                             #引入函式庫中所有函式
import json					#添加 json模組
app = Flask(__name__)                           #建立Flask物件
dict0 = {}					#建立用於儲存資料的字典

@app.route('/',methods=['GET'])                 #設定根目錄之路由
def index():
        return render_template('lab10_plus.html')    #打開html檔

@app.route('/set',methods=['POST'])    		#設定要讓表單填完後要切換過來的路由
def result():
	store_name = request.form['store_name']  #將輸入進來的資料存進字典
	score = request.form['score']
	dict0[store_name] = score
	print('')
	print(f"user input data : {{'store_name': '{store_name}', 'score': '{score}'}}")	#將輸入結果於終端顯示
	print('')
	print(f'Data on server : {dict0}')
	print('')
	dict0_string = json.dumps(dict0, ensure_ascii=False)					#將自短典內容轉換為字串
	return render_template('lab10_plus.html', dict0_string = dict0_string)    		#將字串回傳給前端進行顯示

@app.route('/reset/<choice>',methods=['GET'])                              			#設定用於reset的路由
def reset(choice):
	if choice == 'y':
		dict0.clear()									#選擇y時清空字典
		print('')
		print(f'Data on server : {dict0}')						#顯示空字典證明已清空
		print('')
		return render_template('reset.html')    					#顯示reset頁面
	else:
		return render_template('lab10_plus.html')    					#輸入其他的字元則甚麼都不做
app.run(host="0.0.0.0", port=3000, debug=True)							#設定debug模式 PORT3000
