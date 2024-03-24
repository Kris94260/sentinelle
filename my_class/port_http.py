from my_class import port
import json
import socket
import time
import requests
from my_class import dirbust


class port_http():
    
    def __init__(self,list=[80,8080,3128]):
        self.ports=[]
        self.name='http'
        self.server=None
        self.cms_name = None
        self.directories={}
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
    
    def get_cms_name(self,ip, port):
        lien = 'http://'+ip+':'+port+'/'
        page = requests.get(lien)
        print(ip, page.status_code)
        try:
            lien = 'http://'+ip+':'+port+'/'
            page = requests.get(lien)
            
            wp = str(page.content).count('wp-content')
            joomla = str(page.content).count('/templates')

            tab = {}
            tab['Inconnu'] = 1
            tab['Wordpress']=wp
            tab['Joomla']=joomla
            self.cms_name = max(tab,key=tab.get)
            print("go dir")
            #list_path=dirbust.dirbuster()
            
            #list_path.dirb(lien,'wordpress.txt')
            #print('a',list_path.to_dict())
    

        except Exception as e:
            print(e)
            self.cms_name="Inconnu"

            
    def test_port2(self,ip):
        for occ in self.ports:
            start_time=time.time()
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                
                # Essayer de se connecter au serveur
                sock.connect((ip, occ.numero))
                occ.status="open"
                occ.delai = (time.time() - start_time )*1000
                #self.get_cms_name(str(ip),str(occ.numero))

                print(f'HTTP -> {ip}:{occ.numero} is {occ.status}, CMS :{self.cms_name}, delai : {occ.delai}')
                self.open.append(occ.numero)
                            
            
            except socket.error as e:
                # La connexion a échoué
                occ.status="close"
            finally:
                # Fermer la connexion
                sock.close()


    def export_dir(self):
        with open('./analyse/server_json/dirbuster/'+'e', "w") as outfile:
            outfile.write(self.to_json())