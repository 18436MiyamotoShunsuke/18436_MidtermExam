import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockettt:
    sockettt.bind(("0.0.0.0",50007))
    sockettt.listen(1)
    while True:
        connection, fromaddr = sockettt.accept()
        with connection:
            while True:
                receivedata = connection.recv(1024)
                if not receivedata:
                    break
                print("data : {}, addr: {}".format(receivedata, fromaddr))
                #connECtion.sendall(b'received')
