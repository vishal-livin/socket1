import socket
import threading

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()

port = 1234

s.bind((host,port))

def send():
        while(True):
                mess = input("enter the mes to send")
                b_mess = mess.encode()
                host = socket.gethostname()

                s.sendto(b_mess , (host,port))
                print("sent:" , mess)

def receive():
        while(True):
                b_mess = s.recvfrom(1024)
                mess = b_mess[0].decode()
                print("\nreceived:",mess)

t1 = threading.Thread(target = receive)
t2 = threading.Thread(target = send)
t1.start()
t2.start()


