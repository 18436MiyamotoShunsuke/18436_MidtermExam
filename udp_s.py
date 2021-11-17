import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as a11:
    a11.bind(("127.0.0.1", 50007))
    while True:
        recvdata, fromaddr = a11.recvfrom(1024)
        print("data: {}, addr: {}".format(recvdata, fromaddr))