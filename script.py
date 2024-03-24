import socket
import ipaddress
import netifaces


class MyConf:
    def __init__(self):
        self.interface='wlp2s0'
        self.ip_address_str = netifaces.ifaddresses(self.interface)[2][0]['addr']
        self.mask_str = netifaces.ifaddresses(self.interface)[2][0]['netmask']
        self.ipaddress = ipaddress.IPv4Address(self.ip_address_str)
        self.mask = ipaddress.IPv4Address(self.mask_str)

        self.calculate_network_range()


    def calculate_network_range(self):
        self.network_address = ipaddress.IPv4Network(f"{self.ipaddress}/{self.mask}", strict=False)
        self.first_lan_address = self.network_address.network_address + 1
        self.last_lan_address = self.network_address.broadcast_address - 1

    def list_ip(self):
        k=self.first_lan_address
        i = 0
        while k!=self.last_lan_address:
            k=self.network_address.network_address + i
            print(k)
            i+=1
        print(i)

my_conf_instance = MyConf()
my_conf_instance.list_ip()
print("IP Address:", my_conf_instance.ipaddress)
print("Mask:", my_conf_instance.mask)
print("First LAN Address:", my_conf_instance.first_lan_address)
print("Last LAN Address:", my_conf_instance.last_lan_address)




  
 
