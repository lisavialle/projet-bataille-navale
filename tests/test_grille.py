import pytest
from grille import Grille

def test_init():
    """
    Teste que l'on peut créer une grille et que ses dimensions sont correctes.
    """
    g = Grille(5, 8)
    assert isinstance(g, Grille)
    assert len(g.cases) == 5          # 5 lignes
    assert len(g.cases[0]) == 8       # 8 colonnes

def test_str():
    """
    Teste que l'affichage __str__ fonctionne correctement
    """
    g = Grille(2, 3)
    expected = "∿∿∿\n∿∿∿"
    assert str(g) == expected