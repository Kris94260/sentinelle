import json
import ipaddress
from my_class import machine_distante
from multiprocessing import  Manager
from my_class import ports_map
import datetime
import os
from alive_progress import alive_bar


class map_reseau():

    def __init__(self,interface,manager=1):
        self.filename=None
        self.interface=interface
        self.manager=manager
        self.first_add=None
        self.last_add=None
        self.network_add=str(interface.network_address).split('/')[0]
        self.broadcast_address=None
        self.list_ip=[]
        self.hotes=[]
        self.hosts_available=[]
        self.define_network()
        self.scan_run=False
        self.protocoles=['http','ssh','sql','ftp']

    def define_network(self):
        self.ipaddress = ipaddress.IPv4Address(self.network_add)
        self.mask = ipaddress.IPv4Address(str(self.interface.mask))
        self.network = ipaddress.IPv4Network(f"{self.ipaddress}/{self.mask}", strict=False)
        self.broadcast_address=self.network.broadcast_address
        self.first_add=self.network.network_address +1
        self.last_add=self.broadcast_address -1
        
        
        ip=self.first_add
        compteur = 1
        while ip!=self.last_add:
            ip=self.network.network_address + compteur
            self.list_ip.append(str(ip))
            compteur+=1
        
        


    def scan_host(self):
        self.hotes=[]
        for ip in self.list_ip:
            map_ports=ports_map.ports_map()
            hote=machine_distante.machine_distante(ip,self.manager,map_ports)
            self.hotes.append(hote)
        print("\n\nHôtes pingables :\n---------------------------")
        total_iterations = len(self.hotes)
        with alive_bar(total_iterations, title='Progression') as bar:
            for x in range(0,len(self.hotes),10):
                for i in range(x,x+10):
                    try:
                        if self.hotes[i]:
                            
                                self.hotes[i].ping2()
                                if self.hotes[i].pingable:
                                    self.hotes[i].get_mac()
                                    print('IP :',self.hotes[i].ip, ' MAC :',self.hotes[i].mac)
                    except:
                        pass
                    bar()

    def scan_all_ports(self):
        self.scan_run =True
        
        for y in self.protocoles:
            print('\n---------------------------')
            print(f"Scan des port {y}")
            print('---------------------------')
            for i in self.hotes:
                if i.pingable==True :
                    i.scan_ports(y)


    def scan_protocol(self,protocol):
        self.scan_run=True
        print('\n---------------------------')
        print(f"Scan des port {protocol}")
        print('---------------------------')

        for i in self.hotes:
            if i.pingable==True:
                i.scan_ports(protocol)


    def hotes_to_dict(self):
        
        retour=[]
        for hote in self.hotes:
            retour.append(hote.to_dict())
        return retour
    
    def print_all(self):
        for y in self.protocoles:
            print('\n---------------------------')
            print(f"Résultat des port {y}")
            print('---------------------------')

            for i in self.hotes:
                if i.pingable==True :
                    if y=='http' and i.map_ports.http.open:
                        print(i.ip,'-',i.map_ports.http.open)
                    elif y=='ssh' and i.map_ports.ssh.open:
                        print(i.ip,'-',i.map_ports.ssh.open)
                    elif y=='sql' and i.map_ports.sql.open:
                        print(i.ip,'-',i.map_ports.sql.open)
                    if y=='ftp' and i.map_ports.ftp.open:
                        print(i.ip,'-',i.map_ports.ftp.open)
        self.export_files()




    def ihm_s(self):
        entree_clavier=''
        while entree_clavier!='q':
            print('\nall : scanner tous les ports des machines accessible')
            print('http : scanner les ports http des machines accessibles')
            print('ssh : scanner les ports ssh des machines accessibles')
            print('sql : scanner les ports sql des machines accessibles')
            print('ftp : scanner les ports ftp des machines accessibles')
            print('q : quitter le menu des scan')
            entree_clavier = input("Entrez votre choix : ")
            if entree_clavier=='all':
                self.scan_all_ports()
            elif entree_clavier=='http':
                self.scan_protocol(entree_clavier)
            elif entree_clavier=='ssh':
                self.scan_protocol(entree_clavier)
            elif entree_clavier=='sql':
                self.scan_protocol(entree_clavier)
            elif entree_clavier=='ftp':
                self.scan_protocol(entree_clavier)

        print('---------------------------')



    def ihm(self):
        entree_clavier=0
        self.scan_host()
        while entree_clavier!='q':
            print('\nq : quitter')
            print('s : scanner les ports des machines accessibles')
            print('p : afficher le resultat') if self.scan_run else ''
            entree_clavier = input("Entrez votre choix : ")
            
            if self.scan_run:
                if entree_clavier=='p':
                    self.print_all()
               

            if entree_clavier=='s':
                self.ihm_s()

    def to_json(self):
        return json.dumps(self.to_dict())
    
    def to_dict(self):
        return {
            'nom interface': self.interface.interface,
            'first address': str(self.first_add),
            'last address': str(self.last_add),
            'network_address': str(self.network_add),
            'broadcast' :str(self.broadcast_address),
            'Hotes':self.hotes_to_dict()
        } 
    

    def export_files(self):
        
        dirname= "./analyse/server_json/"
        self.filename = "{}.json".format(datetime.datetime.now().strftime("%m-%d_%H-%M-%S"))
        with open(dirname+'data/'+self.filename, "w") as outfile:
            outfile.write(self.to_json())

        