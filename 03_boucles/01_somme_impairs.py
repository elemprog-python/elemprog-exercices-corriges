
# Exercice 3.1 : Somme des impairs

## Question 1

def somme_impairs_inf(n : int) -> int:
    """Précondition: n >= 0
    Renvoie la somme de tous les entiers naturels impairs 
    inférieurs ou égaux à n.
    """
    # somme calculée
    s : int = 0
    
    # impair courant  (1 est le premier impair)
    i : int = 1
    
    while i <= n:
        s =  s + i
        i = i + 2
    
    return s

# Jeu de test
assert somme_impairs_inf(0) == 0
assert somme_impairs_inf(1) == 1
assert somme_impairs_inf(2) == 1
assert somme_impairs_inf(3) == 4
assert somme_impairs_inf(4) == 4
assert somme_impairs_inf(5) == 9
assert somme_impairs_inf(8) == 16


## Question 2

def somme_premiers_impairs(n : int) -> int:
    """Précondition : n > 0
    Renvoie la somme des n premiers entiers impairs.
    """
    # somme calculée
    s : int = 0
    
    # compteur
    i : int = 1
    
    # impair courant (1 est le premier impair)
    imp : int = 1  
    
    while i <= n:
        s = s + imp
        imp = imp + 2
        i = i + 1
        
    return s


# Jeu de tests
assert somme_premiers_impairs(1) == 1 ** 2
assert somme_premiers_impairs(2) == 2 ** 2
assert somme_premiers_impairs(3) == 3 ** 2
assert somme_premiers_impairs(4) == 4 ** 2
assert somme_premiers_impairs(5) == 5 ** 2
assert somme_premiers_impairs(8) == 8 ** 2
assert somme_premiers_impairs(9) == 9 ** 2
