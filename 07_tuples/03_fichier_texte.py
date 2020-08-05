
# Exercice 7.3 : Fichiers texte et système de facturation

from typing import List, Tuple

## Chargement d'un fichier texte en Python

def chargement_fichier(nom_fichier : str) -> List[str]:
    """Précondition : nom_fichier est le nom d'un fichier texte existant
    Retourne le contenu du fichier texte identifié par nom_fichier
    sous la forme d'une liste de lignes de texte.
    """
    # Lignes contenues dans le fichier
    l1 : List[str] = []  

    # Lignes sans retour charriot
    l2 : List[str] = [] 

    with open(nom_fichier, 'r') as f:  # 'r' pour read (lecture)
        l1 = f.readlines() # opération de lecture de lignes

    # suppression des retours charriots
    ligne : str
    for ligne in l1:
        if ligne != '' and ligne[-1] == '\n':
            l2.append(ligne[:-1])
        else:
            l2.append(ligne)

    return l2

def sauvegarde_fichier(nom_fichier : str, Contenu : List[str]) -> None:
    """Précondition : nom_fichier est un nom correct de fichier
    Sauvegarde le Contenu comme lignes de texte dans le
    fichier identifié par nom_fichier
    Attention : si le fichier existe déjà son contenu sera
    effacé.
    """
    with open(nom_fichier, 'w') as f: # 'w' pour write (écriture)
        ligne : str
        for ligne in Contenu:
            f.write(ligne) # écriture de la ligne
            f.write('\n')  # ajout d'un retour charriot


    return None


## Question 1

sauvegarde_fichier("haiku.txt", ["Papillon voltige"
                                     ,"Dans un monde"
                                     , "Sans espoir."
                                     , "(Kobayashi Issa)"])


## Question 2

def decoupage_mots(phrase : str) -> List[str]:
    """Précondition : phrase est composée de mots séparés par des espaces
    Renvoie la liste des mots de la phrase.
    """
    # La liste des mots
    lmots : List[str] = []
    
    # Le mot courant
    mot : str = ""
        
    ch : str # Caractère courant dans la phrase
    for ch in phrase:
        if ch == ' ':
            if mot != "":
                lmots.append(mot)
                mot = ""
        else:
            mot = mot + ch
            
    if mot != "":
        lmots.append(mot)
            
    return lmots

# Jeu de tests
assert decoupage_mots("Dans un monde") == ["Dans", "un", "monde"]
assert decoupage_mots("Bonjour    Hello     ") == ["Bonjour", "Hello"]
assert decoupage_mots("") == []


## Question 3

sauvegarde_fichier("commande.txt", ["Lait  12   2.0"
                                         , "Thé    8   4.5"
                                         , "Tomate 6   1.5"
                                         , "Fromage 9  8.5"])

def lecture_produit(ligne : str) -> Tuple[str, int, float]:
    """Précondition : la ligne de texte décrit une commande de produit.
    Renvoie la commande produit (nom, quantité, prix unitaire).
    """
    lmots : List[str] = decoupage_mots(ligne)
    nom_produit : str = lmots[0]
    quantite : int = int(lmots[1])
    prix_unitaire : float = float(lmots[2])
    return (nom_produit, quantite, prix_unitaire)

# Jeu de tests
assert lecture_produit("Lait  12 2.0") == ('Lait', 12, 2.0)
assert lecture_produit("Tomate 6   1.5") == ('Tomate', 6, 1.5)


## Question 4

def lecture_commande(commande : List[str]) -> List[Tuple[str, int, float]]:
    """Précondition : la commande est dans le bon format
    Renvoie la liste des produits commandés.
    """
    lproduits : List[Tuple[str, int, float]] = []
    
    produit : str
    for produit in commande:
        lproduits.append(lecture_produit(produit))
        
    return lproduits


# Voici l'expression cherchée :
lecture_commande(chargement_fichier("commande.txt"))


## Question 5

def gen_facture(lproduits : List[Tuple[str, int, float]]) -> List[str]:
    """Précondition : lproduits est une liste de produits commandés.
    Renvoie une facture éditée sous la forme d'une liste
    de lignes de texte.
    """
    lfacture : List[str] = ["Produit  Prix",
                            "-------  ----"]
    
    # Prix total
    total_ht : float = 0.0
        
    nom_produit : str
    quantite : int
    prix_unitaire : float
    for (nom_produit, quantite, prix_unitaire) in lproduits:
        lfacture.append(nom_produit + "  " + str(quantite * prix_unitaire))
        total_ht = total_ht + quantite * prix_unitaire
        
    lfacture.append("")  # ajout d'une ligne vide
    lfacture.append("Total_HT    " + str(total_ht))
    
    lfacture.append("TVA_20%     " + str(total_ht * 20.0 / 100.0))
    lfacture.append("Total_TTC   " + str(total_ht + (total_ht * 20.0 / 100.0)))
    
    return lfacture


# L'expression cherchée est la suivante :
sauvegarde_fichier('facture.txt', 
                       gen_facture(lecture_commande(
                                      chargement_fichier('commande.txt'))))

