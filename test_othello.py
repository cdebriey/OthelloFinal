import unittest
from Plateau import *
from Game import *


class TestPlateau(unittest.TestCase):

    def test_placePion(self):
        P=Plateau()
        Move1= P.placePion((5, 2), COULEURS[1])
        Move2= P.placePion((4, 4), COULEURS[2])
        Move3= P.placePion((4, 5), COULEURS[0])
        Move4= P.placePion((5, 4), COULEURS[2])
        Move5= P.placePion((8, 4), COULEURS[1])
        Move6= P.placePion((2, 2), COULEURS[0])
        self.assertEqual(Move1,'black')
        self.assertEqual(Move2,'white')
        self.assertEqual(Move3,'')
        self.assertEqual(Move4,'white')
        self.assertEqual(Move5,'black')
        self.assertEqual(Move6,'')

        #Test la fonction placePion de Plateau: vérifie si la case a la bonne couleur

    def test_estvide(self):
        V= Plateau()
        V.placePion((5, 2), COULEURS[0])
        V.placePion((4, 4), COULEURS[0])
        V.placePion((4, 5), COULEURS[0])
        V.placePion((5, 4), COULEURS[1])
        V.placePion((8, 4), COULEURS[2])
        V.placePion((2, 2), COULEURS[1])
        Vide1= V.estVide((5, 2))
        Vide2= V.estVide((4, 4))
        Vide3= V.estVide((4, 5))
        Vide4= V.estVide((5, 4))
        Vide5= V.estVide((2, 2))
        Vide6= V.estVide((8, 4))
        self.assertTrue(Vide1)
        self.assertTrue(Vide2)
        self.assertTrue(Vide3)
        self.assertFalse(Vide4)
        self.assertFalse(Vide5)
        self.assertFalse(Vide6)

        #Test la fonction estVide de Plateau: vérifie si la case est vide ou non

    
    def test_estAdj(self):
        A= Plateau()
        A.placePion((4,4), COULEURS[1])
        Adjacent1= A.estAdj((4,5), 'black')
        Adjacent2= A.estAdj((4,3), 'black')
        Adjacent3= A.estAdj((3,4), 'black')
        Adjacent4= A.estAdj((5,4), 'black')
        self.assertTrue(Adjacent1)
        self.assertTrue(Adjacent2)
        self.assertTrue(Adjacent3)
        self.assertTrue(Adjacent4)

        #Test la fonction estAdj de Plateau: vérifie si une case est adjacente et a la même couleur que
        # celle en argurment 
    
    def test_encadre(self):
        E= Plateau()
        E.placePion((4, 4), COULEURS[2])
        E.placePion((4, 5), COULEURS[1])
        E.placePion((5, 4), COULEURS[1])
        E.placePion((5, 5), COULEURS[2])
        Encadre1= E.encadre((4,4),(1,0),'black')
        self.assertFalse(Encadre1)

        #Test la fonction encadre de Plateau: vérifie dans la direction donnée si le premier pion rencontré 
        # depuis la coordonnée donnée en argument est de la
        # couleur donnée en argument. Doit renvoyer False si case Vide ou au bord du tableau

    
    def test_encadre2(self):
        E= Plateau()
        E.placePion((3, 5), COULEURS[1])
        E.placePion((4, 5), COULEURS[2])
        E.placePion((5, 5), COULEURS[2])
        Encadre2= E.encadre((5,5),(-1,0),'white')
        self.assertTrue(Encadre2)
        #Test la fonction encadre de Plateau: vérifie dans la direction donnée si le premier pion rencontré 
        # depuis la coordonnée donnée en argument est de la
        # couleur donnée en argument. Doit renvoyer True si on tombe sur une case de l'autre couleur

    
    def test_rempla(self):
        R= Plateau()
        R.placePion((2, 6), COULEURS[2])
        R.placePion((2, 7), COULEURS[1])
        R.placePion((3, 6), COULEURS[1])
        R.placePion((3, 7), COULEURS[2])
        self.assertIsNone(R.rempla((2,6),(0,1),'black'))
        # Test la fonction rempla de Plateau: La fonction vérifie que la première case dans la direction donnée 
        # en argument depuis la coordonnée donnée en argument
        #est de la couleur donnée en argument. Si oui, elle en change la couleur  et recommence
        #une case plus loin. Sinon, elle s'arrête.
    

    def test_ouJouer(self):
        J= Plateau()
        J.placePion((4, 4), COULEURS[2])
        J.placePion((4, 5), COULEURS[1])
        J.placePion((5, 4), COULEURS[1])
        J.placePion((5, 5), COULEURS[2])
        Possib1= J.ouJouer('black')
        self.assertEqual(Possib1,[(5, 3), (6, 4), (3, 5), (4, 6)])
        # Test la fonction ouJouer de Plateau: Renvoie une liste de tuple. 
        # Ces tuples sont les cases où on peut jouer


    
    def test_couleurJouer(self):
        J = Jeu()
        Couleur = J.couleurJoueur()
        self.assertEqual(Couleur,'black')
        #Test la fonction couleurJoueur de Game: Doit être black car premier tour

    def test_couleurAdverser(self):
        J= Jeu()
        CouleurAdv = J.couleurAdverse()
        self.assertEqual(CouleurAdv,'white')
        #Test la fonction couleurAdv de Game: Doit être white car c'est la couleur adverse de black
        #au premier tour
    
    def test_calculScore(self):
        J=Jeu()
        Scoreblack = J.calculScore('black')
        Scorewhite= J.calculScore('white')
        self.assertEqual(Scoreblack,2)
        self.assertEqual(Scorewhite,2)
        #Test la fonction calculScore de Game: Au début de partie, les deux joueurs
        #sont à deux points chacun
    
    def test_calculScore2(self):
        J= Jeu()
        J.jouer((4,3))
        J.jouer((3,5))
        Scoreblack2 = J.calculScore('black')
        Scorewhite2= J.calculScore('white')
        self.assertEqual(Scoreblack2,3)
        self.assertEqual(Scorewhite2,3)
        #Test la fonction calculScore de Game: Après avoir joué chacun une fois,
        #les deux joueurs sont à 3 points partout
    
 
    def test_jouer(self):
        J=Jeu()
        Jouer1 = J.jouer((4,3))
        Jouer2= J.jouer((3,5))
        self.assertEqual(Jouer1,(4,3))
        self.assertEqual(Jouer2,(3,5))
        #Test la fonction jouer de Game: vérifie si le joueur a bien joué un tour à la bonne
        #coordonnée
    
    def test_getHscore(self):
        J=Jeu()
        Hscore= J.getHscore()
        self.assertEqual(Hscore, ['Ben', 56])
        #Test la fonction jouer de getHscore: vérifie si le meilleur score sur toutes les parties


if __name__ == '__main__':
    unittest.main()