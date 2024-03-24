import socket

def get_netbios_name(ip_address):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip_address)
        return host_name
    except socket.herror:
        return None
        
        
# Remplacez "192.168.1.1" par l'adresse IP que vous souhaitez rechercher
ip_address = "192.168.50.146"
netbios_name = get_netbios_name(ip_address)

if netbios_name:
    print(f"Le nom NetBIOS associé à {ip_address} est : {netbios_name}")
else:
    print(f"Aucun nom NetBIOS trouvé pour l'adresse IP : {ip_address}")
    
input()