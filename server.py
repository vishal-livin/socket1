import time,socket,sys
print("intialising.....")
time.sleep(1)
s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
host = input(str("enter the ip to connect"))
name = input(str("enter your name"))
port = 1234
print ("\n trying to connect to", host)
time.sleep(1)
s.connect((host,port))
print(" connected...\n")
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")
while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name,":",message)
    message = input(str("me :"))
    s.send(message.encode())