#Importing all necessary libraries
import socket
import random
import threading
import os
import sys

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
	def sender(self, uid):
		while True:
			msg = bytes(input(), "utf-8")
			self.sendMessage(msg, uid)
	def sendMessage(self, msg, uid):
		self.clients[uid].send(msg)
		
	def receiveFrom(self, uid,broad):
		print("Thread running"+str(uid))
		while True:
			msg = self.clients[uid].recv(1024)
			print("Received from " + "<"+str(self.addr[uid][0]) + "-" + str(uid) +">"+ ": " + msg.decode("utf-8"))
			print("##################################################################")
			if(str(msg.decode("utf-8")) == "exit0"):
				self.clients[uid].close()
				break
			if(broad == 1):
				msg = "Received from " + "<"+str(self.addr[uid][0]) + "-" + str(uid) +">"+ ": " + msg.decode("utf-8")
				msg = bytes(msg, "utf-8")
				for k in self.clients:
					if(k != uid):
						self.sendMessage(msg,k)
					
			
	def broadcastSender(self):
		while True:
			msg = input()
			msg = "Received from Server: " + msg
			msg = bytes(msg, "utf-8")
			for uid in self.clients:
				self.sendMessage(msg, uid)
		
	def chatP2P(self):
		os.system("clear")
		print("Server Side Chat Window")
		self.showClients()
		clientID = int(input("Enter ID: "))
		threadS = threading.Thread(target = self.sender, args = (clientID,))
		threadR = threading.Thread(target = self.receiveFrom, args = (clientID,0))
		threadS.start()
		print("##################################################################")
		threadR.start()
		return
	def chatBroadcast(self):
		os.system("clear")
		print("\nList of clients on Server: ")
		self.showClients()
		print("##################################################################")
		threadS = threading.Thread(target = self.broadcastSender, args = ())
		threadS.start()
		for uid in self.clients:
			threadR = threading.Thread(target = self.receiveFrom, args = (uid,1))
			threadR.start()
		return
	def showClients(self):
		for uid in self.clients:
			print(str(uid) + " belongs to " + str(self.addr[uid][0]) + " - " + str(self.addr[uid][1]))
class Client:
	s = None
	uid = None
	def __init__(self):
		thread = threading.Thread(target = self.run, args = ())
		thread.start()
		thread.join()	
		
	def run(self):
		#ip = str(input("Enter the IP of the Server: "))
		ip = "127.0.0.1"
		port = int(input("Enter the port number of Server: "))
		self.s = socket.socket()
		self.s.connect((ip, port))
		uid = self.s.recv(1024).decode('utf-8')
		print("\nYou are connected to server and you have been assigned - ")
		print("Unique ID: " + uid)
	def chatP2PServer(self):
		os.system("clear")
		print("Peer-2-Peer Chat Window Started")
		threadS = threading.Thread(target = self.sendMessage, args = ())
		threadR = threading.Thread(target = self.receiveFrom, args = (0,))
		threadS.start()
		print("##################################################################")
		threadR.start()
		return
	def chatP2PClient(self):
	
		return
	def chatBroadcast(self):
		os.system("clear")
		print("MultiUser Chat Window Started")
		threadS = threading.Thread(target = self.sendMessage, args = ())
		threadR = threading.Thread(target = self.receiveFrom, args = (1,))
		threadS.start()
		print("##################################################################")
		threadR.start()
		return
	def sendMessage(self):
		while True:
			msg = bytes(input(), "utf-8")
			self.s.send(msg)
			print("##################################################################")
	def receiveFrom(self,broad):
		while True:
			msg = self.s.recv(1024)
			if(broad == 1):
				print(msg.decode("utf-8"))
				print("##################################################################")
			else:
				print("Received from Server: " + msg.decode("utf-8"))
				print("##################################################################")
	
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
			print("1. Chat with particular Client")
			print("2. Show connected clients")
			print("3. Broadcast Chat with all Clients")
		
			choice = int(input("Enter your choice: "))
			if(choice == 1):
				thread = threading.Thread(target = self.server.chatP2P, args = ())
				thread.start()
				thread.join()
				break	
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
		conti = True
		while(conti == True):
			print("#################################")
			print("######## Client Options #########")
			print("#################################")
			print("1. P2P with Server")
			print("2. P2P with Clients on Server")
			print("3. Broadcast with Everyone on Server")
			choice = int(input("Enter your choice: "))
			if(choice == 1):
				thread = threading.Thread(target = self.client.chatP2PServer, args = ())
				thread.start()
				thread.join()
				break
			elif(choice == 2):
				self.client.chatP2PClient()
			elif(choice == 3):
				self.client.chatBroadcast()
				break
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
			break
		elif(choice == 2):
			chat.joinChatServer()
			break
		else:
			print("Invalid Choice")
		print("#################################")
		y = int(input("Do you want to continue Chat Options[1/0]: "))
		if(y == 0):
			conti = False
		else:
			conti = True
	
	
