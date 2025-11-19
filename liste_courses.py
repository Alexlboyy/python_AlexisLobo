def afficher_liste():
    """
    Affiche la liste de courses
    """
    f = open("listes.txt", "r")

    print()
    print("Liste de courses :")
    print(f.read())



def ajouter_article(article_ajouter):
    """
    Ajoute un article à la liste de courses

    Retourne:
        list: La liste modifiée
    """
    with open("listes.txt", "r") as f:
        listes = [ligne.rstrip("\n") for ligne in f]
    
    listes.append(article_ajouter)
    print()
    print("Voici la liste a jour :")
    for element in listes:
        print(element)
    print()
    print("Voulez vous enregister ? oui ou non")
    save = input()
    if save == "oui":
        with open("listes.txt", "w") as f:
            for element in listes:
                f.write(element + "\n")
        print("Votre liste a été mis a jour !")


def retirer_article(test):
    """
    Retire un article de la liste de courses

    Retourne:
        list: La liste modifiée
    """
    with open("listes.txt", "r") as f:
        listes = [ligne.rstrip("\n") for ligne in f]

    for element in listes:
        print(element)
    print()
    print("Veuillez ecire votre article à supprimer:")
    article_supprimer = str(input())
    
    listes.remove(article_supprimer)
    print()
    print("Nouvelle liste :")
    for element in listes:
        print(element)
    print()
    print("Voulez vous enregister ? oui ou non")
    save = input()
    if save == "oui":
        with open("listes.txt", "w") as f:
            for element in listes:
                f.write(element + "\n")
        print("Votre liste a été mis a jour !")


def sauvegarde_liste():
    print()


# Programme principal
def main():
    """Fonction principale du programme"""

    print("Bienvenue dans le gestionnaire de liste de courses !")
    print()

    # Choix
    print("Veuillez slectionner votre choix :")
    print("1 - Visualiser la liste") 
    print("2 - Ajouter un article") 
    print("3 - Supprimer un article")
    print("4 - Sauvegarder la liste")
    print()
    print("Votre choix :")
    choix = int(input())

    if choix == 1:
        afficher_liste()
    elif choix == 2:
        print("Veuillez ecire votre article :")
        article_ajouter = str(input())
        ajouter_article(article_ajouter)
    elif choix == 3:
        retirer_article()
    elif choix == 4:
        sauvegarde_liste()
    else:
        print()
        print("Il y a que 4 choix")


main()