class Grille:
    """
    Classe Grille pour le jeu Bataille Navale.
    Attributs :
        - lignes : nombre de lignes
        - colonnes : nombre de colonnes
        - vide : caractère pour une case vide ('∿')
        - cases : liste de listes représentant la grille
    Méthodes :
        - __str__ : affiche la grille sous forme de texte
    """

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = '∿'
        # création de la grille : liste de listes initialisée avec le caractère vide
        self.cases = [[self.vide for _ in range(colonnes)] for _ in range(lignes)]

    def __str__(self):
        """
        Retourne la grille sous forme de texte pour affichage.
        Chaque ligne est une chaîne, les lignes sont séparées par des sauts de ligne.
        """
        return "\n".join("".join(ligne) for ligne in self.cases)
