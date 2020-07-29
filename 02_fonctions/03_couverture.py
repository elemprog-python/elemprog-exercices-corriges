
# Exercice 2.3 : Couverture

## Question 1

def f(n1 : float, n2 : float, n3 : float) -> str:
    """Précondition : n1 != n2 and n2 != n3 and n3 != n1
    retourne un cas parmi 6 selon les valeurs de n1, n2 et n3.
    """
    if n1 < n2 and n2 < n3:
        return 'cas 1'
    elif n1 < n3 and n3 < n2:
        return 'cas 2'
    elif n2 < n1 and n1 < n3:
        return 'cas 3'
    elif n2 < n3 and n3 < n1:
        return 'cas 4'
    elif n3 < n1 and n1 < n2:
        return 'cas 5'
    else:
        return 'cas 6'


# Jeu de tests
assert f(1, 2, 3) == 'cas 1'
assert f(1, 3, 2) == 'cas 2'
assert f(2, 1, 3) == 'cas 3'
assert f(3, 1, 2) == 'cas 4'
assert f(2, 3, 1) == 'cas 5'
assert f(3, 2, 1) == 'cas 6'


## Question 2

def f_bis(n1 : float, n2 : float, n3 : float) -> str:
    """ ... cf ci-dessus ...
    """
    if n1 < n2:
        if n2 < n3:
            return 'cas 1'
        elif n1 < n3:
            return 'cas 2'
        else:
            return 'cas 5'
    elif n1 < n3:
        return 'cas 3'
    elif n2 < n3:
        return 'cas 4'
    else:
        return 'cas 6'

