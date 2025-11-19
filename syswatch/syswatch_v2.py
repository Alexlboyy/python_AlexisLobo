import collector

def afficher_systeme(donnees_systeme):
    print("======INFORMATION SYSTEME======")
    print(f"Type d'OS : {donnees_systeme.get("os")}")
    print(f"Version de l'OS : {donnees_systeme.get("os")} {donnees_systeme.get("version")}")
    print(f"Type d'architecture : {donnees_systeme.get("architecture")}")
    print(f"Le hostname : {donnees_systeme.get("hostname")}")
    print("===============================")

def afficher_cpu(donnees_cpu):
    print("========INFORMATION CPU========")
    print(f"Nombre de coeurs physiques : {donnees_cpu.get("coeurs_physiques")} coeurs")
    print(f"Nombre de coeurs logiques : {donnees_cpu.get("coeurs_logiques")} coeurs")
    print(f"Pourcentage d'utilisation du CPU : {donnees_cpu.get("utilisation")} %")
    print("===============================")

def afficher_ram(donnees_memoire):
    print("========INFORMATION RAM========")
    print(f"Total de mémoire : {octets_vers_go(donnees_memoire.get("total"))}")
    print(f"Disponibilité de la mémoire : {octets_vers_go(donnees_memoire.get("disponible"))}")
    print(f"Pourcentage d'utilisation de la mémoire : {donnees_memoire.get("pourcentage")} %")
    print("===============================")

def afficher_disques(donnees_disques):
    print("======INFORMATION DISQUES======")
    print(f"Point de montage du disque : {donnees_disques.get("point_montage")}")
    print(f"Nombre total du disque : {donnees_disques.get("total")}")
    print(f"Nombre total du disque utilisé : {donnees_disques.get("utilise")}")
    print(f"Pourcentage du disque utilisé : {donnees_disques.get("pourcentage")} %")
    print("===============================")

def afficher_tout():
    print("======INFORMATION GENERAL======")
    donnees_sys = collector.collecter_info_systeme()
    print()
    afficher_systeme(donnees_sys)
    donnees_cpu = collector.collecter_cpu()
    print()
    afficher_cpu(donnees_cpu)
    donnees_ram = collector.collecter_memoire()
    print()
    afficher_ram(donnees_ram)
    donnees_disques = collector.collecter_disques()
    print()
    afficher_disques(donnees_disques)
    print("===============================")

def octets_vers_go(octets):
    GB = str(round(octets/1024**3, 2)) + "GB"
    return(GB)

# toutes_les_donnees = collector.collecter_tout()

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
    afficher_systeme(donnees_sys)
elif choix == "3":
    donnees_cpu = collector.collecter_cpu()
    afficher_cpu(donnees_cpu)
elif choix == "4":
    donnees_ram = collector.collecter_memoire()
    afficher_ram(donnees_ram)
elif choix == "5":
    donnees_disques = collector.collecter_disques()
    afficher_disques(donnees_disques)