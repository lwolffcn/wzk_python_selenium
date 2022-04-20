import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.connect((host, port))

print(s.recv(1024))
client_str = 'I am client_str'
s.send(client_str.encode('utf-8', 'strict'))
