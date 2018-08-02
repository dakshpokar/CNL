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
	def broadcastMessage(self):
		print("Broadcaster")
	def sendMessage(self):
		print("Sender")
	def showClients(self):
		print("Clients")
class Client:
	s = None
	def __init__(self):
		thread = threading.Thread(target = self.run, args = ())
		thread.daemon = True
		thread.start()
	def run(self):

		port = int(input("Enter the port number of Server: "))
		self.s = socket.socket()
		self.s.connect(('127.0.0.1', port))
	def sendMessage(self):
		self.s.sendall
	
class Chat:
	server = None
	client = None
	def createChatServer(self):
		print("#################################")
		print("######## Create a Server ########")
		print("#################################")
		self.server = Server()
		print("\nServer Made Successfully")
		conti = True
		while(conti == True):
			print("#################################")
			print("######## Server Options #########")
			print("#################################")
			print("1. Send message to particular client")
			print("2. Show connected clients")
			print("3. Broadcast Message to all clients")
		
			choice = int(input("Enter your choice: "))
			if(choice == 1):
				self.server.sendMessage()
			elif(choice == 2):
				self.server.showClients()
			elif(choice == 3):
				self.server.broadcastMessage()
			else:
				print("Invalid Choice")
			print("#################################")
			y = int(input("Do you want to continue Server Options[1/0]: "))
			if(y == 0):
				conti = False
			else:
				conti = True
	
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
		y = int(input("Do you want to continue Chat Options[1/0]: "))
		if(y == 0):
			conti = False
		else:
			conti = True
	
	
