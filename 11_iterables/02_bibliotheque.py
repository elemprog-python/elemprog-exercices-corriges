
# Exercice 11.2 : Gestion de bibliothèque

from typing import Set, Dict, Tuple

LivresBD : Dict[str,Tuple[str,int]]
LivresBD = {'Les misérables':('Victor Hugo', 5),
            'Le dernier des Mohicans':('James F. Cooper', 0),
            'Un animal doué de raison': ('Robert Merle', 6),
            'Le grand Meaulnes':('Alain Fournier', 1), 
            'Notre-dame de Paris':('Victor Hugo', 4),
            'Les comtemplations':('Victor Hugo', 0) }

## Question 1

def auteurs(livres : Dict[str,Tuple[str,int]]) -> Set[str]:
    """Retourne l'ensemble des noms d'auteurs de la base de Livres.
    """
    return { auteur for (_, (auteur, _)) in livres.items() }

# Jeu de tests
assert auteurs(LivresBD) == { 'Victor Hugo', 'James F. Cooper', 
                             'Robert Merle', 'Alain Fournier'}


## Question 2

def titres_empruntables(livres : Dict[str,Tuple[str,int]]) -> Set[str]:
    """Retourne l'ensemble des titres empruntables dans la base de Livres.
    """
    return { titre for (titre, (_, stock)) in livres.items()
                       if stock > 0 }


# Jeu de tests
assert titres_empruntables(LivresBD) == {'Le grand Meaulnes',
                                         'Les misérables',
                                         'Notre-dame de Paris',
                                         'Un animal doué de raison'}

## Question 3

def titres_auteur(auteur : str, livres : Dict[str,Tuple[str,int]])         -> Set[str]:
    """Retourne l'ensemble des titres de l'auteur spécifié
    dans la base des livres.
    """
    return { titre for (titre,(auteur_livre,_)) in livres.items() 
             if auteur == auteur_livre }

# Jeu de tests
assert titres_auteur('Victor Hugo', LivresBD)     == {'Les comtemplations','Les misérables','Notre-dame de Paris'}

assert titres_auteur('Robert Merle', LivresBD)     == {'Un animal doué de raison'}

assert titres_auteur('Gaston Leroux', LivresBD) == set()

