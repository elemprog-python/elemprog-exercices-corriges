
# Exercice 6.4 : Fonction mystère


## Question 3

from typing import List

def est_croissante(l : List[float]) -> bool:
    """Retourne True si l est rangée en ordre strictement croissant
    et False sinon.
    """
    if (len(l) == 0) or (len(l) == 1):
        return True
    else:
        i : int
        for i in range(len(l) - 1):
            if l[i] >= l[i + 1]:
                return False
    return True

# Jeu de tests
assert est_croissante([1, 3, 4, 7, 8, 11, 13]) == True
assert est_croissante([1, 3, 4, 7, 8, 11, 9]) == False
assert est_croissante([1, 3, 4, 2, 5, 6]) == False
assert est_croissante([1, 3, 3, 4, 5, 6]) == False
assert est_croissante([]) == True
assert est_croissante([5]) == True


## Question 4

def est_croissante2(l : List[float]) -> bool:
    """ ... cf. ci-dessus ... 
    """
    # Résultat
    b : bool = True
    # Indice courant    
    i : int = 0 
    while (i < len(l) - 1) and b:
        b = l[i] < l[i + 1]
        i = i + 1            
    return b

# Jeu de tests
assert est_croissante2([1, 3, 4, 7, 8, 11, 13]) == True
assert est_croissante2([1, 3, 4, 7, 8, 11, 9]) == False
assert est_croissante2([1, 3, 4, 2, 5, 6]) == False
assert est_croissante2([1, 3, 3, 4, 5, 6]) == False
assert est_croissante2([]) == True
assert est_croissante2([5]) == True
