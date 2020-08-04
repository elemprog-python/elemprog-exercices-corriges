
# Exercice 6.1 : Listes de répétitions

## Question 1

from typing import List, TypeVar
T = TypeVar('T')

def repetition(x : T, k : int) -> List[T]:
    """Précondition : k >= 0
    Retourne la liste composée de k occurrences de x.
    """
    # liste résultat
    lr : List[T] = []
    
    i : int
    for i in range(0, k):
        lr.append(x)
        
    return lr

# Jeu de tests
assert repetition(0, 4) == [0, 0, 0, 0]
assert repetition(4, 0) == []
assert repetition('pom', 5) == ['pom', 'pom', 'pom', 'pom', 'pom']


## Question 2

def repetition_bloc(l : List[T], k : int) -> List[T]:
    """Précondition : k >= 0
    Retourne la liste composée de k répétitions de la liste l.
    """
    # Liste résultat
    lr : List[T] = []
        
    i : int
    for i in range(k):
        lr = lr + l
        
    return lr

# Jeu de tests
assert repetition_bloc([1, 2], 4) == [1, 2, 1, 2, 1, 2, 1, 2]
assert repetition_bloc([4, 5, 2, 3], 0) == []
assert repetition_bloc(['pim', 'pam', 'poum'], 3)         ==  ['pim', 'pam', 'poum',              'pim', 'pam', 'poum',              'pim', 'pam', 'poum']

