
# Exercice 8.2 : Lettres de l'alphabet

from typing import List

## Question 1

def alphabet() -> List[str]:
    """Retourne la liste des 26 lettres de l'alphabet.
    """
    return [chr(i) for i in range(ord('a'), ord('z') + 1)]


# Jeu des tests
assert alphabet() == ['a','b','c','d','e','f','g','h','i','j','k','l','m',                      'n','o','p','q','r','s','t','u','v','w','x','y','z']


## Question 2

def est_voyelle(c : str) -> bool:
    """Précondition : len(c) == 1
    Retourne True si c est une voyelle, ou False sinon.
    """
    return (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u')  or (c == 'y')


# Jeu de tests
assert est_voyelle('a') == True
assert est_voyelle('c') == False
assert est_voyelle('e') == True
assert est_voyelle('g') == False


## Question 3

# [c for c in alphabet() if est_voyelle(c)]

## Question 4

# [c for c in alphabet() if not est_voyelle(c)]

