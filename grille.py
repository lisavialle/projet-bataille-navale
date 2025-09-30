class Grille:
    """
    Classe Grille pour le jeu de bataille navale.
    Représente la grille du joueur ou de l'adversaire.
    """

    def __init__(self, nombre_lignes, nombre_colonnes):
        # Dimensions de la grille
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes

        # Codage des cases
        self.vide = '∿'    # case vide
        self.touche = 'x'  # case où l'adversaire a tiré

        # Liste plate représentant la grille (taille = lignes * colonnes)
        self.matrice = [self.vide for _ in range(nombre_lignes * nombre_colonnes)] # Création de la grille : toutes les cases initialisées avec '∿'

    def __str__(self):
    """Affichage de la grille sous forme de texte, vide = '.', tir = 'x'"""
    result = ""
    for l in range(self.nombre_lignes):
        ligne = ""
        for c in range(self.nombre_colonnes):
            index = l * self.nombre_colonnes + c
            case = self.matrice[index]
            # On transforme le symbole '∿' en '.' pour l'affichage
            if case == self.vide:
                ligne += "."
            else:
                ligne += case
        result += ligne + "\n"
    return result.strip()


    def afficher(self):
        """Affiche directement la grille."""
        print(self)

    def tirer(self, ligne, colonne):
        """
        Effectue un tir sur la case (ligne, colonne).
        Marque la case avec le caractère 'x' si coordonnées valides.
        Retourne True si tir effectué, lève ValueError sinon.
        """
        if 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes:
            index = ligne * self.nombre_colonnes + colonne
            self.matrice[index] = self.touche
            return True
        else:
            raise ValueError("Coordonnées hors de la grille")
