import pytest
from grille import Grille

def test_creation_grille():
    g = Grille(4, 6)
    # Vérifie la taille totale de la liste
    assert len(g.matrice) == 4 * 6
    # Vérifie que toutes les cases sont initialisées à vide
    assert all(case == g.vide for case in g.matrice)

def test_tirer_valide():
    g = Grille(3, 3)
    assert g.tirer(1, 1) is True
    # Vérifie que la case est bien marquée
    assert g.matrice[1 * g.nombre_colonnes + 1] == g.touche

def test_tirer_hors_grille():
    g = Grille(3, 3)
    with pytest.raises(ValueError):
        g.tirer(5, 5)

def test_str():
    g = Grille(5, 8)
    # Affichage initial : toutes les cases vides
    attendu = "........\n........\n........\n........\n........"
    assert str(g) == attendu

    # Tir sur la ligne 2, colonne 3
    g.tirer(2, 3)
    attendu = "........\n........\n...x....\n........\n........"
    assert str(g) == attendu

