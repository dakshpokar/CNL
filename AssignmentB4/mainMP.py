import socket
import random
import os
import threading

class Server:
	addr_list = []
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
			for i in self.addr_list:
				self.s.sendto(msg, i)
	def receiver(self):
		while True:
			msg, self.addr = self.s.recvfrom(1024)
			if(self.addr not in self.addr_list):
				self.addr_list.append(self.addr)
			else:
				print("Message from " + str(self.addr) + ": " + str(msg.decode("utf-8")))
				msg = str(msg.decode("utf-8"))
				msg = msg + "|||" + str(self.addr)
				for i in self.addr_list:
					if(i != self.addr):
						self.s.sendto(bytes(msg, "utf-8"), i)
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
		self.c.sendto(bytes('',"utf-8"), (self.ip, self.port))
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
			if("|||" in msg.decode("utf-8")):
				msg, addr = msg.decode("utf-8").split("|||")
				print("Message from " + str(addr) + ":" + str(msg))
			else:
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
