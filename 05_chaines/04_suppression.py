
# Exercice 5.4 : Suppressions

## Question 1

def suppression_debut(c : str, s : str) -> str:
    """Précondition : len(c) == 1
    Retourne la chaîne s sans la première occurrence du caractère c.
    """
    # Indicateur si la première occurrence 
    # de c a été vue ou non
    premiere_trouvee : bool = False
        
    # Résultat
    res : str = ''
    
    d : str
    for d in s:
        if d != c:
            res = res + d
        elif  not premiere_trouvee:
            premiere_trouvee = True
        else:
            res = res + d

    return res

# Jeu de tests
assert suppression_debut('a', '') == ''
assert suppression_debut('a', 'aaaaa') == 'aaaa'
assert suppression_debut('p', 'le papa noel') == 'le apa noel'
assert suppression_debut('a', 'bbbbb') == 'bbbbb'


## Question 2

def suppression_derniere(c : str, s : str) -> str:
    """Précondition : len(c) == 1
    Retourne la chaîne s sans la dernière occurrence du caractère c.
    """
    
    # Indicateur si la dernière occurrence 
    # de c a été vue ou non
    derniere_trouvee = False 
    
    # Résultat
    res : str = ''

    # Indice du caractère courant, en partant de la fin
    i : int = len(s) - 1
    while i >= 0:
        if s[i] != c:
            res = s[i] + res
        elif  not derniere_trouvee:
            derniere_trouvee = True
        else:
            res = s[i] + res
            
        i = i - 1
        
    return res

# Jeu de tests
assert suppression_derniere('a','') == ''
assert suppression_derniere('a', 'aaaaa') == 'aaaa'
assert suppression_derniere('p', 'le papa noel') == 'le paa noel'
assert suppression_derniere('a', 'bbbbb') == 'bbbbb'

