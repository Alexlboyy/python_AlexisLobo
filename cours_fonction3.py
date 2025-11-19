def est_mot_de_passe_valide(mdp):
    """
    La fonction permet de vérifier si le mot de passe rentré est valide
    """
    nombre_caractere = len(mdp)
    if nombre_caractere >= 8:
        if any(char.isupper() for char in mdp):
            if any(c.isdigit() for c in mdp):
                print("Le mot de passe est valide")
    else:
        print("Le mot de passe est invalide")


est_mot_de_passe_valide("Teeeeest1")