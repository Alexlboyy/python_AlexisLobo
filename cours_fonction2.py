def calculer_prix_ttc(prix, TVA = 20):
    """
    La fonction permet de calculer un prix HT en TTC avec 20% de TVA
    """
    prix_ttc = prix * (1 + TVA/100)
    prix_rond = round(prix_ttc, 2)
    print(prix_rond)

calculer_prix_ttc(100.432)