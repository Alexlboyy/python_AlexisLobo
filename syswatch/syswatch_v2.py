import collector

def afficher_systeme(systeme):
    print("======INFORMATION SYSTEME======")
    collector.collecter_info_systeme()

def afficher_cpu(cpu):
    print("========INFORMATION CPU========")
    collector.collecter_cpu()

def afficher_ram(memoire):
    print("========INFORMATION RAM========")
    collector.collecter_memoire()

def afficher_disques(liste_disques):
    print("======INFORMATION DISQUES======")
    collector.collecter_disques()

def octets_vers_go(octets):
    GB = str(round(octets/1024**3, 2)) + "GB"
    return(GB)

collector.collecter_tout()