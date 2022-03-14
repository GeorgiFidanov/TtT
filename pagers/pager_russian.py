import socket
from _thread import *
import json 
import time
from host import host,port

ClientMultiSocket = socket.socket()


header = {"name": "Ivanushka", "language": "ru", "reciever":"", "msg":""}  # a real dict.
init_header = {"name": "Ivanushka", "language": "ru"}

demo1 = "Как тебя зовут?"
demo2 = "Роскосмос лучше, чем НАСА!"
demo3 = "Возьмите водку и повеселитесь на МКС!"
demos = [demo1, demo2, demo3]

recievers = ['Markos','Marioo','Pier']

print('Waiting for connection response')

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)

def send_init_msg():
    data = json.dumps(init_header)
    ClientMultiSocket.send(bytes(data,encoding="utf-8"))

def send_msg():
    i = 0
    while True:
        header["reciever"] = recievers[i]
        header["msg"] = demos[i]
        data = json.dumps(header)
        ClientMultiSocket.send(bytes(data,encoding="utf-8"))
        i+=1
        if i == 3:
            i = 0
        time.sleep(10)
def receive_msg():
    while True:
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))



send_init_msg()
start_new_thread(receive_msg, ())
send_msg()

ClientMultiSocket.close()
