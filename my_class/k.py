import subprocess

def nmblookup(host):
    try:
        # Exécute la commande nmblookup -A <host> et capture la sortie
        result = subprocess.check_output(["nmblookup", "-A", host], universal_newlines=True)

        # Affiche la sortie de la commande
        print(result)

    except subprocess.CalledProcessError as e:
        # En cas d'erreur, affiche un message d'erreur
        print(f"Erreur lors de l'exécution de nmblookup : {e}")

# Appel de la fonction avec un exemple d'hôte
nmblookup("192.168.50.106")
