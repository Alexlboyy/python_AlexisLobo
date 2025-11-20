import csv
import json
import collector
import time
import os

timestamp = collector.collecter_tout()
cpu_info = collector.collecter_cpu()
memoire_info = collector.collecter_memoire()
systeme_info = collector.collecter_info_systeme()
disques_info = collector.collecter_disques()


def enregistrer_disque():
    premier_disque = disques_info[0]
    disque_pourcentage = premier_disque.get("pourcentage")
    return disque_pourcentage

donnees = [
    {"timestamp": timestamp.get("timestamp"), "hostname": systeme_info.get("hostname"), "cpu_percent": (str(cpu_info.get("utilisation")) + "%"), "mem_total_gb": (str(round((memoire_info.get("total")/(1024**3)), 2)) + "Gb"), "mem_dispo_gb": (str(round((memoire_info.get("disponible")/(1024**3)), 2)) + "Gb"), "mem_percent": (str(memoire_info.get("pourcentage")) + "%"), "disk_root_percent": (str(enregistrer_disque()) + "%")}
]

def exporter_csv(metriques, fichier="syswatch\export.csv"):
    """Cette fonction permet d'exporter en .CSV tout les données.

    Args:
        metriques (_type_, optional): C'est toutes les données regrouper nécessaire pour l'export en csv. Defaults to donnees.
        fichier (str, optional): C'est le chemin du fichier ou il va etre enregistrer. Defaults to "syswatch\export.csv".
    """
    if os.path.isfile(fichier):
        try:
            with open(fichier, "a", newline='') as f:
                # DictWriter : écrit dicts en CSV
                colonnes = ["timestamp", "hostname", "cpu_percent", "mem_total_gb", "mem_dispo_gb", "mem_percent", "disk_root_percent"]
                writer = csv.DictWriter(f, fieldnames=colonnes, delimiter=";")
                
                writer.writeheader()  # Écrire en-têtes
                writer.writerows(metriques)  # Écrire toutes les lignes
        except PermissionError:
            print("Une erreur de permission est survenue")
    else:
        try:
            with open(fichier, "w", newline='') as f:
                # DictWriter : écrit dicts en CSV
                # colonnes = ["timestamp", "hostname", "cpu_percent", "mem_total_gb", "mem_dispo_gb", "mem_percent", "disk_root_percent"]
                # writer = csv.DictWriter(f, fieldnames=colonnes, delimiter=";")
                
                # writer.writeheader()  # Écrire en-têtes
                writer.writerows(metriques)  # Écrire toutes les lignes
        except PermissionError:
            print("Une erreur de permission est survenue")

exporter_csv(donnees)


def exporter_json(metriques, fichier="syswatch\sauvegarde.json"):
    """Cette fonction permet d'exporter en .JSON toutes les données.

    Args:
        metriques (_type_): C'est toutes les données regrouper nécessaire pour l'export en csv
        fichier (str, optional): C'est le chemin du fichier ou il va etre enregistrer. Defaults to "syswatch\sauvegarde.json".
    """
    try:
        with open(fichier, 'w') as fichier:
            json.dump(metriques, fichier, indent=2)
    except PermissionError:
        print("Une erreur de permission est survenue")

exporter_json(donnees)

# def collecter_en_continu(intervalle, nombre):
#     # fois = 0
#     while True:
#         print(donnees)
#         exporter_csv(donnees, r"syswatch\export.csv")
#         time.sleep(intervalle)

# collecter_en_continu(1, 2)

