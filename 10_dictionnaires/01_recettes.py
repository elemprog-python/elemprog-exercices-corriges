
# Exercice 10.1 : Recettes de cuisine

from typing import Dict, Set
Recette = Dict[str,Set[str]]

Dessert : Recette
Dessert = {
    'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'}
    ,'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'}
    ,'crepes' : {'oeuf', 'farine', 'lait'}
    ,'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'}
    ,'kouign amann' : {'farine', 'beurre', 'sucre'}
 }


## Question 1

def nb_ingredients(des : Recette, r : str) -> int:
    """Précondition : r in des
    Renvoie le nombre d'ingredients necessaires à la recette r
    dans le dictionnaire des recettes des
    """
    return len(des[r])

# Jeu de tests
assert nb_ingredients(Dessert, 'crepes') == 3
assert nb_ingredients(Dessert, 'gateau chocolat') == 5


## Question 2

def recette_avec(des : Recette, i : str) -> Set[str]:
    """Renvoie les recettes de des qui utilisent l'ingrédient i.
    """
    # Ensemble résultat
    ens : Set[str] = set()

    r : str
    for r in des:
        if i in des[r]:
            ens.add(r)

    return ens

# Jeu de tests
assert recette_avec(Dessert, 'beurre')   == {'kouign amann', 'quatre-quarts', 'gateau chocolat'}
assert recette_avec(Dessert, 'lait') == {'crepes'}
assert recette_avec(Dessert, 'fraise') == set()


## Question 3

def tous_ingredients(des : Recette) -> Set[str]:
    """Renvoie les ingrédients apparaissant dans une recette de D.
    """

    # Ensemble résultat
    ens : Set[str] = set()

    r : str
    for r in des:
        i : str
        for i in des[r]:
            ens.add(i)

    return ens

# Jeu de tests
assert tous_ingredients(Dessert)     == {'farine', 'lait', 'yaourt', 'beurre'
        ,'chocolat', 'sucre', 'oeuf'}
assert tous_ingredients(dict()) == set()


# Variante utilisant l'union :

def tous_ingredients2(des : Recette) -> Set[str]:
    """Renvoie les ingrédients apparaissant dans une recette de des.
    """

    ens : Set[str]
    ens = set()

    r : str
    for r in des:
        ens = ens | des[r]

    return ens

# Jeu de tests
assert tous_ingredients2(Dessert)     == {'farine', 'lait', 'yaourt', 'beurre'
        ,'chocolat', 'sucre', 'oeuf'}
assert tous_ingredients2(dict()) == set()

## Question 4

def table_ingredients(des : Recette) -> Dict[str,Set[str]]:
    """Renvoie les recettes associées à chaque ingrédient de des.
    """
    # Dictionnaire résultat
    table : Dict[str, Set[str]] = dict()

    ingredients : Set[str] = tous_ingredients(des)

    i : str
    for i in ingredients:
        table[i] = recette_avec(des, i)

    return table

# Jeu de tests
assert table_ingredients(Dessert)     == {'lait': {'crepes'} 
        ,'beurre': {'gateau chocolat', 'quatre-quarts', 'kouign amann'}
        ,'oeuf': {'gateau chocolat', 'quatre-quarts', 
                  'crepes', 'gateau yaourt'}
        ,'yaourt': {'gateau yaourt'}
        ,'sucre': {'kouign amann', 'gateau chocolat'
                   ,'quatre-quarts', 'gateau yaourt'}
        ,'farine': {'kouign amann', 'gateau chocolat'
                    ,'quatre-quarts', 'crepes', 'gateau yaourt'}
        ,'chocolat': {'gateau chocolat'}}

assert table_ingredients(dict()) == dict()


## Question 5

def ingredient_principal(des : Recette) -> str:
    """Précondition : len(des) > 0
    Renvoie le nom de l'ingredient le plus utilisé.
    """
    table : Dict[str,Set[str]] = table_ingredients(des)

    # Ingredient le plus utilisé
    ires : str = ''

    # Nombre de recettes avec l'ingrédient le plus utilisé
    n : int = 0

    i : str
    for i in table:
        if len(table[i]) > n:
            ires = i
            n = len(table[i])

    return ires

# Jeu de tests
assert ingredient_principal(Dessert) == 'farine'
assert ingredient_principal({'A' : {'a', 'b'},
                             'B' : {'a', 'c'}}) == 'a'
assert ingredient_principal({'A' : {'a', 'b'},
                             'B' : {'a', 'b'}}) in {'a', 'b'}


## Question 6


def recettes_sans(des : Recette, i : str) -> Recette:
    """Renvoie un livre de recettes n'utilisant pas l'ingrédent i.
    """
    # Dictionnaire résultat
    dres : Recette = dict()

    r : str
    for r in des:
        if i not in des[r]:
            dres[r] = des[r]

    return dres

# Jeu de tests
assert recettes_sans(Dessert, 'beurre')     == {'gateau yaourt' : {'yaourt', 'oeuf','farine', 'sucre'}
        ,'crepes' : {'oeuf', 'farine', 'lait'}}
assert recettes_sans(Dessert, 'oeuf')     == {'kouign amann': {'farine', 'beurre', 'sucre'}}
assert recettes_sans(Dessert, 'farine') == {}

