import requests 
import os 
import json

class dirbuster():

    def __init__(self,url, wordlist):
        self.directory = []
        self.url=url
        self.wordlist=wordlist


    def dirb(self):
        try:
            if self.url[:7] != 'http://':
                self.url="http://"+self.url
            r=requests.get(self.url)
            if r.status_code == 200:
                print('Host is up.')
            else:
                print('Host is down.')
                return
            if os.path.exists(os.getcwd()+self.wordlist):
                fs=open(os.getcwd()+self.wordlist,"r")
                for i in fs:
                    print(i)
                    i =i.strip()
                    req =self.url+"/"+i
                    rq=requests.get(req)
                    if rq.status_code == 200:
                        
                        self.directory.append(str(self.url+"/"+i))
                fs.close()
            else:
                print(os.getcwd()+'..'+self.wordlist+" n'existe pas dans ce repertoire.")
        except Exception as e:
            print(e)
            

    def directories_to_dict(self):
        retour=[]
        for d in self.directory:
            retour.append(d.to_dict())
        return retour
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def to_dict(self):
        return {
            'Directory':self.directories_to_dict()
        } 