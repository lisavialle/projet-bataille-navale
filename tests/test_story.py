from grille import Grille

def test_user_story_simulee():
    g = Grille(5, 8)
    g.tirer(2, 3)
    attendu = "........\n........\n...x....\n........\n........"
    assert str(g) == attendu