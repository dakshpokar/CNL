import math
ip = str(input("Enter the Network Address: "))
subnets = int(input("Enter the number of subnets: "))
bitmod = int(math.log(subnets)/math.log(2))
bitmodpower = 0
list_ip = ip.split(".")
net_ip_in_bin = []
for i in range(0,len(list_ip)):
    net_ip_in_bin.append('{0:08b}'.format(int(list_ip[i])));

if(int(list_ip[0]) <= 127):
    class_id = "A"
    bitmodpower = 24
elif(int(list_ip[0]) >= 128 and int(list_ip[0]) <= 192):
    class_id = "B"
    bitmodpower = 16
elif(int(list_ip[0]) >= 192 and int(list_ip[0]) <= 223):
    class_id = "C"
    bitmodpower = 8
    
if(class_id == "C" and subnets > 256):
    print("Cannot create more than "+ str(256) +" subnets with class C IP Address")
    exit()
elif(class_id == "B" and subnets > 256*256):
    print("Cannot create more than "+ str(256*256) +" subnets with class B IP Address")
    exit()
elif(class_id == "A" and subnets > 256*256*256):
    print("Cannot create more than "+ str(256*256*256) +" subnets with class C IP Address")
    exit()
    
print("Class is: " + str(class_id))
dict_masks = { "A": "255.0.0.0", "B" : "255.255.0.0", "C" : "255.255.255.0"}
print("Default Netmask is: " + dict_masks[class_id])
list_mask_ip = dict_masks[class_id].split(".")
mask_ip_in_bin = []
for i in range(0,len(list_mask_ip)):
    mask_ip_in_bin.append('{0:08b}'.format(int(list_mask_ip[i])));


spec_netmask = []
print("Specific Netmask is: ")
ssnm = []
ssnm.append((int(list_ip[0]) & int(list_mask_ip[0])))
ssnm.append((int(list_ip[1]) & int(list_mask_ip[1])))
ssnm.append((int(list_ip[2]) & int(list_mask_ip[2])))
ssnm.append((int(list_ip[3]) & int(list_mask_ip[3])))
print(str(ssnm[0]) + "." + str(ssnm[1]) + "." + str(ssnm[2]) + "." + str(ssnm[3]))

bin_gen = []
fomat ='{0:0'+str(bitmod)+'b}'
for i in range(0, pow(2,bitmod)):
    bin_gen.append(fomat.format(int(i)))
for i in range(0, len(bin_gen)):
    bin_gen[i] = bin_gen[i] + "0"*(8-bitmod);
bin_gen.append("11111111")
for i in range(0, pow(2,bitmod)):
    if(i == pow(2,bitmod)-1):
        print(str(list_ip[0]) + "." + str(list_ip[1]) + "." + str(list_ip[2]) + "." + str(int(bin_gen[i],2)) + " - " +
              str(list_ip[0]) + "." + str(list_ip[1]) + "." + str(list_ip[2]) + "." + str(int(bin_gen[i+1],2)))
    else:
        print(str(list_ip[0]) + "." + str(list_ip[1]) + "." + str(list_ip[2]) + "." + str(int(bin_gen[i],2)) + " - " +
              str(list_ip[0]) + "." + str(list_ip[1]) + "." + str(list_ip[2]) + "." + str(int(bin_gen[i+1],2)-1))
