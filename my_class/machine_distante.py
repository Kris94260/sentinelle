import subprocess
import platform
import json
from multiprocessing import Process
from ping3 import ping
from scapy.all import ARP,Ether,srp



class machine_distante():

    def __init__(self,ip,manager,map_ports):
        self.map_ports=map_ports
        self.manager = manager
        self.ip= ip
        self.pings = None  # Indicates if subprocess.run has worked
        self.pingable = None #self.manager.Value('i', 0)
        self.mac =''

    def get_mac(self):
        try:
            arp =ARP(pdst=self.ip)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether/arp
            result = srp(packet, timeout=0.1, verbose=False)[0]
            mac = result[0][1].hwsrc
            self.mac = mac

        except Exception as e:
            pass

    def ping2(self):
        try:
            response = ping(self.ip, timeout=0.05)            
            self.pings="OK"
            if response:
                self.pingable=True
            else :
                self.pingable=False
            
        except Exception as e:
            pass


    def ping(self,nombre=1):
        print(self.ip,"start ping")
        parametres_ping = ["ping", "-c", str(nombre)]  # Pour Linux et macOS
        if platform.system().lower() == "windows":
            parametres_ping = ["ping", "-n", str(nombre)]  # Pour Windows

        try:
            # Exécuter la commande ping et capturer la sortie
            resultat = subprocess.run(parametres_ping + [self.ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

            # Vérifier la sortie pour déterminer si le ping a réussi
            self.pingable = "0% packet loss" in resultat.stdout
            self.pings = True
        except subprocess.CalledProcessError:
            # En cas d'erreur, retourner False
            self.pings =False

        #print(self.to_json())
        #return self.pingable
        print(self.ip,"stop ping", self.pingable)


    def tPing(self, nombre=1):
        process_ping = Process(target=self.ping, args=(nombre,))
        process_ping.start()
        #process_ping.join()

    def scan_ports(self,protocol):
        self.map_ports.scan(self.ip,protocol)
        #print("abruti",self.map_ports.to_dict())

    def to_dict(self):
        return {
                'IP': self.ip,
                'MAC': self.mac,
                'subprocess': self.pings,
                'Hote_pingable': self.pingable,
                'Map_ports': self.map_ports.to_dict()
            }
    
    def to_json(self):
        return json.dumps(self.to_dict())
