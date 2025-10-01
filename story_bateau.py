from bateau import Bateau

def chevauchent(b1: Bateau, b2: Bateau) -> bool:
    """Retourne True si les bateaux b1 et b2 partagent au moins une case"""
    return any(pos in b2.positions for pos in b1.positions)

def user_story_chevauchement():
    """
    User Story : "chevauchement"
    Utilisateur : un joueur
    Story : Positionner des bateaux sans chevauchement
    """

    print("=== Cas 1 : deux bateaux qui SE chevauchent ===")
    b1 = Bateau(2, 3, longueur=3)          # (2,3), (2,4), (2,5)
    b2 = Bateau(2, 4, longueur=2)          # (2,4), (2,5)
    print("Positions b1 :", b1.positions)
    print("Positions b2 :", b2.positions)
    print("Chevauchent ?", chevauchent(b1, b2))

    print("\n=== Cas 2 : deux bateaux qui NE se chevauchent PAS ===")
    b3 = Bateau(0, 0, longueur=2)          # (0,0), (0,1)
    b4 = Bateau(1, 0, longueur=2, vertical=True) # (1,0), (2,0)
    print("Positions b3 :", b3.positions)
    print("Positions b4 :", b4.positions)
    print("Chevauchent ?", chevauchent(b3, b4))

if __name__ == "__main__":
    user_story_chevauchement()
