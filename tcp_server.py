# coding:utf-8

import socket

host = '127.0.0.1'
port = 8000
BUFF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print u'服务器启动成功：%s:%s' % (host, port)

while True:
    client, addr = server.accept()  # addr为tuple:(host,port)
    print u'连接上',addr
    while True:
        data = client.recv(BUFF_SIZE)   # 从客户端接收数据
        print u'来自%s：%s' % (addr, data)
        client.sendall(data)
server.close()