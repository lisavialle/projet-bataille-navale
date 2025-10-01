class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def __str__(self):
        orientation = "vertical" if self.vertical else "horizontal"
        return f"Bateau(ligne={self.ligne}, colonne={self.colonne}, longueur={self.longueur}, orientation={orientation})"
