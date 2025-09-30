import pytest
from grille import Grille

def test_init():
    g = Grille(5, 8)
    assert g.nombre_lignes == 5
    assert g.nombre_colonnes == 8
    # vérifie que la matrice contient bien uniquement des cases vides
    for ligne in g.matrice:
        for case in ligne:
            assert case == g.vide

def test_tirer():
    g = Grille(3, 3)
    g.tirer(1, 1)
    assert g.matrice[1][1] == g.touche

def test_tirer_hors_grille():
    g = Grille(3, 3)
    with pytest.raises(ValueError):
        g.tirer(5, 5)
