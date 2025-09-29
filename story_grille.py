"""
User Story : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire

Actions :
1) créer une grille à 5 lignes et 8 colonnes
2) afficher la grille à l'écran
3) demander à l'utilisateur de rentrer deux coordonnées x et y
4) tirer à l'endroit indiqué sur la grille
5) retour en 2 (boucle)

REMARQUE :
- Les lignes qui appellent une méthode qui pourrait ne pas encore être implémentée
  (par exemple g.tirer(...)) sont volontairement COMMENTÉES. 
  Décommente-les lorsque tu auras codé la méthode correspondante dans grille.py.
"""

# Tentative d'import de la classe Grille (si elle existe dans grille.py).
# Si elle n'existe pas encore, on définit une classe minimale temporaire
# pour permettre d'exécuter la story sans plantage (affichage uniquement).
try:
    from grille import Grille
except Exception:
    # Grille minimale pour permettre d'exécuter la story tant que tu n'as pas codé grille.py
    class Grille:
        def __init__(self, lignes=5, colonnes=8):
            self.lignes = lignes
            self.colonnes = colonnes
            self.vide = '∿'  # caractère pour case vide
            # représentation interne : liste plate ou liste de listes, ici liste de listes
            self.cases = [[self.vide] * colonnes for _ in range(lignes)]

        def __str__(self):
            # affichage ligne par ligne (sans espaces pour ressembler à l'énoncé)
            return "\n".join("".join(ligne) for ligne in self.cases)

        def tirer(self, x, y, impact='x'):
            """Méthode minimale : marque la case si vide.
               NOTE : c'est juste pour permettre des tests manuels si grille.py n'existe pas.
               Quand tu auras ton vrai Grille.tirer dans grille.py, supprime/ignore cette
               définition ou remplace-la.
            """
            if 0 <= x < self.lignes and 0 <= y < self.colonnes:
                if self.cases[x][y] == self.vide:
                    self.cases[x][y] = impact
                    return True
            return False


def jouer():
    # Étape 1 : création de la grille 5x8
    g = Grille(5, 8)

    print("User Story : Plouf dans l'eau")
    print("Tape 'q' à la ligne ou colonne pour quitter.\n")

    while True:
        # Étape 2 : affichage de la grille
        print("Grille actuelle :")
        print(g)
        print()  # ligne vide pour lisibilité

        # Étape 3 : demander les coordonnées à l'utilisateur
        # On accepte 'q' pour quitter la story.
        sx = input(f"Entrez la ligne (0-{g.lignes - 1}) : ")
        if sx.strip().lower() == 'q':
            print("Fin de la story.")
            break
        sy = input(f"Entrez la colonne (0-{g.colonnes - 1}) : ")
        if sy.strip().lower() == 'q':
            print("Fin de la story.")
            break

        # validation des entiers
        try:
            x = int(sx)
            y = int(sy)
        except ValueError:
            print("Entrée invalide — merci d'entrer des nombres entiers.\n")
            continue

        if not (0 <= x < g.lignes and 0 <= y < g.colonnes):
            print("Coordonnées hors de la grille — recommencez.\n")
            continue

        # Étape 4 : tirer à l'endroit indiqué
        # ------------------------------
        # IMPORTANT : la ligne suivante appelle la méthode g.tirer(x, y).
        # Si tu n'as pas encore codé Grille.tirer() dans grille.py → laisse-la COMMENTÉE.
        # Décommente une fois que tu as implémenté Grille.tirer.
        # ------------------------------
        # g.tirer(x, y)   # <-- décommenter quand Grille.tirer est disponible

        # Pour l'instant, si tu veux vérifier manuellement sans implémentation,
        # on affiche juste un message pour valider la story :
        print(f"Tir enregistré en ({x}, {y}). (Décommente g.tirer(x, y) dans ce fichier quand la méthode sera implémentée.)\n")

        # Étape 5 : retour à l'étape 2 (boucle)
        # La boucle recommence automatiquement

if __name__ == "__main__":
    jouer()
