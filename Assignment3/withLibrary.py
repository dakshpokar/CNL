import ipaddress
import math
import os

class Subnet:
	net_ip = ""
	nsubs = 0
	subnets = []
	def classful(self):
		self.net_ip = str(input("Enter Classful Network IP: "))
		if self.checkIP(self.net_ip) == False:
			return
		self.nsubs = int(input("Enter the number of subnets: "))
		prefix_diff = int(math.log(self.nsubs)/math.log(2))		#bits to modify
		list_ip = self.net_ip.split(".")
		if(int(list_ip[0]) < 127):
			class_id = "A"
		elif(int(list_ip[0]) >= 128 and int(list_ip[0]) < 192):
			class_id = "B"
		elif(int(list_ip[0]) >= 192 and int(list_ip[0]) < 223):
			class_id = "C"
		else:
			print("Class D and E addresses are not allowed")
			return
		print("The Network IP belongs to Class " + class_id)
		dict_masks = { "A": "255.0.0.0", "B" : "255.255.0.0", "C" : "255.255.255.0" } 
		subnet_mask = dict_masks[class_id]
		print("Therefore default subnet mask is: " + subnet_mask)
		#To find subnet mask 
		ssbmask = []
		prefix_diff += 8
		if(prefix_diff in range(0,8)):
			ssbmask.append(str(sum( 2**(8 - x) for x in range(1,prefix_diff+1))))
			ssbmask.append(0)
			ssbmask.append(0)
			ssbmask.append(0)						
		elif(prefix_diff in range(8,16)):
			ssbmask.append(255)
			ssbmask.append(str(sum( 2**(8 - x) for x in range(1,prefix_diff+1-8))))
			ssbmask.append(0)
			ssbmask.append(0)
		elif(prefix_diff in range(16,24)):
			ssbmask.append(255)
			ssbmask.append(255)
			ssbmask.append(str(sum( 2**(8 - x) for x in range(1,prefix_diff+1-16))))
			ssbmask.append(0)
		elif(prefix_diff in range(24,32)):
			ssbmask.append(255)
			ssbmask.append(255)				
			ssbmask.append(255)				
			ssbmask.append(str(sum( 2**(8 - x) for x in range(1,prefix_diff+1-24))))					
		calc_ssbmask = str(ssbmask[0]) + "." + str(ssbmask[1]) + "." + str(ssbmask[2]) + "." + str(ssbmask[3])
		print("Calculated Subnet Mask is: " + calc_ssbmask)
		#Anding SubnetMask and given IP to get Network IP
		
		
		
	def classless(self):
		self.net_ip = str(input("Enter Classless Network IP: "))
		self.nsubs = int(input("Enter the number of subnets: "))
		first_split = self.net_ip.split("/")
		if self.checkIP(first_split[0]) == False:
			return
		list_ip = first_split[0].split(".")
		mask_bits = first_split[1]
		print(list_ip)
		print(mask_bits)
		
		prefix_diff = int(math.log(self.nsubs)/math.log(2))
		self.subnets = list(ipaddress.ip_network(self.net_ip).subnets(prefix_diff)) 
		self.display()
	def display(self):
		c = 1
		for i in self.subnets:
			print("Subnet "+str(c)+" \t "+str(i[0])+" \t "+str(i[-1]))
			c = c + 1
	def findwithinSubnet(self):
		key = str(input("Enter the IP Address to find: "))
		c = 0
		for i in self.subnets:
			c += 1 
			for j in i:
				if(key == str(j)):
					print("Found IP in: " + str(c) + " Subnet");
					break;
	def setIP(self):
		ip = str(input("Enter the IP you want to set: "))
		os.system("ifconfig")
		inteface = str(input("Enter your interface: "))
		os.system("sudo ifconfig "+inteface+" "+ip)
	
	def pingIP(self):
		ip = str(input("Enter the ip address: "))
		x = os.system("ping "+ip+" -c 1")
		if(x == 512):
			print("Host is down!")
	def checkIP(self, ip):
		list_ip = ip.split(".")
		if not '.' in ip:
			print("IP Address invalid")
			return False
		else:
			for i in list_ip:
				if(int(i) > 255 or int(i) < 0):
					print("The IP address values ranges between 0 and 255")
					return False
					break
		return True	
		
if __name__ == "__main__":
	subnet = Subnet()

	print("Welcome to Subnetter")
	print("Select any one option from the following")
	print("1. Find Subnets Ranges using classless IP")
	print("2. Find SUbnets Ranges using classful IP")
	choice = int(input("Enter your choice: "))
	if(choice == 1):
		subnet.classless()
	else:
		subnet.classful()
