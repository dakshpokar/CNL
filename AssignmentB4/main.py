#Importing all necessary libraries
import socket
import random
import threading

class Server:
	clients = {}
	addr = {}
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
			rand_id = random.randint(1,1000)
			self.clients[rand_id] = conn 
			self.addr[rand_id] = addr
			print("\n#################################")
			print("Client connected having "+str(addr)+" as Address")
			uid = str(rand_id)
			message = "Its Unique ID: " + uid
			print(message)
			conn.sendall(uid.encode('utf-8'))
	def broadcastMessage(self):
		print("Broadcaster")
	def sendMessage(self):
		print("Sender")
	def showClients(self):
		for uid in self.clients:
			print(str(uid) + " belongs to " + str(self.addr[uid][0]) + " - " + str(self.addr[uid][1]))
class Client:
	s = None
	uid = None
	def __init__(self):
		thread = threading.Thread(target = self.run, args = ())
		thread.daemon = True
		thread.start()
	def run(self):
		port = int(input("Enter the port number of Server: "))
		self.s = socket.socket()
		self.s.connect(('127.0.0.1', port))
		uid = self.s.recv(1024).decode('utf-8')
		print("\nYou are connected to server and you have been assigned - ")
		print("Unique ID: " + uid)
		
		
	def sendMessage(self):
		#abstract
		print("Abstract")
	
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
			print("1. Chat with particular client")
			print("2. Show connected clients")
			print("3. Broadcast Message to all clients")
		
			choice = int(input("Enter your choice: "))
			if(choice == 1):
				self.server.chatP2P()
			elif(choice == 2):
				self.server.showClients()
			elif(choice == 3):
				self.server.chatBroadcast()
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
		
		while(conti == True):
			print("#################################")
			print("######## Client Options #########")
			print("#################################")
			print("1. P2P with Server")
			print("2. Broadcast Messanger")
			choice = int(input("Enter your choice: "))
			if(choice == 1):
				self.client.chatP2P()
			elif(choice == 2):
				self.client.chatBroadcast()
			else:
				print("Invalid Choice")
			print("#################################")
			y = int(input("Do you want to continue Server Options[1/0]: "))
			if(y == 0):
				conti = False
			else:
				conti = True
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
	
	
