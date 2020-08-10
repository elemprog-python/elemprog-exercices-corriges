
# Exercice 10.2 : Statistiques sur les lettres

from typing import Dict, Set

def est_lettre(c : str) -> bool:
    """Précondition : len(c) == 1    (caractère)
    Retourne True si le caractère c est une lettre, ou False sinon.
    """
    return ((c >= 'a') and (c <= 'z'))         or ((c >= 'A') and (c <= 'Z'))         or (c in {'é', 'è', 'à', 'ù', 'œ'})

# Jeu de tests
assert est_lettre('a') == True
assert est_lettre('Z') == True
assert est_lettre(',') == False
assert est_lettre('1') == False

## Question 1

def frequences_lettres(s : str) -> Dict[str,int]:
    """Retourne les fréquences des lettres de la chaîne s.
    """
    # Dictionnaire résultat
    freqs : Dict[str,int] = dict()
    
    c : str
    for c in s:
        if est_lettre(c): # seulement si c est une lettre
            if c in freqs: # caractère présent
                freqs[c] = freqs[c] + 1  # incrémenter la fréquence
            else:
                freqs[c] = 1  # première occurrence
            
    return freqs

# Jeu de tests
assert frequences_lettres('alea jacta est')        == {'l': 1, 'j': 1, 'a': 4, 't': 2, 's': 1, 'e': 2, 'c': 1}
assert frequences_lettres("l'élève")        == {'v': 1, 'e': 1, 'l': 2, 'é': 1, 'è': 1}

## Question 2

def lettre_freq_max(freqs : Dict[str,int]) -> str:
    """Précondition : len(Freqs) > 0
    Retourne la lettre de fréquence maximale dans freqs.
    """
    # Fréquence maximale
    fmax : int = 0
    
    # Lettre de fréquence maximale
    lmax : str = ''
    
    lettre : str
    for lettre in freqs:
        if freqs[lettre] > fmax:
            fmax = freqs[lettre]
            lmax = lettre
            
    return lmax

# Jeu de tests
assert lettre_freq_max({'l': 1, 'j': 1, 'a': 4, 
                        't': 2, 's': 1, 'e': 2, 'c': 1}) == 'a'
assert lettre_freq_max(frequences_lettres('alea jacta est')) == 'a'
assert lettre_freq_max(frequences_lettres("l'élève")) == 'l'


## Question 3

def chargement_texte(fichier : str) -> str:
    """Précondition : le fichier est présent sur le disque
    Retourne la chaîne de caractères correspondant au contenu
    du fichier.
    """
    # Contenu du fichier
    contenu : str = ''
    
    with open(fichier, 'r') as f:
        contenu = f.read()
        
    return contenu

# Après avoir récupéré le fichier d'exemple et l'avoir placé dans le répertoire courant :

# frequences_lettres(chargement_texte('9645.txt.utf-8'))

# lettre_freq_max(
#         frequences_lettres(
#             chargement_texte('9645.txt.utf-8')))


## Question 4

def lettres_freq_inf(freqs : Dict[str,int], fseuil : int) -> Set[str]:
    """Précondition : fseuil > 0
    Retourne les lettres de fréquence inférieure
    à fseuil dans freqs.
    """
    # Lettres de fréquence inférieure au seuil
    finf : Set[str] = set()
        
    lettre : str
    for lettre in freqs:
        if freqs[lettre] <= fseuil:
            finf.add(lettre)

    return finf

# Jeu de tests
assert lettres_freq_inf(frequences_lettres('alea jacta est'), 1)        == {'c', 'j', 'l', 's'}
assert lettres_freq_inf(frequences_lettres("l'élève"), 2)        == {'e', 'l', 'v', 'è', 'é'}

## Question 5

# lettres_freq_inf(
#         frequences_lettres(
#             chargement_texte('9645.txt.utf-8')), 100)

