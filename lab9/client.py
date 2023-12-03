import socket

HOST = '192.168.137.234'                                #建立socket
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected to 192.168.137.234")

outdata = input('The Fibonacci(n) when n = ');

s.send(outdata.encode())                                #將input結果傳給伺服器

if outdata == 'exit':                                   #當輸入exit時中斷連線
    print('Connection closed')
    s.close()
else:
    indata = s.recv(1024)
    print(f'The answer is: {indata.decode()}')




