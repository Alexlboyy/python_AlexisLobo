import collector

def afficher_systeme(donnees_systeme, heure):
    """Cette fonction permet d'afficher les données du systeme reçu de façon formaté

    Parametres:
        donnees_systeme (dict): C'est un dictionnaire contenant toute les informations du systeme envoyer depuis collector.py
        heure (_type_): Cela permet de recupérer le timestamp
    """
    print("======INFORMATION SYSTEME======")
    print(f"Données du : {heure.get("timestamp")}")
    print(f"Type d'OS : {donnees_systeme.get("os")}")
    print(f"Version de l'OS : {donnees_systeme.get("os")} {donnees_systeme.get("version")}")
    print(f"Type d'architecture : {donnees_systeme.get("architecture")}")
    print(f"Le hostname : {donnees_systeme.get("hostname")}")
    print("===============================")

def afficher_cpu(donnees_cpu, heure):
    """Cette fonction permet d'afficher les données du CPU reçu de façon formaté

    Parametres:
        donnees_cpu (dict): C'est un dictionnaire contenant toute les informations du CPU envoyer depuis collector.py
        heure (_type_): Cela permet de recupérer le timestamp
    """
    print("========INFORMATION CPU========")
    print(f"Données du : {heure.get("timestamp")}")
    print(f"Nombre de coeurs physiques : {donnees_cpu.get("coeurs_physiques")} coeurs")
    print(f"Nombre de coeurs logiques : {donnees_cpu.get("coeurs_logiques")} coeurs")
    print(f"Pourcentage d'utilisation du CPU : {donnees_cpu.get("utilisation")} %")
    print("===============================")

def afficher_ram(donnees_memoire, heure):
    """Cette fonction permet d'afficher les données de la mémoire reçu de façon formaté

    Parametres:
        donnees_memoire (dict): C'est un dictionnaire contenant toute les informations de la mémoire envoyer depuis collector.py
        heure (_type_): Cela permet de recupérer le timestamp
    """
    print("========INFORMATION RAM========")
    print(f"Données du : {heure.get("timestamp")}")
    print(f"Total de mémoire : {octets_vers_go(donnees_memoire.get("total"))}")
    print(f"Disponibilité de la mémoire : {octets_vers_go(donnees_memoire.get("disponible"))}")
    print(f"Pourcentage d'utilisation de la mémoire : {donnees_memoire.get("pourcentage")} %")
    print("===============================")

def afficher_disques(donnees_disques, heure):
    """Cette fonction permet d'afficher les données des disques reçu de façon formaté

    Parametres:
        donnees_disques (dict): C'est un dictionnaire contenant toute les informations des disques envoyer depuis collector.py
        heure (_type_): Cela permet de recupérer le timestamp
    """
    nombre_de_disque = 1
    print("======INFORMATION DISQUES======")
    for disque in donnees_disques:
        print(f"Disque {nombre_de_disque} :")
        print(f"Données du : {heure.get("timestamp")}")
        print(f"Point de montage du disque : {disque.get("point_montage")}")
        print(f"Nombre total du disque : {disque.get("total")}")
        print(f"Nombre total du disque utilisé : {disque.get("utilise")}")
        print(f"Pourcentage du disque utilisé : {disque.get("pourcentage")} %")
        nombre_de_disque = nombre_de_disque + 1
    print("===============================")

def afficher_tout():
    """Cette fonction permet de faire appelle a toute les autres fonctions pour tout afficher en même temps 
    """
    print("======INFORMATION GENERAL======")
    donnees_sys = collector.collecter_info_systeme()
    print()
    afficher_systeme(donnees_sys, heure)
    donnees_cpu = collector.collecter_cpu()
    print()
    afficher_cpu(donnees_cpu, heure)
    donnees_ram = collector.collecter_memoire()
    print()
    afficher_ram(donnees_ram, heure)
    donnees_disques = collector.collecter_disques()
    print()
    afficher_disques(donnees_disques, heure)
    print("===============================")

def octets_vers_go(octets):
    GB = str(round(octets/1024**3, 2)) + "GB"
    return(GB)

heure = collector.collecter_tout()

print("Selectionner une option :")
print("1 - Données generale")
print("2 - Données système")
print("3 - Données CPU")
print("4 - Données RAM")
print("5 - Données disques")
print()
print(f"Votre choix ?")
choix = input()

if choix == "1":
    afficher_tout()
elif choix == "2":
    donnees_sys = collector.collecter_info_systeme()
    afficher_systeme(donnees_sys, heure)
elif choix == "3":
    donnees_cpu = collector.collecter_cpu()
    afficher_cpu(donnees_cpu, heure)
elif choix == "4":
    donnees_ram = collector.collecter_memoire()
    afficher_ram(donnees_ram, heure)
elif choix == "5":
    donnees_disques = collector.collecter_disques()
    afficher_disques(donnees_disques, heure)
else:
    print("Veuillez choisir un choix valide !")