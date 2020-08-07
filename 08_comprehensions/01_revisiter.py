
# Exercice 8.1 : Revisiter les listes

## Question 1

from typing import List, TypeVar
T = TypeVar('T')

def repetition(x : T, k : int) -> List[T]:
    """Précondition : k >= 0    
    Retourne la liste composée de k occurrences de x.
    """
    return [x for i in range(1, k + 1)]

# Jeu de tests
assert repetition(0, 4) == [0, 0, 0, 0]
assert repetition(4, 0) == []
assert repetition('pom', 5) == ['pom', 'pom', 'pom', 'pom', 'pom']

## Question 2

def liste_diviseurs(a : int) -> List[int]:
    """Précondition : a > 0
    Retourne la liste des diviseurs de a.
    """ 
    return [i for i in range(1, a + 1) if a % i == 0]

# Jeu de tests
assert liste_diviseurs(2) == [1, 2]
assert liste_diviseurs(12) == [1, 2, 3, 4, 6, 12]
assert liste_diviseurs(25) == [1, 5, 25]

def liste_diviseurs_impairs(a : int) -> List[int]:
    """Précondition : a > 0
    Retourne la liste des diviseurs impairs de a.
    """     
    return [i for i in range(1, a + 1) 
              if (a % i == 0) and (i % 2 == 1)]

# Jeu de tests
assert liste_diviseurs_impairs(2) == [1]
assert liste_diviseurs_impairs(12) == [1, 3]
assert liste_diviseurs_impairs(30) == [1, 3, 5, 15]
assert liste_diviseurs_impairs(15) == [1, 3, 5, 15]

