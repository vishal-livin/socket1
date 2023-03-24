import time,socket,sys
print("intialising.....")
time.sleep(1)
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host,port))
print(host,"(",ip,")\n")
name = input(str("enter your name.."))
s.listen(1)
print("\n waiting for incoming connection...")
conn, addr = s.accept()
print("\n recevied connection from",addr[0],"(",addr[1])
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name,"has connected to chat room")
conn.send(name.encode())
while True:
    message = input(str("me:"))
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name,":",message)
    
    
    

#import time,socket,sys
#print("intialising.....")
#time.sleep(1)
#s = socket.socket()
