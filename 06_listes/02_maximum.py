
# Exercice 6.2 : Maximum d'une liste

from typing import List, TypeVar

## Question 1 

def max_liste(l : List[float]) -> float:
    """Précondition :  len(l) > 0
    Retourne le plus grand élément de la liste L.
    """
    # Maxium partiel
    mx : float = l[0] # cf. précondition
        
    e : float
    for e in l[1:]:
        if e > mx:
            mx = e
            
    return mx         

# Jeu de tests
assert max_liste([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == 9
assert max_liste([-2, -1, -5, -3, -1, -4, -1]) == -1


## Question 2


# Déclaration de la variable de type
T = TypeVar('T')

def nb_occurrences(l : List[T], x : T) -> int:
    """Retourne le nombre d'occurrences de x dans L.
    """
    # Résultat 
    res : int = 0 # (la valeur calculée)

    e : T
    for e in l:
        if e == x:
            res = res + 1
            
    return res


# Jeu de tests
assert nb_occurrences([3, 7, 9, 5.4, 8.9, 9, 8.999, 5], 9) == 2
assert nb_occurrences(["chat", "ours", "chat", "chat", "loup"], "chat")          == 3
assert nb_occurrences(["chat", "ours", "chat", "chat", "loup"], "ou")          == 0


## Question 3

def nb_max(l : List[float]) -> int:
    """Précondition : len(l) > 0
    Retourne le nombre d'occurrences du maximum de l dans l.
    """
    return nb_occurrences(l, max_liste(l))

# Jeu de tests
assert nb_max([3, 7, 9, 5.4, 8.9, 9, 8.999]) == 2
assert nb_max([-2, -1, -5, -3, -1, -4, -1]) == 3

