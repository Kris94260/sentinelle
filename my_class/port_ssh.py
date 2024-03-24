

from my_class import port
import json
import socket
import time


class port_ssh():
    
    def __init__(self,list=[22]):
        self.ports=[]
        self.name='ssh'
        self.open=[]
        for i in list:
            self.ports.append(port.port(i))

    def to_dict(self):
        return {
            'Name':self.name,
            'Ports': self.ports_to_dict(),
        }
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def ports_to_dict(self):
        
        retour=[]
        for port in self.ports:
            retour.append(port.to_dict())
        return retour
    

    def test_port2(self,ip):
        for occ in self.ports:
            start_time=time.time()
            try:
                #start_time = datetime.now()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                # Fixer un délai d'attente pour la connexion (en secondes)
                sock.settimeout(0.5)
                
                # Essayer de se connecter au serveur
                sock.connect((ip, occ.numero))
                occ.status="open"
                occ.delai = (time.time() - start_time )*1000
                print(f'SSH -> {ip}:{occ.numero} is {occ.status}, delai : {occ.delai}')
                self.open.append(occ.numero)
                
            except socket.error as e:
                # La connexion a échoué
                occ.status="close"
            finally:
                # Fermer la connexion
                
                sock.close()