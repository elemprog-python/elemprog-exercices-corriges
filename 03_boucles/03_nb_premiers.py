
# Exercice 3.3 : Nombres premiers

## Question 1


def divise(n : int, p : int) -> bool:
    """Précondition : n > 0 et p >= 0
    Renvoie True si et seulement si n divise p.
    """    
    return p % n == 0

# Jeu de tests
assert divise(1, 4) == True
assert divise(2, 4) == True
assert divise(3, 4) == False
assert divise(4, 4) == True
assert divise(4, 2) == False
assert divise(17, 123) == False
assert divise(17, 357) == True
assert divise(21, 357) == True


## Question 2


## Réponse

### Sans sortie anticipée :

def est_premier(n : int) -> bool:
    """Précondition: n >= 0
    renvoie True si et seulement si n est premier.
    """
    if n < 2:
        return False
    else:   
        # pas de diviseur trouvé ?
        b : bool = True
        
        # prochain diviseur potentiel
        i : int = 2
    
        while b and (i < n):
            if divise(i, n):
                b = False
            else:
                i = i + 1
            
        return b

# Jeu de tests
assert est_premier(0) == False
assert est_premier(1) == False
assert est_premier(2) == True
assert est_premier(17) == True
assert est_premier(357) == False

### Avec sortie anticipée :

def est_premier2(n : int) -> bool:
    """ ... cf. ci-dessus ...
    """
    if n < 2:
        return False
    else:   
        # prochain diviseur potentiel
        i : int = 2  
        while i < n:
            if divise(i, n):
                return False
            else:
                i = i + 1
            
        return True

# Jeu de tests
assert est_premier2(0) == False
assert est_premier2(1) == False
assert est_premier2(2) == True
assert est_premier2(17) == True
assert est_premier2(357) == False
