
# Exercice 11.1 : Compréhensions en vrac

import math

from typing import List, Set, Dict

Liste : List[int]
Liste = [ 2, 5, 12, 31, 2, 17, 31, 42, 2 ]

Dico : Dict[str,str]
Dico = {'xx':'bli', 'yzy':'blo', 'cuicui':'toutou', 'miaou':'toutou' }

Ens : Set[float]
Ens = { 2.7, 4.12, 3.31, 8.29, 1.13, 12.31 }


## Question 1 : compréhensions de listes

# [ (k,Dico[k]) for k in Dico ]

# [ (k,v) for (k,v) in Dico.items() ]

# [ Dico[k] for k in Dico ]

# [ v for (k,v) in Dico.items() ]

# [ math.ceil(v) for v in Ens if v < 5.0 ]


## Question 2 : compréhensions d'ensembles

# { c for c in 'a bac a cab' }

# { c for c in 'a bac a cab' if c != ' ' }

# { (k, Dico[k]) for k in Dico }

# { v for (k,v) in Dico.items() }

# { Dico[k] for k in Dico }

# { k + 's' for k in Dico if len(Dico[k]) > 3 }

# { n % 5 for n in Liste }

# { n % 10 for n in range(0, 20) }

# [ n % 10 for n in range(0, 20) ]

## Question 3 : Compréhensions de dictionnaires

# { k:Dico[k] for k in Dico }

# { Dico[k]:k for k in Dico }

# { (v + v):k for (k, v) in Dico.items() }

# { (Dico[k] + Dico[k]):k for k in Dico }

# { k:v for (k, v) in zip(range(1, 8), Liste)}

# { k:v for (k, v) in zip(range(1, 10), Liste) if v > 15 }

# { k:v for k in range(1, 10) for v in Liste if v > 15 }


