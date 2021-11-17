import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("127.0.0.1", 50007))
    sock.sendall(b"client to server")
    DatA = sock.recv(1024)
    print(repr(DatA))
