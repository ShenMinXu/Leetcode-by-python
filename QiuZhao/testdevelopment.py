import socket
# 开启ip和端口
ip_port = ('127.0.0.1', 9999)
# 生成一个socket对象
sk = socket.socket()
# 绑定ip端口
sk.bind(ip_port)
# 最多连接数
sk.listen(5)
# 开启死循环等待客户端连接
while True:
    print('服务器启动...')
    # 等待链接,阻塞，直到渠道链接 conn打开一个新的对象专门给当前链接的客户端 addr是ip地址
    conn, addr = sk.accept()
    print("客户端地址:",str(addr))
    # 获取客户端请求数据
    client_data = conn.recv(1024)
    # 打印对方的数据
    print(client_data.decode("utf-8"))
    # 向对方发送数据
    #也可写成conn.send("来自服务器的问候".encode("utf-8"))
    conn.send(bytes("来自服务器的问候","utf-8"))
    # 关闭链接
    conn.close()