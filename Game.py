from tkinter import *
import json
from Plateau import *

#####                                                 Class Jeu                                                   ######

# Class Jeu qui va gérer toutes les actions de chaque partie

class Jeu:
    def __init__(self):
        self.plateau = Plateau()
        self.plateau.placePion((4, 4), COULEURS[2])
        self.plateau.placePion((4, 5), COULEURS[1])
        self.plateau.placePion((5, 4), COULEURS[1])
        self.plateau.placePion((5, 5), COULEURS[2])

 

        self.__tour = 0
        self.dictscore = {}
# Place les pions initiaux et le compteur de tour à 0


    @property
    def tour(self):
        return self.__tour


    def couleurJoueur(self):
        if self.__tour % 2 == 0:
            return COULEURS[1]
        else:
            return COULEURS[2]
# Renvoie la couleur du joueur dont c'est le tour. Le premier tour est toujours noir.


    def couleurAdverse(self):
        if self.couleurJoueur() == COULEURS[1]:
            return COULEURS[2]
        else:
            return COULEURS[1]
# Renvoie la couleur de l'autre joueur


    def calculScore(self, couleur):
        score = 0
        for elem in self.plateau.grille.values():
            if elem == couleur:
                score += 1
        return score
# Calcule le score de la couleur donnée en argument.

    def changeTour(self):
        self.__tour += 1


    def jouer(self, coord):
        self.plateau.placePion(coord, self.couleurJoueur())
        for direction in DIRECTIONS:
            if self.plateau.encadre(coord, direction, self.couleurAdverse()):
                self.plateau.rempla(coord, direction, self.couleurAdverse())
        self.changeTour()
        return coord 
# Joue un tour (place un pion, remplace ce qu'il faut et avance le compteur de tour).


    def getHscore(self):
       fichierscore = open('hscore.txt')
       self.dictscore = json.load(fichierscore)
       fichierscore.close()
       max = ['', 0]
       if len(self.dictscore) == 0:
           return ["personne", 0]
       for score in self.dictscore:
           if max[1] < int(self.dictscore[score]):
               max[1] = int(self.dictscore[score])
               max[0] = score
       return max
# Importe le fichier texte des scores et renvoi le pseudo et le score correspondant dont le score est le plus élevé.


    def majscores(self, nomN, nomB):
        fichierscore = open('hscore.txt')
        self.dictscore = json.load(fichierscore)
        fichierscore.close()
        self.scorefinB = self.calculScore(COULEURS[2])
        self.scorefinN = self.calculScore(COULEURS[1])
        for pseudo, score in self.dictscore.items():
            if pseudo == nomB and self.scorefinB > score:
                self.dictscore[nomB] = self.scorefinB
            elif pseudo == nomN and self.scorefinN > score:
                self.dictscore[nomN] = self.scorefinN
        if nomB not in self.dictscore.keys():
            self.dictscore[nomB] = self.scorefinB
        if nomN not in self.dictscore.keys():
            self.dictscore[nomN] = self.scorefinN
        fichierscore = open('hscore.txt', 'w')
        fichierscore.write(json.dumps(self.dictscore, indent=2))
        fichierscore.close()
# Met à jour le fichier texte des scores en y ajoutant de nouvelles entrées ou en mettant à jour le nouveau meilleur
#   score du joueur ayant déjà joué.

"""
Copyright 2020 Benedict Agblevor & Charles de Briey

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
