import socket

def main():
    while True:
        msg = input("请输入想要发送的数据:(输入q退出)")

        if msg == "q":
            break
        #创建udp套接字
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        #可以使用套接字收发数据
        s.sendto(msg.encode("gbk"),("192.168.61.1",8080))

        #关闭套接字
        s.close()



if __name__ == '__main__':
    main()