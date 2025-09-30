from grille import Grille

def user_story_plouf():
    """
    User Story : "Plouf dans l'eau"
    Utilisateur : un joueur
    Story : On veut pouvoir gérer les tirs de l'adversaire
    Actions :
      - créer une grille à 5 lignes et 8 colonnes
      - afficher la grille à l'écran
      - demander à l'utilisateur de rentrer deux coordonnées x et y
      - tirer à l'endroit indiqué sur la grille
      - retour en 2
    """

    g = Grille(5, 8)
    g.afficher()

    while True:
        try:
            x = int(input("Entrez la ligne (0 à 4) : "))
            y = int(input("Entrez la colonne (0 à 7) : "))
            g.tirer(x, y)
            g.afficher()
        except ValueError:
            print("Coordonnées invalides, essayez encore.")
        except KeyboardInterrupt:
            print("\nFin de la partie.")
            break

# ⚠️ On ne lance la user story que si on exécute ce fichier directement
if __name__ == "__main__":
    user_story_plouf()

