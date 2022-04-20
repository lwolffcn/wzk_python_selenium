import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    print(c)
    server_str = 'Thank you for connecting server_str'
    c.send(server_str.encode('utf-8', 'strict'))
    print(c.recv(1024))
    # c.close()
