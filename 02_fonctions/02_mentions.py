# Exercice 2.2 : Calcul des mentions (corrigé)

## Question 1


def mention(note : float) -> str:
    """Précondition : (note>=0) and (note<=20)
    Retourne la mention correspondant à la note spécifiée.
    """
    if note < 10:
        return 'Eliminé'
    elif note < 12:
        return 'Passable'
    elif note < 14:
        return 'AB'
    elif note < 16:
        return 'B'
    else:
        return 'TB'

# Jeu de tests
assert mention(0) == 'Eliminé'
assert mention(8) == 'Eliminé'
assert mention(10) == 'Passable'
assert mention(12.5) == 'AB'
assert mention(15) == 'B'
assert mention(20) == 'TB'


# Une autre version dans l'ordre décroissant :

def mention_bis(note : float) -> str:
    """ ... cf. ci-dessus ... """    
    if note >= 16:
        return 'TB'
    elif note >= 14:
        return 'B'
    elif note >= 12:
        return 'AB'
    elif note >= 10:
        return 'Passable'
    else:
        return 'Eliminé'


## Question 2

def mention_2(note : float) -> str:
    """ ... cf-ci-dessus ..."""        
    if note < 12:
        if note < 10:
            return 'Eliminé'
        else: 
            return 'Passable'
    elif note < 14:
        return 'AB'
    elif note < 16:
        return 'B'
    else:
        return 'TB'


# Avec cette version, l'évaluation ne nécessite que 2 tests lorsque $0 \leq note  < 14$ et 3 tests lorsque $14 \leq note \leq 20$.

