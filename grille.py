class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.vide = '∿'
        self.touche = 'x'
        # la "matrice" représente la grille comme dans ton UML
        self.matrice = [[self.vide for _ in range(nombre_colonnes)] for _ in range(nombre_lignes)]

    def __str__(self):
        """Affichage de la grille sous forme de texte."""
        return "\n".join("".join(ligne) for ligne in self.matrice)

    def afficher(self):
        """Affiche directement la grille (équivalent à print)."""
        print(self)

    def tirer(self, x, y):
        """Effectue un tir sur la case (x, y)."""
        if 0 <= x < self.nombre_lignes and 0 <= y < self.nombre_colonnes:
            self.matrice[x][y] = self.touche
        else:
            raise ValueError("Coordonnées hors de la grille")
