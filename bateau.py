class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = None  # marque générique pour la classe de base

    def __str__(self):
        orientation = "vertical" if self.vertical else "horizontal"
        return f"{self.__class__.__name__}(ligne={self.ligne}, colonne={self.colonne}, longueur={self.longueur}, orientation={orientation}, marque={self.marque})"

    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coule(self, grille) -> bool:
        for (l, c) in self.positions:
            index = l * grille.nombre_colonnes + c
            if grille.matrice[index] != grille.touche:
                return False
        return True

# --------------------------
# Sous-classes pour chaque type
# --------------------------

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "⛴"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
