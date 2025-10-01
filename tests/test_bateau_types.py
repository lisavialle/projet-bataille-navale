import pytest
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille

def test_bateau_marque_porte_avion():
    g = Grille(4, 4)
    b = PorteAvion(0, 0)
    g.ajoute(b)
    assert all(g.matrice[i] == "🚢" for i in range(4))  # 4 cases horizontales

def test_bateau_marque_croiseur():
    g = Grille(4, 4)
    b = Croiseur(1, 0, vertical=True)
    g.ajoute(b)
    positions = [(1, 0), (2, 0), (3, 0)]
    for l, c in positions:
        index = l * g.nombre_colonnes + c
        assert g.matrice[index] == "⛴"

def test_bateau_marque_torpilleur():
    g = Grille(2, 3)
    b = Torpilleur(0, 1)
    g.ajoute(b)
    positions = [(0, 1), (0, 2)]
    for l, c in positions:
        index = l * g.nombre_colonnes + c
        assert g.matrice[index] == "🚣"

def test_bateau_marque_sous_marin():
    g = Grille(3, 3)
    b = SousMarin(1, 1, vertical=True)
    g.ajoute(b)
    positions = [(1, 1), (2, 1)]
    for l, c in positions:
        index = l * g.nombre_colonnes + c
        assert g.matrice[index] == "🐟"
