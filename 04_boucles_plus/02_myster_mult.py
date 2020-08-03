
# Exercice 4.2 : Fonction mystère

def mult(n : int, m : int) -> int:
    """Précondition : (n >= 0) and (m >= 0)
    Renvoie la multiplication de n par m.
    """
    a : int = n
    b : int = 0
    c : int = 0
    
    while a > 0:
        while a > 0:
            a = a - 1
            b = b + 1
            
        a = b - 1
        b = 0
        c = c + m
        
    return c


# Jeu de tests
assert mult(3, 4) == 12
assert mult(2, 1) == 2
assert mult(3, 10) == 30
assert mult(8, 0) == 0
assert mult(0, 5) == 0
assert mult(6, 7) == 42
assert mult(9, 99) == 891

