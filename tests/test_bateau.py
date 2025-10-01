import pytest
from bateau import Bateau

def test_creation_bateau_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1  # par défaut
    assert b.vertical is False  # par défaut horizontal

def test_creation_bateau_personnalise():
    b = Bateau(0, 0, longueur=4, vertical=True)
    assert b.ligne == 0
    assert b.colonne == 0
    assert b.longueur == 4
    assert b.vertical is True

def test_positions_horizontal():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]

