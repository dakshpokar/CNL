#Importing all necessary libraries
import socket
import random
import threading

class Server:
	def __init__(self):
		thread = threading.Thread(target = self.run, args = ())
		thread.daemon = True
		thread.start()
	def run(self):
		s = socket.socket()
		print("Socket created successfully.")
		port = random.randint(10000,30000)
		s.bind(('', port))
		print("Socket binded to port "+str(port))
		s.listen(5)
		print("Awaiting for connections")
		while True:
			conn, addr = s.accept()
			print("Client connected having "+str(addr)+" as Address")
			message = 'Welcome to Chat Server'
			conn.sendall(message.encode('utf-8'))
			conn.close()
class Client:
	def __init__(self):
		thread = threading.Thread(target = self.run, args = ())
		thread.daemon = True
		thread.start()
	def run(self):

		port = int(input("Enter the port number of Server: "))
		s = socket.socket()
		s.connect(('127.0.0.1', port))
		print(s.recv(1024).decode('utf-8'))
		s.close()
class Chat:
	server = None
	client = None
	def createChatServer(self):
		print("#################################")
		print("######## Create a Server ########")
		print("#################################")
		self.server = Server()
		return
		
	def joinChatServer(self):
		print("Joined Chat Server")
		self.client = Client()
		return
		
if __name__ == "__main__":
	chat = Chat()
	conti = True
	while(conti):
		print("#################################")
		print("#### Welcome to Chat Program ####")
		print("#################################")
		print("1. Create your own server")
		print("2. Join a server")
		choice = int(input("Enter your choice: "))
		if(choice == 1):
			chat.createChatServer()
		elif(choice == 2):
			chat.joinChatServer()
		else:
			print("Invalid Choice")
		print("#################################")
		y = int(input("Do you want to continue[1/0]: "))
		if(y == 0):
			conti = False
		else:
			conti = True
	
	
