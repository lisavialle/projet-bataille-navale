class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def __str__(self):
        orientation = "vertical" if self.vertical else "horizontal"
        return f"Bateau(ligne={self.ligne}, colonne={self.colonne}, longueur={self.longueur}, orientation={orientation})"

    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coule(self, grille) -> bool:
        """
        Retourne True si toutes les positions du bateau sont touchées ('x') sur la grille.
        """
        for (l, c) in self.positions:
            index = l * grille.nombre_colonnes + c
            if grille.matrice[index] != grille.touche:
                return False
        return True
