
# Exercice 7.1 : Nombres complexes


## Question 1

from typing import Tuple
Complexe = Tuple[float, float]

def partie_reelle(c : Complexe) -> float:
    """Renvoie la partie réelle du nombre complexe c.
    """
    re, _ = c    
    return re

# Jeu de tests
assert partie_reelle((2.0,3.0)) == 2.0
assert partie_reelle((0.0,1.0)) == 0.0
assert partie_reelle((4.0,0.0)) == 4.0

def partie_imaginaire(c : Complexe) -> float:
    """Renvoie la partie imaginaire du nombre complexe c.
    """
    _, im = c
    return im

# Jeu de tests
assert partie_imaginaire((2.0,3.0)) == 3.0
assert partie_imaginaire((0.0,1.0)) == 1.0
assert partie_imaginaire((4.0,0.0)) == 0.0


## Question 2

def addition_complexe(c1 : Complexe, c2 : Complexe) -> Complexe:
    """Renvoie le nombre complexe correspondant à c1 + c2. 
    """  
    re1, im1 = c1
    re2, im2 = c2
    return (re1 + re2 , im1 + im2)

# Jeu de tests
assert addition_complexe((1.0, 0.0), (0.0, 1.0)) == (1.0, 1.0)
assert addition_complexe((2.0, 3.0), (0.0, 1.0)) == (2.0, 4.0)


## Question 3

def produit_complexe(c1 : Complexe, c2 : Complexe) -> Complexe:
    """Renvoie le nombre complexe correspondant à c1 * c2. 
    """
    re1, im1 = c1
    re2, im2 = c2
    return (re1*re2 - im1 * im2, re1 * im2 + im1 * re2)

# Jeu de tests
assert produit_complexe((0.0, 0.0), (1.0, 1.0)) == (0.0, 0.0)
assert produit_complexe((0.0, 1.0), (0.0, 1.0)) == (-1.0, 0.0)

