
# Exercice 9.1. : Différence symétrique

## Question 1

from typing import Set, TypeVar
T = TypeVar('T')

def diff_sym(ens1 : Set[T], ens2 : Set[T]) -> Set[T]:
    """Retourne la différence symétrique entre ens1 et ens2.
    """
    # Ensemble résultat
    ens : Set[T] = set()
    
    e1 : T
    for e1 in ens1:
        if e1 not in ens2:
            ens.add(e1)
            
    e2 : T
    for e2 in ens2:
        if e2 not in ens1:
            ens.add(e2)
            
    return ens

# Jeu de tests
assert diff_sym({2, 5, 9}, {3, 5, 8}) == {2, 3, 8, 9}
assert diff_sym({2, 5, 9}, {2, 5, 8, 9}) == {8}
assert diff_sym({'a', 'b', 'c'}, {'d', 'e', 'f'})        == {'a', 'b', 'c', 'd', 'e', 'f'}
assert diff_sym({'a', 'b', 'c'}, set()) == {'a', 'b', 'c'}
assert diff_sym(set(), {'d', 'e', 'f'}) == {'d', 'e', 'f'}
assert diff_sym({'a', 'b', 'c'}, {'a', 'b', 'c'}) == set()

## Question 2

def diff_sym2(ens1 : Set[T], ens2 : Set[T]) -> Set[T]:
    """Retourne la différence symétrique entre ens1 et ens2.
    """
    return (ens1 - ens2) | (ens2 - ens1)

# Jeu de tests
assert diff_sym2({2, 5, 9}, {3, 5, 8}) == {2, 3, 8, 9}
assert diff_sym2({2, 5, 9}, {2, 5, 8, 9}) == {8}
assert diff_sym2({'a', 'b', 'c'}, {'d', 'e', 'f'})        == {'a', 'b', 'c', 'd', 'e', 'f'}
assert diff_sym2({'a', 'b', 'c'}, set()) == {'a', 'b', 'c'}
assert diff_sym2(set(), {'d', 'e', 'f'}) == {'d', 'e', 'f'}
assert diff_sym2({'a', 'b', 'c'}, {'a', 'b', 'c'}) == set()

# Concernant l'efficacité, ici on a besoin de parcourir plusieurs fois
# chaque ensemble, alors qu'un seul parcours suffit dans la première
# définition, qui est donc plus efficace «théoriquement». Cependant,
# les opérateurs ensemblistes de Python sont implémentés en langage C
# et compilés en code optimisé. Il est donc possible que la seconde
# version soit donc plus performante en pratique. Dans tous les cas, à
# moins de considérer de très gros ensembles (plusieurs centaines de
# milliers d'éléments au minimum), on n'observera pas de différence
# importante.
