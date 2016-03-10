# coding:utf-8

import socket

host = "127.0.0.1"
port = 8000
BUFF_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    data = raw_input(u'请输入命令：')
    client.sendall(data)
    response = client.recv(BUFF_SIZE)
    print response 
client.close()

