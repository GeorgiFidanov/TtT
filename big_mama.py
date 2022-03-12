import socket
import os
from _thread import *
import threading

ServerSideSocket = socket.socket()
ThreadCount = 0

#host = '127.0.0.1'
host = '192.168.1.20'
port = 2004

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))


print('Socket is listening..')
ServerSideSocket.listen(5)

def translete_msg(msg):
    return msg.upper()


clients = set()
clients_lock = threading.Lock()
                        #Client
def multi_threaded_client(connection):
    global clients_lock

    connection.send(str.encode('Server is working:'))
    
    with clients_lock:
        clients.add(connection)
    try:
        while True:
        
            data = connection.recv(2048)
            response = 'Server message: ' + data.decode('utf-8')

            if not data:
                break
            
            msg_out = translete_msg(str(response))
            print(msg_out)
            with clients_lock:
                for curr in  clients:
                    curr.sendall(msg_out.encode())
    finally:
        with clients_lock:
            clients.remove(connection)
            connection.close() 


def make_server():
    global ThreadCount 
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))


while True:    
    make_server()

ServerSideSocket.close()
