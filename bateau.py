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
        """Renvoie la liste des positions (ligne, colonne) occupées par le bateau."""
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]
