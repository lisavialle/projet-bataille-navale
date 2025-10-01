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

from bateau import Bateau

def test_ajoute_bateau():
    g = Grille(2, 3)
    # Ajout bateau horizontal qui rentre
    b1 = Bateau(1, 0, longueur=2, vertical=False)
    assert g.ajoute(b1) is True
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]

    # Ajout bateau vertical qui ne rentre pas
    b2 = Bateau(1, 0, longueur=2, vertical=True)
    assert g.ajoute(b2) is False
    # Grille inchangée
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]

    # Ajout bateau trop long
    b3 = Bateau(1, 0, longueur=4, vertical=True)
    assert g.ajoute(b3) is False
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]