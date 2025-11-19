import platform
import psutil

def afficher_sysinfo():
    """Cette fonction permet d'afficher des informations systèmes
    """
    print("========SYSWATCH ALEXIS========")
    print()
    print("======INFORMATION SYSTEME======")
    try:
        print(f"Le système d'explotation est : {platform.system()}")
        print(f"La version du système est : {platform.version()}")
        print(f"L'architecture du système est en : {platform.architecture()}")
        print(f"Le nom de la machine est : {platform.node()}")
        print(f"La version de Python utilisée est : Python {platform.python_version()}")
    except:
        print("Une erreur est survenu")
    print("===============================")

def afficher_cpu():
    """Cette fonction permet d'afficher de information du CPU
    """
    print()
    print("========INFORMATION CPU========")
    try:
        print(f"Le nombre de coeurs physiques du CPU : {psutil.cpu_count(logical=False)} coeurs")
        print(f"Le nombre de coeurs logiques du CPU : {psutil.cpu_count()} coeurs")
        print(f"L'utilisation actuel du CPU est de : {psutil.cpu_percent()} %")
    except:
        print("Une erreur est survenu")
    print("===============================")

def afficher_memoire():
    """Cette fonction permet d'afficher les informations la RAM
    """
    print()
    print("========INFORMATION RAM========")
    try:
        print(f"La mémoire totale est de : {round((psutil.virtual_memory().total)/1024**3, 2)} Go")
        print(f"La mémoire disponible est de : {round((psutil.virtual_memory().free)/1024**3, 2)} Go")
        print(f"Le pourcentage d'utilisation est de : {psutil.virtual_memory().percent} %")
    except:
        print("Une erreur est survenu")
    print("===============================")

def afficher_disque():
    """Cette fonction permet d'afficher les informations des disques
    """
    print()
    print("========INFORMATION DISQUES========")
    nombre_disque = 1
    try:
        for disque in psutil.disk_partitions():
            print(f"Disque {str(nombre_disque)} :")
            print(f"Le point de montage du disque est : {disque.mountpoint}")
            print(f"Le pourcentage d'utilisation du disque est de : {psutil.disk_usage(disque.mountpoint).percent} %")
            nombre_disque = nombre_disque + 1
    except:
        print("Une erreur est survenu")
    print("===============================")

if __name__ == "__main__":
    afficher_sysinfo()
    afficher_cpu()
    afficher_memoire()
    afficher_disque()


# Source pour psutil : https://psutil.readthedocs.io/en/latest/