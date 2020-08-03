
# Exercice 4.1. : Retour sur la factorielle (corrigé)

def factorielle(n : int) -> int:
    """Précondition : n >= 0
    Retourne le produit factoriel n!
    """
    # Rang
    k : int = 1   
    
    # Factorielle au rang k
    f : int = 1
    
    while k <= n:
        f = f * k
        k = k + 1
        
    return f

## Question 1

## Réponse

# Jeu de tests
assert factorielle(0) == 1
assert factorielle(1) == 1
assert factorielle(2) == 2
assert factorielle(3) == 6
assert factorielle(4) == 24
assert factorielle(5) == 120
assert factorielle(6) == 720


## Question 2

## Question 3 : à propos de la correction

