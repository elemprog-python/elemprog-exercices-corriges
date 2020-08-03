
# Exercice 5.1 : Intervalles

## Question 1

def somme_carres(n : int) -> int:
    """Précondition : n >= 0
    Retourne la somme des carrés des entiers inférieurs ou
    égaux à n.
    """
    # Somme à calculer
    s : int = 0 
    
    i : int # Entier courant
    for i in range(1, n + 1):
        s = s + i * i
        
    return s

# Jeu de tests
assert somme_carres(0) == 0
assert somme_carres(1) == 1
assert somme_carres(2) == 5
assert somme_carres(3) == 14
assert somme_carres(4) == 30
assert somme_carres(5) == 55


## Question 2

def produit_cubes(m : int, n : int) -> int:
    """Précondition : (0 <= m) and (m <= n)
    Retourne le produit des cubes des entiers dans l'intervalle [m,n[.
    """
    # Produit à calculer
    p : int = 1
    
    k : int # Entier courant
    for k in range(m, n):
        p = p * k * k * k
        
    return p

# Jeu de tests
assert produit_cubes(1, 4) == 1 * 8 * 27
assert produit_cubes(2, 4) == 216
assert produit_cubes(4, 8) == 592704000
