
# Exercice 5.3 : Palindromes

## Question 1

def est_palindrome(s : str) -> bool:
    """Retourne True si et seulement si s est un palindrome.
    """
    i : int # Indice courant
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False  # différence trouvée
        
    # La boucle s'est terminée sans qu'on trouve de différence 
    # entre la lecture dans un sens et dans l'autre
    return True

# Jeu de tests
assert est_palindrome('') == True
assert est_palindrome('je ne suis pas un palindrome') == False
assert est_palindrome('aaaa') == True
assert est_palindrome('aba') == True
assert est_palindrome('amanaplanacanalpanama') == True


# Variante plus efficace (contrôle que la moitié de gauche correspond à la moité de droite)

def est_palindrome2(s : str) -> bool:
    """ ... cf. ci-dessus ...
    """
    i : int
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
        
    return True

# Jeu de tests
assert est_palindrome2('') == True
assert est_palindrome2('je ne suis pas un palindrome') == False
assert est_palindrome2('aaaa') == True
assert est_palindrome2('aba') == True
assert est_palindrome2('amanaplanacanalpanama') == True

# Une variante de cette dernière fonction qui exploite l'utilisation des entiers négatifs pour l'accès aux éléments d'une chaîne de caractères (vu en cours) :

def est_palindrome3(s : str) -> bool:
    """ ... cf. ci-dessus ...
    """
    i : int
    for i in range(0,len(s)//2):
        if s[i] != s[-i-1]:
            return False
        
    return True

# Jeu de tests
assert est_palindrome3('') == True
assert est_palindrome3('je ne suis pas un palindrome') == False
assert est_palindrome3('aaaa') == True
assert est_palindrome3('aba') == True
assert est_palindrome3('amanaplanacanalpanama') == True

## Question 2

def miroir(s : str) -> str:
    """Retourne le palindrome miroir de la chaîne s.
    """
    # Chaîne inversée
    r : str = ''  
    
    ch : str  # Caractère courant
    for ch in s:
        r = ch + r
        
    return s + r

# Jeu de tests
assert miroir('abc') == 'abccba'
assert est_palindrome(miroir('abc'))
assert est_palindrome(miroir('amanaplanacanal'))
assert est_palindrome(miroir('do-re-mi-fa-sol'))


# Variante exploitant les indices négatifs dans les chaînes de caractères :

def miroir2(s : str) -> str:
    """ ... cf. ci-dessus ...
    """
    # Chaîne inversée
    r : str = ''
    
    i : int  # Position du caractère courant
    for i in range(1,len(s)+1):
        r = r + s[-i]
        
    return s + r

# Jeu de tests
assert miroir2('abc') == 'abccba'
assert est_palindrome(miroir2('abc'))
assert est_palindrome(miroir2('amanaplanacanal'))
assert est_palindrome(miroir2('do-re-mi-fa-sol'))
