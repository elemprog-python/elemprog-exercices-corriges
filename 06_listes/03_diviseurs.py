
# Exercice 6.3 : Liste de diviseurs

from typing import List

## Question 1

def liste_diviseurs(a : int) -> List[int]:
    """Précondition : a > 0
    Retourne la liste des diviseurs de a.""" 
    
    # liste résultat
    lr : List[int] = []
        
    i : int
    for i in range(1, a + 1):
        if a % i == 0:
            lr.append(i)
    return lr

# Jeu de tests
assert liste_diviseurs(2) == [1, 2]
assert liste_diviseurs(12) == [1, 2, 3, 4, 6, 12]
assert liste_diviseurs(25) == [1, 5, 25]


## Question 2

def liste_diviseurs_impairs(a : int) -> List[int]:
    """Précondition : a > 0
    Retourne la liste des diviseurs impairs de a.
    """ 
    # Liste résultat
    lr : List[int] = []
    
    # Candidat diviseur impair
    i : int = 1 # 1 est le plus petit candidat possible.
    
    while i < a + 1:
        if a % i == 0:
            lr.append(i)
            
        i = i + 2
            
    return lr

# Jeu de tests
assert liste_diviseurs_impairs(2) == [1]
assert liste_diviseurs_impairs(12) == [1, 3]
assert liste_diviseurs_impairs(30) == [1, 3, 5, 15]
assert liste_diviseurs_impairs(15) == [1, 3, 5, 15]

