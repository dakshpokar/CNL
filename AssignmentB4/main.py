import socket
import random
import os
import threading

class Server:
	def create(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.port = random.randint(10000,30000)
		self.s.bind(('', self.port))
		print("Socket binded to port: " + str(self.port))
		self.chatWindow()
		return
	def sender(self):
		while True:
			msg = bytes(input(), "utf-8")
			self.s.sendto(msg, self.addr)
	def receiver(self):
		while True:
			msg, self.addr = self.s.recvfrom(1024)
			print("Message from " + str(self.addr) + ": " + str(msg.decode("utf-8")))
	def chatWindow(self):
		print("Chat Window\n############################")
		threadS = threading.Thread(target = self.sender)
		threadR = threading.Thread(target = self.receiver)
		threadS.start()
		threadR.start()
class Client:
	def create(self):
		#self.ip = input("Enter the ip: ")
		self.ip = "127.0.0.1"
		self.port = int(input("Enter the port number of server: "))
		self.c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print("Socket binded successfully")
		self.chatWindow()
	def chatWindow(self):
		os.system("clear")
		print("Chat Window\n############################")
		threadS = threading.Thread(target = self.sender)
		threadR = threading.Thread(target = self.receiver)
		threadS.start()
		threadR.start()
	def sender(self):
		while True:
			msg = bytes(input(), "utf-8")
			self.c.sendto(msg, (self.ip, self.port))
	def receiver(self):
		while True:
			msg, addr = self.c.recvfrom(1024)
			print("Message from " + str(addr) + ": " + str(msg.decode("utf-8")))
		
	
print("Welcome to UDP Chat")
print("Choose")
print("1. Create a Server")
print("2. Join the Server")
choice = int(input("Enter your choice: "))
if(choice == 1):
	server = Server()
	server.create()
else:
	client = Client()
	client.create()
	client.chatWindow()
