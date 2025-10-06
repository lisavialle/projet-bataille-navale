import random
import time
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

# ---------------------------
# Couleurs ANSI
# ---------------------------
RESET = "\033[0m"
ROUGE = "\033[91m"
VERT = "\033[92m"
CYAN = "\033[96m"
JAUNE = "\033[93m"

# ---------------------------
# Placement aléatoire sécurisé
# ---------------------------

def generer_positions_valides(grille: Grille, bateau):
    positions_valides = []

    for vertical in [False, True]:
        bateau.vertical = vertical
        for l in range(grille.nombre_lignes):
            for c in range(grille.nombre_colonnes):
                bateau.ligne = l
                bateau.colonne = c

                rentre_dans_grille = all(
                    0 <= pos[0] < grille.nombre_lignes and 0 <= pos[1] < grille.nombre_colonnes
                    for pos in bateau.positions
                )
                if not rentre_dans_grille:
                    continue

                chevauchement = any(
                    grille.matrice[pos[0]*grille.nombre_colonnes + pos[1]] != grille.vide
                    for pos in bateau.positions
                )
                if not chevauchement:
                    positions_valides.append((l, c, vertical))

    return positions_valides

def placer_bateau_aleatoirement(grille: Grille, bateau):
    positions_valides = generer_positions_valides(grille, bateau)
    if not positions_valides:
        return False
    l, c, vertical = random.choice(positions_valides)
    bateau.ligne = l
    bateau.colonne = c
    bateau.vertical = vertical
    grille.ajoute(bateau)
    return True

# ---------------------------
# Affichage grille avancé
# ---------------------------

def afficher_grille_coloree_avance(grille_visible: Grille):
    grid_text = "   " + " ".join(f"{i}" for i in range(grille_visible.nombre_colonnes)) + "\n"
    for i in range(grille_visible.nombre_lignes):
        ligne = f"{i}  "
        for j in range(grille_visible.nombre_colonnes):
            index = i * grille_visible.nombre_colonnes + j
            case = grille_visible.matrice[index]

            if case == "x":
                ligne += ROUGE + "x " + RESET
            elif case == "💣":
                ligne += JAUNE + "💣 " + RESET
            elif case in ["🚢", "⛴", "🚣", "🐟"]:
                ligne += VERT + case + " " + RESET
            else:
                ligne += CYAN + "∿ " + RESET
        grid_text += ligne + "\n"
    return grid_text

# ---------------------------
# Jeu principal avancé
# ---------------------------

def jeu_gui_avance():
    grille_interne = Grille(8, 10)   # contient les vrais bateaux
    grille_visible = Grille(8, 10)   # ce que le joueur voit

    bateaux = [
        PorteAvion(0, 0),
        Croiseur(0, 0),
        Torpilleur(0, 0),
        SousMarin(0, 0)
    ]

    for b in bateaux:
        placer_bateau_aleatoirement(grille_interne, b)

    coups = 0
    bateaux_restants = bateaux.copy()

    print("\033c", end="")
    print(CYAN + "Bienvenue dans la bataille navale avancée !\n" + RESET)

    while bateaux_restants:
        print(f"Nombre de coups joués : {coups}\n")
        print(afficher_grille_coloree_avance(grille_visible))

        try:
            x = int(input("Entrez la ligne (0-7) : "))
            y = int(input("Entrez la colonne (0-9) : "))
        except ValueError:
            print("Entrée invalide. Réessayez.")
            print("\033c", end="")
            continue

        if not (0 <= x < grille_visible.nombre_lignes and 0 <= y < grille_visible.nombre_colonnes):
            print("Coordonnées hors de la grille.")
            print("\033c", end="")
            continue

        coups += 1
        touche_bateau = False

        for b in bateaux_restants:
            if (x, y) in b.positions:
                grille_visible.tirer(x, y, touche="💣")
                touche_bateau = True

                # Vérifier si le bateau est coulé (avec la grille INTERNE)
                if b.coule(grille_interne):
                    # Montrer toutes ses cases sur la grille visible
                    for (l, c) in b.positions:
                        grille_visible.matrice[l * grille_visible.nombre_colonnes + c] = b.marque

                    print("\033c", end="")
                    print(f"Nombre de coups joués : {coups}\n")
                    print(afficher_grille_coloree_avance(grille_visible))
                    print(VERT + f"🎉 Coulé ! Vous avez coulé le {b.__class__.__name__} !" + RESET)
                    bateaux_restants.remove(b)
                    time.sleep(2)  # pause pour bien voir le message

                break  # on arrête après avoir touché

        if not touche_bateau:
            grille_visible.tirer(x, y)  # Tir raté
            print("\033c", end="")
            print(f"Nombre de coups joués : {coups}\n")
            print(afficher_grille_coloree_avance(grille_visible))
            print(ROUGE + "💥 Raté !" + RESET)
            time.sleep(1)

        print("\033c", end="")

    # Partie terminée
    print(afficher_grille_coloree_avance(grille_visible))
    print(f"Félicitations ! Vous avez coulé tous les bateaux en {coups} coups !")

# ---------------------------
# Exécution directe
# ---------------------------
if __name__ == "__main__":
    jeu_gui_avance()
