import platform
import psutil
from datetime import datetime

def collecter_info_systeme():
    """Cette fonction permet de stocker les informations du systeme dans un Dictionnaire.

    Returns:
        Dictionnaire: Contenant l'OS, la version, l'architecture et le hostname.
    """
    systeme = {
        "os": platform.system(),
        "version": platform.version(),
        "architecture": platform.architecture(),
        "hostname": platform.node()
    }
    return systeme

def collecter_cpu():
    """Cette fonction permet de stocker les informations du CPU dans un Dictionnaire.

    Returns:
        Dictionnaire: Contenant le nombre de coeur physique, le nombre de coeurs logiques et le pourcentage d'utilisation.
    """
    cpu = {
        "coeurs_physiques": psutil.cpu_count(logical=False),
        "coeurs_logiques": psutil.cpu_count(),
        "utilisation": psutil.cpu_percent(interval=1)
    }
    return cpu

def collecter_memoire():
    """Cette fonction permet de stocker les informations de la RAM dans un Dictionnaire.

    Returns:
        Dictionnaire: Contenant le nombre total de la RAM, le nombre disponible de RAM et le pourcentage d'utilisation.
    """
    memoire = {
        "total": psutil.virtual_memory().total,
        "disponible": psutil.virtual_memory().free,
        "pourcentage": psutil.virtual_memory().percent
    }
    return memoire

def collecter_disques():
    """Cette fonction permet de stocker les informations des disques dans un Dictionnaire.

    Returns:
        Dictionnaire: Contenant le point de montage, le total du disque, l'utilisation du disque et le pourcentage.
    """
    liste_disques = []
    try:
        for disque in psutil.disk_partitions():
            liste_disques.append({"point_montage": disque.mountpoint, "total": psutil.disk_usage(disque.mountpoint).total, "utilise": psutil.disk_usage(disque.mountpoint).used, "pourcentage": psutil.disk_usage(disque.mountpoint).percent})
    except:
        print("Il y a eu un souci")
    return liste_disques

def collecter_tout():
    """Cette fonction permet d'appeller toutes les fonctions.

    Returns:
        Dictionnaire: Contenant toutes les métriques structurées
    """
    info_systeme = collecter_info_systeme()
    info_cpu = collecter_cpu()
    info_memoire = collecter_memoire()
    info_disque = collecter_disques()

    tout = {
        "info_systeme": info_systeme,
        "versinfo_cpuion": info_cpu,
        "info_memoire": info_memoire,
        "info_disque": info_disque,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    return tout

collecter_tout()