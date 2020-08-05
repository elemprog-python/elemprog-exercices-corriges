
# Exercice 7.2 : Nombre d'occurrences du maximum

## Question


from typing import List, Tuple

def nb_de_max(l : List[float]) -> Tuple[float, int]:
    """Précondition : len(l) > 0
    Renvoie le couple (m,n) dans lequel m est le maxumum de l
    et n le nombre d'occurrences de m dans l.
    """ 
    # Candidat maximum
    m : float = l[0]
        
    # Nombre de fois où m est apparu dans l
    n : int = 1 
    
    # x : float
    for x in l[1:]:
        if x > m : # on a trouvé un nombre supérieur au maximum courant
            m = x
            n = 1
        elif x == m : # on a trouvé une nouvelle occurrence du maximum courant
            n = n + 1
        
    return (m, n)

# Jeu de tests
assert nb_de_max([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == (9, 2)
assert nb_de_max([-2, -1, -5, -3, -1, -4, -1]) == (-1, 3)

