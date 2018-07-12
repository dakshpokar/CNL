import ipaddress
import math

class Subnet:
	net_ip = ""
	nsubs = 0
	subnets = []
	def classful(self):
		self.net_ip = str(input("Enter Classful Network IP: "))
		self.nsubs = int(input("Enter the number of subnets: "))
		
	def classless(self):
		self.net_ip = str(input("Enter Classless Network IP: "))
		self.nsubs = int(input("Enter the number of subnets: "))
		list_ip = self.net_ip.split(".")
		prefix_diff = int(math.log(self.nsubs)/math.log(2))
		self.subnets = list(ipaddress.ip_network(self.net_ip).subnets(prefix_diff)) 
		self.display()
	def display(self):
		c = 1
		for i in self.subnets:
			print("Subnet "+str(c)+" ::: "+str(i[0])+" - "+str(i[-1]))
			c = c + 1
		
if __name__ == "__main__":
	subnet = Subnet()
	#subnet.classful()
	subnet.classless()
