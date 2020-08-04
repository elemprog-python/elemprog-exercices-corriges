
# Exercice 6.5 : Découpages

from typing import List, TypeVar
T = TypeVar('T')


## Question 1 : découpages simples

def decoupage_simple(l : List[T], i : int, j : int) -> List[T]:
    """Précondition : (i >= 0) and (j >= 0)
    Retourne le découpage l[i:j].
    """
    # Liste résultat
    lr : List[T] = []
        
    k : int
    for k in range(i, j):
        if k < len(l):
            lr.append(l[k])
            
    return lr



# Jeu de tests
lcomptine : List[str]
lcomptine = ['am', 'stram', 'gram', 'pic', 'pic', 'col', 'gram']

assert decoupage_simple(lcomptine, 1, 3) == lcomptine[1:3]
assert decoupage_simple(lcomptine, 3, 4) == lcomptine[3:4]
assert decoupage_simple(lcomptine, 3, 3) == lcomptine[3:3]
assert decoupage_simple(lcomptine, 5, 3) == lcomptine[5:3]
assert decoupage_simple(lcomptine, 0, 7) == lcomptine[0:7]


## Question 2 : découpage avec pas

def decoupage_pas(l : List[T], i : int, j : int, p : int) -> List[T]:
    """Précondition : (i >= 0) and (j >= 0) and (p > 0)
    Retourne le découpage l[i:j:p].
    """
    lr : List[T] = []
    k : int
    k = i   # on commence en i
    while k < j:   # j n'est pas inclus
        if k < len(l):
            lr.append(l[k])
            
        k = k + p
            
    return lr

# Jeu de tests
assert decoupage_pas(lcomptine,1, 5, 2) == lcomptine[1:5:2]
assert decoupage_pas(lcomptine,2, 6, 1) == lcomptine[2:6:1]


## Question 3 : pas inverse

def decoupage_pas_inv(l : List[T], i : int, j : int, p : int) -> List[T]:
    """Précondition : (i >= 0) and (j >= 0) and (p < 0)
    Retourne le découpage l[i:j:p].
    """
    lr : List[T] = []
    k : int = i  # on commence en i
    while k > j:   # j est inclus
        if k < len(l):
            lr.append(l[k])
            
        k = k + p
            
    return lr

# Jeu de tests
assert decoupage_pas_inv(lcomptine, 5, 2, -2) == lcomptine[5:2:-2]
assert decoupage_pas_inv(lcomptine, 6, 0, -1) == lcomptine[6:0:-1]
assert decoupage_pas_inv(lcomptine, 6, 0, -3) == lcomptine[6:0:-3]


## Question 4 : découpage généralisé

def normalisation(i : int, long: int) -> int:
    """Précondition: long >= 0
    Retourne la normalisation de l'indice k pour
    une liste de longueur long.
    """  
    if i < 0: # indice négatif
        if -i <= long:  # dans l'intervalle [O;long]
            return long + i
        else: # en dehors de l'intervalle [0;long]
            return 0
    else: # indice positif
        if i > long: # en dehors de l'intervalle [0;long]
            return long
        else:
            return i  # déjà normalisé


# jeu de tests
assert normalisation(0, 6) == 0  # positif dans [0;6]
assert normalisation(4, 6) == 4  # positif dans [0;6]
assert normalisation(6, 6) == 6  # positif dans [0;6]
assert normalisation(7, 6) == 6  # positif hors [0;6]
assert normalisation(-0, 6) == 0 # négatif (cas limite)
assert normalisation(-1, 6) == 5 # négatif dans [0;6]
assert normalisation(-3, 6) == 3 # négatif dans [0;6]
assert normalisation(-5, 6) == 1 # négatif dans [0;6]
assert normalisation(-6, 6) == 0 # négatif dans [0;6]
assert normalisation(-7, 6) == 0 # négatif hors [0;6]


def decoupage(l : List[T], i : int, j : int, p : int) -> List[T]:
    """Précondition : p != 0
    Retourne le découpage l[i:j:p].
    """
    # Normalisation de i
    ni : int = normalisation(i, len(l))
    
    # Normalisation de j
    nj : int = normalisation(j, len(l))
    
    if p > 0: # pas strictement positif
        return decoupage_pas(l, ni, nj, p)
    else: # pas strictement négatif (d'après l'hypothèse)
        return decoupage_pas_inv(l, ni, nj, p)

# Jeu de tests
assert decoupage(lcomptine, 1, 3, 1) == lcomptine[1:3]
assert decoupage(lcomptine, 3, 4, 1) == lcomptine[3:4]
assert decoupage(lcomptine, 3, 3, 1) == lcomptine[3:3]
assert decoupage(lcomptine, 5, 3, 1) == lcomptine[5:3]
assert decoupage(lcomptine, 0, 7, 1) == lcomptine[0:7]
assert decoupage(lcomptine, -4, -1, 1) == lcomptine[-4:-1]
assert decoupage(lcomptine, -6, -2, 1) == lcomptine[-6:-2]
assert decoupage(lcomptine,1, 5, 2) == lcomptine[1:5:2]
assert decoupage(lcomptine,2, 6, 1) == lcomptine[2:6:1]
assert decoupage(lcomptine, 5, 2, -2) == lcomptine[5:2:-2]
assert decoupage(lcomptine, 6, 0, -1) == lcomptine[6:0:-1]
assert decoupage(lcomptine, 6, 0, -3) == lcomptine[6:0:-3]

