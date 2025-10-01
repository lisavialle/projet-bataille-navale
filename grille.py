from bateau import Bateau

class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.vide = '∿'
        self.touche = 'x'
        self.bateau = '⛵'
        self.matrice = [self.vide for _ in range(nombre_lignes * nombre_colonnes)]

    def __str__(self):
        """Affichage de la grille sous forme de texte"""
        result = ""
        for l in range(self.nombre_lignes):
            ligne = ""
            for c in range(self.nombre_colonnes):
                index = l * self.nombre_colonnes + c
                case = self.matrice[index]
                # On transforme 'vide' en '.' pour l'affichage
                if case == self.vide:
                    ligne += "."
                else:
                    ligne += case
            result += ligne + "\n"
        return result.strip()

    def afficher(self):
        print(self)

    def tirer(self, ligne, colonne):
        if 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes:
            index = ligne * self.nombre_colonnes + colonne
            self.matrice[index] = self.touche
            return True
        else:
            raise ValueError("Coordonnées hors de la grille")

    def ajoute(self, bateau: Bateau):
        """Ajoute un bateau sur la grille si toutes ses positions sont valides"""
        # Vérifie que toutes les positions sont dans la grille
        for (l, c) in bateau.positions:
            if l >= self.nombre_lignes or c >= self.nombre_colonnes:
                return False  # le bateau ne rentre pas
        # Place le bateau
        for (l, c) in bateau.positions:
            index = l * self.nombre_colonnes + c
            self.matrice[index] = self.bateau
        return True