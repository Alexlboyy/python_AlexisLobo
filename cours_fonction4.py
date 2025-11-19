def afficher_menu():
    """menu
    """
    print("selectionner ...")
    choix = input()

def count_article(courses):
    return f"nombre d'artciles {len(courses)}"

def afficher_articles(courses):
    """_summary_

    Args:
        courses (_type_): _description_
    """
    if len(courses) == 0:
        return
    
    for i, article in enumerate(courses, 1):
        print(f"{i}. {article}")
    
def ajouter_article(courses, article):
    """ajouter un article a la liste de course

    Args:
        courses (_type_): _description_
        article (_type_): _description_
    Returns:
        La nouvelle liste
    """
    return courses.append(article)

def retirer_article(courses, article):
    """retirer un article a la liste de course

    Args:
        courses (_type_): _description_
        article (_type_): _description_
    Returns:
        La nouvelle liste
    """
    if article in courses:
        courses.remove(article)
    else :
        print(f"{article} pas dans la liste")

def main():
    """_summary_
    """
    listes_courses = []
    while True:
        afficher_menu()

