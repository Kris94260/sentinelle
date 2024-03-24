from my_class import map_reseau
from my_func import fonctions

interfaces=fonctions.load_interfaces()
num=len(interfaces)
manager=94 # a remplacer par with Manager() as manager
while num>=0:
    print("""
 ____  _____ _   _ _____ ___ _   _ _____ _     _     _____ 
/ ___|| ____| \ | |_   _|_ _| \ | | ____| |   | |   | ____|
\___ \|  _| |  \| | | |  | ||  \| |  _| | |   | |   |  _|  
 ___) | |___| |\  | | |  | || |\  | |___| |___| |___| |___ 
|____/|_____|_| \_| |_| |___|_| \_|_____|_____|_____|_____|
                                                    By Krxs94
      """)
    print("Nombre d'interfaces trouver :",num)
    interface_num=-1
    if num>0:
        fonctions.choix_interface(interfaces)
        print('q : quitter')
        print('r : lancer un nouveau scan')
        interface_to_scan = input("Entrez le numero de l'interface que vous voulez scanner ? : ")
        if interface_to_scan.isdigit():
            interface_num = int(interface_to_scan)
        if 0 <= interface_num < num:
            map = map_reseau.map_reseau(interfaces[interface_num],manager)
            map.ihm()
            break

        elif interface_to_scan =='q':
            num=-1
        elif interface_to_scan =='r':
            interfaces = fonctions.load_interfaces()
            num = len(interfaces)
        else:
            print('\n\nLe choix est invalide\n\n')

    elif num==0:
        print('1 : Scanner les interfaces à nouveau')
        print('q : Quitter le programme')
        reponse=input("Appuyer une touche pour relancer le scan : ")
        if reponse == '1':
            interfaces = fonctions.load_interfaces()
            num = len(interfaces)
        elif reponse == 'q':
            num = -1
        else:
            print('\n\nLe choix est invalide\n\n')
        



