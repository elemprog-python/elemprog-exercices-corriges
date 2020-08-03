
# Exercice 5.2 : Fonction mystère

def nb_chiffres(s : str) -> int:
    """Renvoie le nombre de chiffres de s.
    """
    nb : int = 0
    
    c : str
    for c in s:
        if c >= '0' and c <= '9':
            nb = nb + 1
            
    return nb

# Jeu de tests
assert nb_chiffres('bonjour') == 0
assert nb_chiffres('12345') == 5
assert nb_chiffres('0') == 1
assert nb_chiffres('') == 0
assert nb_chiffres('a1b2c3ed4') == 4

