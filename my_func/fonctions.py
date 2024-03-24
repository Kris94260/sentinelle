import netifaces
from my_class import interface


def load_interfaces():
    num=0
    interfaces=[]
    for interface_str in netifaces.interfaces():
        obj = interface.Interface(interface_str,num)
        if obj.ip_address and str(obj.ip_address)!='127.0.0.1':
            interfaces.append(interface.Interface(interface_str,num))
            num+=1
    return interfaces

def choix_interface(interfaces):
    print('---------------------------')
    for interface in interfaces:
        print("Numero de l'interface :",interface.numero)
        print("Nom de l'interface :",interface.interface)
        print("IP de l'interface :",interface.ip_address,"/",interface.mask)
        print('---------------------------')