import csv
import collector

timestamp = collector.collecter_tout()
cpu_info = collector.collecter_cpu()
memoire_info = collector.collecter_memoire()
systeme_info = collector.collecter_info_systeme()
disques_info = collector.collecter_disques()

# colonne = [
#     ["timestamp", "hostname", "cpu_percent", "mem_total_gb", "mem_dispo_gb", "mem_percent", "disk_root_percent"],
#     [timestamp.get("timestamp"), systeme_info.get("hostname"), (str(cpu_info.get("utilisation")) + "%"), (str(round((memoire_info.get("total")/(1024**3)), 2)) + "Gb"), (str(round((memoire_info.get("disponible")/(1024**3)), 2)) + "Gb"), (str(memoire_info.get("pourcentage")) + "%")]
# ]

# def exporter_csv(): 
#     """Cette fonction permet de créer le fichier CSV et d'enregistrer les données à l'intérieur.
#     """
#     with open(r'syswatch\export.csv', "w", newline="", encoding="utf-8") as csv_file:
#         csv_writer = csv.writer(csv_file, delimiter=";")
#         csv_writer.writerows(colonne)

# exporter_csv()

# def exporter_json():
#     print()

donnees = [
    {"timestamp": timestamp.get("timestamp"), "hostname": systeme_info.get("hostname"), "cpu_percent": (str(cpu_info.get("utilisation")) + "%"), "mem_total_gb": (str(round((memoire_info.get("total")/(1024**3)), 2)) + "Gb"), "mem_dispo_gb": (str(round((memoire_info.get("disponible")/(1024**3)), 2)) + "Gb"), "mem_percent": (str(memoire_info.get("pourcentage")) + "%")}
]

def exporter_csv():
    with open("metriques.csv", "w", newline='') as f:
        # DictWriter : écrit dicts en CSV
        colonnes = ["timestamp", "hostname", "cpu_percent", "mem_total_gb", "mem_dispo_gb", "mem_percent", "disk_root_percent"]
        writer = csv.DictWriter(f, fieldnames=colonnes)
        
        writer.writeheader()  # Écrire en-têtes
        writer.writerows(donnees)  # Écrire toutes les lignes

exporter_csv()