import socket
import os

print("\nWelcome to DNS lookup")
print("\nChoose from the following")
print("1. Enter IP Address")
print("2. Enter URL")
choice = int(input("Enter your choice: "))
if(choice == 1):
	ip = input("Enter the IP Address: ")
	print(os.system("nslookup " + str(ip)))
else:
	url = input("Enter the URL: ")
	print(socket.gethostbyname(url))

