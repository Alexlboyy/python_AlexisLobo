from datetime import datetime

def saluer_personne(nom,heure):
    """
    La fonction permet de comparer l'heure et d'afficher le bon mot en sortie.
    """
    if heure >= 6 and heure <= 12:
        print("Bonjour " + nom)
    elif heure >= 12 and heure <= 18:
        print("Bon après-midi " + nom)
    elif heure >= 18 and heure <= 24:
        print("Bonsoir " + nom)
    else :
        print("Bonne nuit mon choubidou " + nom)

saluer_personne("Alexis",1)