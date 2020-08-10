
# Exercice 9.2 : Répétitions dans les listes

## Question 1

from typing import List, Set, TypeVar
T = TypeVar('T')

def repetes(l : List[T]) -> Set[T]:
    """Retourne l'ensemble des éléments répétés dans L.
    """
    # Eléments déjà vus
    vus : Set[T] = set()  # éléments déjà vus
    
    # Ensemble résultat
    ens : Set[T] = set()
    
    e : T
    for e in l:
        if e in vus:  # déjà vu ?
            ens.add(e) # répétition
        else:
            vus.add(e) # c'est tout vu !
        
    return ens

# Jeu de tests
assert repetes([1, 2, 23, 9, 2, 23, 6, 2, 9]) == {2, 9, 23}
assert repetes([1, 2, 3, 4]) == set()
assert repetes(['bonjour', 'ça', 'ça', 'va', '?']) == {'ça'}


## Question 2

def sans_repetes(l : List[T]) -> List[T]:
    """Retourne la liste des éléments de l sans
    leur(s) répétition(s)."""
    # Eléments déjà vus
    vus : Set[T] = set()
        
    # Liste résultat
    lr : List[T] = []
    
    e : T
    for e in l:
        if e not in vus:
            lr.append(e)
            vus.add(e)
            
    return lr

# Jeu de tests
assert sans_repetes([1, 2, 23, 9, 2, 23, 6, 2, 9]) == [1, 2, 23, 9, 6]
assert sans_repetes([1, 2, 3, 4]) == [1, 2, 3, 4]
assert sans_repetes([2, 1, 2, 1, 2, 1, 2]) == [2, 1]
assert sans_repetes(['bonjour', 'ça', 'ça', 'va' , '?'])        == ['bonjour', 'ça', 'va', '?']


## Question 3

def uniques(l : List[T]) -> Set[T]:
    """Retourne l'ensemble des éléments apparaissant
    une seule fois dans l."""
    
    # Eléments vus au moins une fois
    unefois : Set[T] = set()   
        
    # Eléments vus plus d'une fois
    trop : Set[T] = set() 
    
    e : T
    for e in l:
        if e in unefois:
            # vu au moins 2 fois
            trop.add(e)
        else:
            # vu pour la première fois
            unefois.add(e)
            
    return unefois - trop

# Jeu de tests
assert uniques([1, 2, 23, 9, 2, 23, 6, 2, 1]) == {6, 9}
assert uniques([1, 2, 1, 1]) == {2}
assert uniques([1, 2, 1, 2, 1]) == set()

