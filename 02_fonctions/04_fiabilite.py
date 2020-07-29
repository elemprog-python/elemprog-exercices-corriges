
# Exercice 2.4 : Mesures fiables (corrigé)

## Question 1

def egal_eps(x1 : float, x2 : float, epsilon : float) -> bool:
    """Précondition : epsilon > 0
    renvoie True quand x1 et x2 sont égaux à epsilon près.
    """
    return epsilon > abs (x1 - x2) 

# Jeu de tests
assert egal_eps(4,5,1.1) == True
assert egal_eps(5,4,1.1) == True
assert egal_eps(-4,-5,1.1) == True
assert egal_eps(-5,-4,1.1) == True
assert egal_eps(3,5,1.1) == False
assert egal_eps(5,3,1.1) == False
assert egal_eps(-3,-5,1.1) == False
assert egal_eps(-5,-3,1.1)== False
assert egal_eps(-1,0,1.1) == True
assert egal_eps(0,-1,1.1) == True
assert egal_eps(-1,1,1.1) == False
assert egal_eps(1,-1,1.1) == False


## Question 2

def fiabilite(v1 : float, v2 : float, v3 : float
              , epsilon : float) -> float:
    """Précondition: epsilon > 0    
    Retourne le taux de fiabilité des trois mesures v1, v2 et v3 
    à epsilon près.
    """
    if egal_eps(v1, v2, epsilon) and egal_eps(v2 ,v3 , epsilon)         and egal_eps(v1, v3, epsilon):
        return 1
    elif ((egal_eps(v1, v2, epsilon) and egal_eps(v2,v3,epsilon)) 
        or (egal_eps(v1, v2, epsilon) and egal_eps(v1, v3, epsilon)) 
        or (egal_eps(v1, v3, epsilon) and egal_eps(v2, v3, epsilon))):
        return 2/3
    else:
        return 0

# Jeu de tests
assert fiabilite(3,3,3,1.1) == 1
assert fiabilite(3,2,1,1.1) == 2/3
assert fiabilite(1,2,3,1.1) == 2/3
assert fiabilite(1,3,2,1.1) == 2/3
assert fiabilite(1,3,5,1.1) == 0
assert fiabilite(1,2,5,1.1) == 0
assert fiabilite(1,5,2,1.1) == 0
assert fiabilite(5,1,2,1.1) == 0


# **Deuxième Solution** : La solution précédente, si elle calcule bien ce que l'on veut, effectue possiblement plusieurs fois un même test, ce que l'on peut éviter en imbriquant les conditionnelles.

def fiabilite2(v1 : float, v2 : float, v3 : float
              , epsilon : float) -> float:
    """ ... cf. ci-dessus ... 
    """
    if egal_eps(v1, v2, epsilon):
        if egal_eps(v1, v3, epsilon):
            if egal_eps(v2, v3, epsilon):
                return 1
            else:
                return 2/3
        else:
            if egal_eps(v2, v3, epsilon):
                return 2/3
            else:
                return 0
    elif egal_eps(v2, v3, epsilon):
        if egal_eps(v1, v3, epsilon):
            return 2/3
        else:
            return 0
    else:
        return 0


# **Troisième Solution** : Bien sûr, on peut aussi précalculer nos égalités *à epsilon près*. Cette solution est peut-être plus simple mais elle effectue des calculs parfois inutiles.

def fiabilite3(v1 : float, v2 : float, v3 : float
              , epsilon : float) -> float:
    """ ... cf. ci-dessus ... 
    """
    egal_v1_v2 : bool = egal_eps(v1, v2, epsilon)

    egal_v2_v3 : bool = egal_eps(v2, v3, epsilon)

    egal_v1_v3 : bool = egal_eps(v1, v3, epsilon)

    if egal_v1_v2 and egal_v2_v3 and egal_v1_v3:
        return 1
    elif ((egal_v1_v2 and egal_v2_v3)
        or (egal_v1_v2 and egal_v1_v3) 
        or (egal_v1_v3 and egal_v2_v3)):
        return 2/3
    else:
        return 0

