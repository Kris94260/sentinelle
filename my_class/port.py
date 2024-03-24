import json

class port():
    
    def __init__(self,numero) :
        self.numero= numero
        self.status=None
        self.delai=None
    
    def to_dict(self):
        return {
            'Numero': self.numero,
            'Status':self.status,
            'Delai': self.delai
        }
    def to_json(self):
        return json.dumps(self.to_dict())