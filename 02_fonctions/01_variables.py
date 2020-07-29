# Exercice 2.1 : Variables et affectations (corrigé)

## Question 1

## Question 2

def sante(x : float) -> str:
    """Retourne "Bonne santé" si x vaut 37.5, retourne "Malade" sinon.
    """
    if x == 37.5:
        return "Bonne santé"
    else:
        return "Malade"

# Jeu de tests
assert sante(37.5) == "Bonne santé"
assert sante(40) == "Malade"
assert sante(36) == "Malade"

