class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.vide = '∿'
        self.touche = 'x'
        # liste plate
        self.matrice = [self.vide for _ in range(nombre_lignes * nombre_colonnes)]

    def __str__(self):
        """Affichage de la grille sous forme de texte."""
        result = ""
        for l in range(self.nombre_lignes):
            ligne = ""
            for c in range(self.nombre_colonnes):
                index = l * self.nombre_colonnes + c
                ligne += self.matrice[index]
            result += ligne + "\n"
        return result.strip()

    def afficher(self):
        """Affiche directement la grille (équivalent à print)."""
        print(self)

    def tirer(self, x, y):
        """Effectue un tir sur la case (x, y)."""
        if 0 <= x < self.nombre_lignes and 0 <= y < self.nombre_colonnes:
            index = x * self.nombre_colonnes + y
            self.matrice[index] = self.touche
        else:
            raise ValueError("Coordonnées hors de la grille")

