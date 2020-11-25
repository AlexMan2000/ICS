import socket

def main():

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定一个本地信息
    local_addr = ("", 7788)
    s.bind(local_addr)

    #接收数据
    recv = s.recvfrom(1024) #1024表示本次接收的最大字节数

    #打印接收到的数据
    print(recv)


    #关闭套接字
    s.close()


if "__name__" == "__main__":
    main()