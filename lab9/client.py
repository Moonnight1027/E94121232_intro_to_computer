import socket

HOST = '192.168.137.234'                                #�إ�socket
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected to 192.168.137.234")

outdata = input('The Fibonacci(n) when n = ');

s.send(outdata.encode())                                #�Ninput���G�ǵ����A��

if outdata == 'exit':                                   #���Jexit�ɤ��_�s�u
    print('Connection closed')
    s.close()
else:
    indata = s.recv(1024)
    print(f'The answer is: {indata.decode()}')




