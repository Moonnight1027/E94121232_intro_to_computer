#coding=utf-8
import random					#添加random模組
from flask import *				#引入函式庫中所有函式
app = Flask(__name__)				#建立Flask物件

@app.route('/',methods=['GET'])			#設定根目錄之路由
def index():
	return render_template('lab10.html')	#打開html檔

@app.route('/student_data',methods=['POST'])	#設定要讓表單填完後要切換過來的路由
def result():
	name = request.form['name']		#在終端顯示從表單輸入的結果
	student_id = request.form['student_id']
	print('')
	print(f'name : {name}')	
	print(f'student_id : {student_id}')
	print('')
	return 'ok'				#回傳給前端ok

@app.route('/rsp',methods=['GET'])				#設定用於猜拳的路由
def mora():
	choice = request.args.get('choice',default= " ")	#使用者出的拳
	AI = ['r', 's', 'p',]					#由random隨機生成電腦出拳
	choice_AI = random.choice(AI)
	if choice != 'r' and choice != 's' and choice != 'p':	#判斷有沒有輸錯
		return 'Wrong input ! try again'
	print('')						#顯示雙方出拳
	print(f'computer : {choice_AI}  user : {choice}')
	print('')
	if choice == 'r' and choice_AI == 's':			#判斷勝負並回傳結果給前端
		return 'You win!'
	elif choice == 's' and choice_AI == 'p':
		return 'You win!'
	elif choice == 'p' and choice_AI == 'r':
		return 'You win!'
	elif choice == 'r' and choice_AI == 'p':
		return 'You lose!'
	elif choice == 's' and choice_AI == 'r':
		return 'You lose!'
	elif choice == 'p' and choice_AI == 's':
		return 'You lose!'
	else:
		return "It's Tie!"
app.run(host="0.0.0.0", port=3000, debug=True)			#設定debug模式 PORT3000
