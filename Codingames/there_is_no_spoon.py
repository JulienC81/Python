# -*- coding: utf-8 -*-
"""
width = int(input())  # largeur
height = int(input()) # hauteur
tableau = []

for i in range(height):
    line = input()  # width characters, each either 0 or .
    tableau.append(list(line))
"""

# On capture la ligne (issue de tableau) et le numéro de la ligne (num_lig)
# traitée.
for num_lig, ligne in enumerate(tableau):
    # A partir de la ligne précédente, on parcours les éléments de la ligne afin
    # d'identifier les nodes et les trous. On capture également le numéro de la
    # colonne traitée
    for num_col, node in enumerate(ligne):
        resultat = "" # resultat(str) est le string qui sera retourné à la fin
        colonne = [] # colonne(list) est la colonne à la verticale du node en cours
        node_suivant = num_col + 1
        # Si l'élément en cours est un trou, on passe
        if node == '.':
            continue
        # Sinon, on retourne ses coordonnées, celles du node le plus proche à sa 
        # droite et celles du node le plus proche en bas de lui.
        else:
            resultat += "{} {} ".format(num_col, num_lig)
            colonne = [tableau[index][num_col]for index in range(num_lig, height)]
            if ligne[node_suivant:] and '0' in ligne[node_suivant:]:
                resultat += "{} {} ".format(ligne[node_suivant:].index('0') \
                + node_suivant, num_lig)
            else:
                resultat += "-1 -1 "
            if colonne[1:] and '0' in colonne[1:]:
                resultat += "{} {} ".format(num_col,
                colonne[1:].index('0') + num_lig + 1)
            else:
                resultat += "-1 -1 "
        print(resultat)

# for num_lig, ligne in enumerate(tableau):
#     vertical = []
#     for index in range(num_lig, height):
#         # print(index, tableau[index][0])
#         vertical.append(tableau[index][0])
#         print(num_lig, index, num_lig + 1, vertical, vertical[1:])
