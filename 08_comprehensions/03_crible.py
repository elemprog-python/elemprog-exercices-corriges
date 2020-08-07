
# Exercice 8.3 : Crible d'Eratosthène

## Question 1

from typing import List

def liste_non_multiple(n : int, l : List[int]) -> List[int]:
    """Précondition : n != 0
    Renvoie la liste des éléments de L qui ne sont pas multiples de n.
    """
    return [e for e in l if e % n != 0]

# Jeu de tests
assert liste_non_multiple(2,[2,3,4,5]) == [3,5]
assert liste_non_multiple(2,[2,4,6]) == []
assert liste_non_multiple(3,[2,3,4,5]) == [2,4,5]
assert liste_non_multiple(2,[]) == []
assert liste_non_multiple(7,[2,3,4,5]) == [2,3,4,5]


## Question 2

def eratosthene(n : int) -> List[int]:
    """Précondition : n > 1
    Renvoie la liste des nombres premiers inférieurs ou égaux à n.
    """
    
    # Liste de départ
    l : List[int] = [ k for k in range(2,n+1)]
    
    # Liste contenant les nombres premiers
    lp : List[int] = [] 

    # Prochain nombre premier
    p : int =0 # prochain nombre premier
    
    while len(l) > 0:
        p = l[0] # on récupère le prochain nombre premier
        lp.append(p) # on le rajoute à la liste courante
        # puis on calcule les entiers non multiples du nombre premier
        l = liste_non_multiple(p, l)
    return lp

# Jeu de tests
assert eratosthene(10) == [2,3,5,7]
assert eratosthene(2) == [2]
assert eratosthene(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


## Question 3

def liste_facteurs_premiers(n : int) -> List[int]:
    """Précondition : n > 1
    Renvoie la liste des facteurs premiers de n.
    """
    return [e for e in eratosthene(n) if n%e == 0]

# Jeu de tests
assert liste_facteurs_premiers(2) == [2]
assert liste_facteurs_premiers(10) == [2, 5]
assert liste_facteurs_premiers(2*3*7) == [2, 3, 7]
assert liste_facteurs_premiers(2*3*4*7*9) == [2, 3, 7]

