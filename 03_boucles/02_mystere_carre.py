
# Exercice 3.2 : Fonction mystère

def somme_carres(m : int, n : int) -> int:
    """Précondition: m <= n
    Retourne la somme des carrés des entiers  dans l'invervalle [m;n].
    """
    
    # la somme des carrés
    s : int = 0   

    # entier courant dans l'intervalle
    i : int = m
    
    while i <= n:
        s = s + i * i
        i = i + 1
        
    return s

# Jeu de tests
assert somme_carres(1, 5) == 55
assert somme_carres(2, 5) == 54
assert somme_carres(3, 5) == 50
assert somme_carres(4, 5) == 41
assert somme_carres(5, 5) == 25
assert somme_carres(3, 6) == 86
assert somme_carres(-4, 0) == 30

