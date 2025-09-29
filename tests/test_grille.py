import pytest
from grille import Grille

def test_init():
    """
    Test de création d'un objet Grille.
    Vérifie que l'objet est bien de type Grille.
    """
    g = Grille()
    assert isinstance(g, Grille)
    