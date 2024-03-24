
import ipaddress
import netifaces
import json


class Interface:
    def __init__(self,interface,numero):
        self.interface=interface
        self.ip_address = None
        self.mask = None
        self.network_address=None
        self.speed=None
        self.numero=numero

        self.information_ip()        
        #print(netifaces.ifaddresses(self.interface))
    def information_ip(self):
        if 2 in netifaces.ifaddresses(self.interface) :
           
            ip_address = netifaces.ifaddresses(self.interface)[2][0]['addr'] 
            mask = netifaces.ifaddresses(self.interface)[2][0]['netmask']
            self.ip_address = ipaddress.IPv4Address(ip_address)
            self.mask = ipaddress.IPv4Address(mask)
            self.network_address = ipaddress.IPv4Network(f"{self.ip_address}/{self.mask}", strict=False)
        
    def to_dict(self):
        return {
            'Numero': self.numero,
            'interface': self.interface,
            'ip_address': str(self.ip_address),
            'mask': str(self.mask),
            'network_address': str(self.network_address),
            'speed': str(self.speed)
        }

    def to_json(self):
        return json.dumps(self.to_dict())


    

  
       

