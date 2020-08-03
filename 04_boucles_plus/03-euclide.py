
# Exercice 4.3 : Retour sur l'algorithme d'Euclide

def pgcd(a : int, b : int) -> int:
    """Précondition: b > 0 et a >= b
    Retourne le plus grand commun diviseur de a et b.""" 
    
    # Quotient
    q : int = a
        
    # Diviseur
    r : int = b
        
    # Variable temporaire
    temp : int = 0
        
    while r != 0:
        temp = q % r
        q = r
        r = temp
        
    return q
