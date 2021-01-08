from tkinter import *
import json
from Game import *

#####                                                  Class Graph                                                 #####

# Class Graph qui est notre interface graphique

class Graph(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.bienvenue = Label(self, text="Bonjour, bienvenue dans l'Othello de Charles & Benedict")
        self.bienvenue.grid(row=0, columnspan=2)
        self.partie = Jeu()
        self.scoremax = self.partie.getHscore()
        Label(self, text="Le meilleur score est actuellement de : {} détenu par {} ".format(self.scoremax[1], self.scoremax[0])).grid(row=2, column=0, columnspan=2)
        Label(self, text="Quel est le nom du joueur 1 ?").grid(row=3, column=0)
        Label(self, text="Quel est le nom du joueur 2 ?").grid(row=4, column=0)
        self.inputB = Entry(self)
        self.inputN = Entry(self)
        self.inputB.grid(row=4, column=1)
        self.inputN.grid(row=3, column=1)
        self.butnp = Button(self, text="Nouvelle Partie")
        self.butnp.grid(row=5, column=1)
        self.butnp.bind('<Button-1>', self.lancenp)
        self.tapi = Canvas(width=399, height=399, bg='darkgreen')
        self.tapi.grid(row=8, column=0, columnspan=3)
        self.tour = Label()
        self.couleur = str
        self.coul = str
        self.nomB = Label()
        self.nomN = Label()
        self.scoreB = Label()
        self.scoreN = Label()
        self.name()
# Initialisation de l'interface graphique et de ses widgets


    def name(self):
        self.winfo_toplevel().title("Othello")
# Nom de la fenêtre


    def getName(self):
        self.nomB = str(self.inputB.get())
        self.nomN = str(self.inputN.get())
        if self.partie.tour%2 == 0:
            return self.nomN
        else:
            return self.nomB
# Renvoie le nom du joueur dont c'est le tour.


    def lancenp(self, event):
        self.partie = Jeu()
        self.nomB = str(self.inputB.get())
        self.nomN = str(self.inputN.get())
        self.scoreB.destroy()
        self.scoreN.destroy()
        self.scoreB = Label(self, text="Score de {} = {}".format(self.nomB, self.partie.calculScore(COULEURS[2])))
        self.scoreN = Label(self, text="Score de {} = {}".format(self.nomN, self.partie.calculScore(COULEURS[1])))
        self.scoreB.grid(row=6, column=0)
        self.scoreN.grid(row=6, column=1)
        self.tour.destroy()
        self.tour = Label(self, text="c'est à {} de jouer".format(self.getName()))
        self.tour.grid(row=7, column=1)
        self.colorCanvas()
        self.tapi.bind('<Button-1>', self.coordClick)
# Lance la nouvelle partie en appelant la classe Jeu.


    def colorCanvas(self):
        i = 1
        while i < 9:
            j = 1
            while j < 9:
                self.tapi.create_rectangle(0+((i-1)*50), 0+((j-1)*50), 50+((i-1)*50), 50+((j-1)*50))
                if self.partie.plateau.grille[(j, i)] == COULEURS[2]:
                    self.coul = "white"
                elif self.partie.plateau.grille[(j, i)] == COULEURS[1]:
                    self.coul = "black"
                else:
                    self.coul = "green"
                if (j, i) in self.partie.plateau.ouJouer(self.partie.couleurAdverse()):
                    self.coul = "grey"
                self.tapi.create_oval(5 + ((i - 1) * 50), 5 + ((j - 1) * 50), 45 + ((i - 1) * 50), 45 + ((j - 1) * 50), fill=self.coul)
                j += 1
            i += 1
# Colorie le canvas. Va créer une grille de carrés et dans ceux-ci des cercles dont on change la couleur en fonction
#   de la grille définie par la classe Jeu


    def coordClick(self, event):
        coord = (event.y//50 + 1, event.x//50 + 1)
        if coord in self.partie.plateau.ouJouer(self.partie.couleurAdverse()):
            self.partie.jouer(coord)
            self.tour.destroy()
            self.tour = Label(self, text="C'est à {} de jouer".format(self.getName()))
            self.tour.grid(row=7, column=1)
            self.scoreN.destroy()
            self.scoreB.destroy()
            self.scoreB = Label(self, text="Score de {} = {}".format(self.nomB, self.partie.calculScore(COULEURS[2])))
            self.scoreN = Label(self, text="Score de {} = {}".format(self.nomN, self.partie.calculScore(COULEURS[1])))
            self.scoreB.grid(row=6, column=0)
            self.scoreN.grid(row=6, column=1)
            if len(self.partie.plateau.ouJouer(self.partie.couleurJoueur())) == 0 and len(self.partie.plateau.ouJouer(self.partie.couleurAdverse())) == 0:
                self.finPartie()
            elif len(self.partie.plateau.ouJouer(self.partie.couleurAdverse())) == 0:
                self.partie.changeTour()
                self.tour.destroy()
                self.tour = Label(self, text="Tu es bloqué, c'est à {} de jouer".format(self.getName()))
                self.tour.grid(row=7, column=1)
        self.colorCanvas()
# Coord sert à convertir l'endroit où on clique sur le canvas en un tuple de coordonnées utilisables par le jeu.


    def finPartie(self):
        self.partie.majscores(self.nomN, self.nomB)
        self.tour.destroy()
        scorefinB =  self.partie.calculScore(COULEURS[2])
        scorefinN =  self.partie.calculScore(COULEURS[1])
        if scorefinB > scorefinN:
            if scorefinB > self.scoremax[1]:
                self.tour = Label(text='Bravo à {} pour sa magnifique victoire et ce nouveau meilleur score !'.format(self.nomB))
            else:
                self.tour = Label(text='Bravo à {} pour sa magnifique victoire !'.format(self.nomB))

        if scorefinB < scorefinN:
            if scorefinN > self.scoremax[1]:
                self.tour = Label(text='Bravo à {} pour sa magnifique victoire et ce nouveau meilleur score !'.format(self.nomN))
            else:
                self.tour = Label(text='Bravo à {} pour sa magnifique victoire !'.format(self.nomN))

        elif scorefinB == scorefinN:
            self.tour = Label(text="Bravo pour cette belle partie mais c'est une égalité parfaite !")
            
        self.tour.grid(row=8, column=0, columnspan=3)
# Met fin à la partie


#####                                               Ce qu'on Run                                                   #####

othello = Graph()
othello.mainloop()

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