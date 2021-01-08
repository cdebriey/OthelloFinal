# Jeu Othello dans le cadre du projet pour le cours d' Architecture et qualité logicielle
# Prof. Jean-Guillaume Louis
# Charles de Briey & Benedict Agblevor


#####                                      Importation des librairies                                              #####

from tkinter import *
import json

######                                         Variables globales                                                  #####

# +----------+---------+---------+
# | (-1, -1) | (0, -1) | (-1, 1) |
# +----------+---------+---------+
# | (-1, 0)  |         | (1, 0)  |
# +----------+---------+---------+
# | (-1, 1)  | (0, 1)  | (1, 1)  |
# +----------+---------+---------+
# Tableau des directions généré avec https://www.tablesgenerator.com/text_tables

DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

COULEURS = ["", "black", "white"]



#####                                            Class Plateau                                                     #####

# Class Plateau qui va créer le plateau comme un dictionnaire dont les clés sont des tuples de deux éléments (les
#   coordonnées) et les valeurs sont les couleurs de chaque case (qui représentent le contenu de chaque case; un pion
#   blanc, un pion noir ou un vide). Toutes les méthodes agissant sur le plateau sont définies dans cette classe aussi.

class Plateau:
    def __init__(self):
        self.__grille = {}
        for j in range(1, 9):
            for i in range(1, 9):
                self.__grille[(i, j)] = COULEURS[0]
# Le plateau est en 8x8. En haut à gauche se trouve la case (1,1) et en bas à droite la case (8,8). X va donc de gauche
#   à droite et Y va de haut en bas. On créé un dictionnaire dont les clés sont des tuples (qui représentent les
#   coordonnées) et les valeurs sont les couleurs des cases.


    @property
    def grille(self):
        return self.__grille
# permet de référencer la grille avec xxx.grille dans les autres classes.


    def placePion(self, coord, couleur):
        self.__grille[coord] = couleur
        return self.__grille[coord]
# change la couleur d'une case par ce qu'on lui donne en argument.


    def encadre(self, coord, direction, couleur):
        check = False
        
        i = 1
        while coord[0] + i*direction[0] in range(1, 9) and coord[1] + i*direction[1] in range(1, 9):
            if self.__grille[coord[0] + i*direction[0], coord[1] + i*direction[1]] == couleur:
                check = True
            elif self.__grille[coord[0] + i*direction[0], coord[1] + i*direction[1]] != COULEURS[0] and check is True:
                return True
            else:
                return False
            i += 1
# Vérifie dans la direction donnée si le premier pion rencontré depuis la coordonnée donnée en argument est de la
#   couleur donnée en argument. Si c'est vrai au moins une fois, la fonction recommence la même opération jusqu'à ce
#   qu'elle tombe sur une case de l'autre couleur (dans ce cas elle renvoie True). Si elle rencontre une case vide ou
#   le bord du tableau avant cela, elle renvoie False.


    def rempla(self, coord, direction, couleur):
        i = 1
        while coord[0] + i*direction[0] in range(1, 9) and coord[1] + i*direction[1] in range(1, 9):
            if self.__grille[coord[0] + i*direction[0], coord[1] + i*direction[1]] == couleur:
                if self.__grille[coord[0] + i*direction[0], coord[1] + i*direction[1]] == COULEURS[2]:
                    self.__grille[coord[0] + i * direction[0], coord[1] + i * direction[1]] = COULEURS[1]
                else:
                    self.__grille[coord[0] + i * direction[0], coord[1] + i * direction[1]] = COULEURS[2]
            else:
                return
            i += 1
# La fonction vérifie que la première case dans la direction donnée en argument depuis la coordonnée donnée en argument
#   est de la couleur donnée en argument. Si oui, elle en change la couleur (b devient n et vice versa) et recommence
#   une case plus loin. Sinon, elle s'arrête.


    def estVide(self, coord):
        return self.__grille[coord] == COULEURS[0]
# Renvoie True si la couleur de la coordonnée en argument est "". Sinon renvoie False


    def estAdj(self, coord, couleur):
        for direction in DIRECTIONS:
            if coord[0] + direction[0] in range(1, 9) and coord[1] + direction[1] in range(1, 9) \
                    and self.__grille[(coord[0] + direction[0], coord[1] + direction[1])] == couleur:
                return True
# Renvoie True si la coordonnée en argument est adjacente à une case de la couleur en argument quel que soit la direction.


    def ouJouer(self, couleur):
        possib = []
        for coord in self.__grille.keys():
            if self.estVide(coord):
                if self.estAdj(coord, couleur):
                    for direction in DIRECTIONS:
                        if self.encadre(coord, direction, couleur) and coord not in possib:
                            possib.append(coord)
        return possib
# Renvoie une liste de tuple. Ces tuples sont les cases où on peut jouer

"""
Copyright 2021 Benedict Agblevor & Charles de Briey

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""