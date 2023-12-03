# _*_ coding: utf-8 _*_ 
import socket

HOST = '192.168.137.234'					#建立socket
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
	print('Waiting for connection...')			
	a = 0							#設定參數
	b = 1
	c = 0
	conn, addr = s.accept()
	print(f'Add connection from {str(addr)}')

	n = conn.recv(1024).decode()				#設定n為從客戶端得到並解碼的結果
	if n == 'exit':
		print(f'Received from {str(addr)}: {n}')	#客戶端輸入exit時跳出迴圈中斷連線
		break
	n = int(n)						#接收到的n為str 需要轉成int
	print(f'Received from {str(addr)}: {n}')
	if n == 0 or n == 1 :					#根據n的值計算結果
		print(f'Send to {str(addr)}: {n}')
		conn.send(str(n).encode())			#將結果回傳給客戶端
	else:
		for i in range(n-1):
			c = b;
			b = b + a;
			a = c;
		print(f'Send to {str(addr)}: {b}')
		conn.send(str(b).encode())
	print('conection closed')
	conn.close()
s.close()							#完成後斷開連線
