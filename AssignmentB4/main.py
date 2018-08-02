#Importing all necessary libraries
import socket

class Chat:
	def createChatServer(self):
		print("Create Chat Server")
	def joinChatServer(self):
		print("Joined Chat Server")
		
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
	
	
