import random
import time
import os
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

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
# Affichage grille avec curseur
# ---------------------------
def afficher_grille_ptg(grille: Grille, curseur_l: int, curseur_c: int):
    lines = []
    header = "   " + " ".join(str(i) for i in range(grille.nombre_colonnes))
    lines.append(header)
    for i in range(grille.nombre_lignes):
        row = f"{i}  "
        for j in range(grille.nombre_colonnes):
            index = i * grille.nombre_colonnes + j
            case = grille.matrice[index]
            char = case
            if i == curseur_l and j == curseur_c:
                char = f"[{char}]"  # Curseur autour de la case
            row += char + " "
        lines.append(row)
    return "\n".join(lines)

# ---------------------------
# Jeu principal interactif
# ---------------------------
def jeu_gui_final():
    grille_interne = Grille(8, 10)
    grille_visible = Grille(8, 10)

    # Crée un bateau de chaque type
    bateaux = [
        PorteAvion(0, 0),
        Croiseur(0, 0),
        Torpilleur(0, 0),
        SousMarin(0, 0)
    ]

    # Placement aléatoire sécurisé
    for b in bateaux:
        placer_bateau_aleatoirement(grille_interne, b)

    coups = 0
    bateaux_restants = bateaux.copy()
    curseur_l, curseur_c = 0, 0

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bataille Navale Interactive ! Utilisez les flèches pour déplacer le curseur et Entrée pour tirer.")

    while bateaux_restants:
        print(afficher_grille_ptg(grille_visible, curseur_l, curseur_c))
        print("\nUtilisez les touches: Z=haut, S=bas, Q=gauche, D=droite, Entrée=tir")
        key = input("Direction (Z/S/Q/D) ou tir (Entrée): ").strip().upper()

        if key == "Z":
            curseur_l = max(0, curseur_l - 1)
        elif key == "S":
            curseur_l = min(grille_visible.nombre_lignes - 1, curseur_l + 1)
        elif key == "Q":
            curseur_c = max(0, curseur_c - 1)
        elif key == "D":
            curseur_c = min(grille_visible.nombre_colonnes - 1, curseur_c + 1)
        elif key == "":
            coups += 1
            touche_bateau = False

            for b in bateaux_restants:
                if (curseur_l, curseur_c) in b.positions:
                    grille_visible.tirer(curseur_l, curseur_c, touche="💣")
                    touche_bateau = True

                    if b.coule(grille_visible):
                        for l, c in b.positions:
                            grille_visible.matrice[l * grille_visible.nombre_colonnes + c] = b.marque
                        bateaux_restants.remove(b)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(afficher_grille_ptg(grille_visible, curseur_l, curseur_c))
                        print(f"🎉 Vous avez coulé un {b.__class__.__name__} !")
                        time.sleep(1.5)
                    break

            if not touche_bateau:
                grille_visible.tirer(curseur_l, curseur_c)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(afficher_grille_ptg(grille_visible, curseur_l, curseur_c))
                print("💥 Raté !")
                time.sleep(1)

        os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Félicitations ! Vous avez coulé tous les bateaux en {coups} coups !")

# ---------------------------
# Exécution directe
# ---------------------------
if __name__ == "__main__":
    jeu_gui_final()
