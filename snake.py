###############################
# nom du projet: snake
# groupe de td: 5
# participants:
#   HARNOUFI Salah-Eddine (chef projet/syntaxe)
#   ENEKEYE BOAYEKAHO Karim Maurel
#   ISSOUF Haled
#   TANG Leon
#   CHERIF Nour
#   SISSOKO Abdullah
###############################

######################
# modules importés: tkinter, random
import tkinter as tk
import random
import copy

#####################
# Constantes

#####################
# Variables globales

# position initiale du serpent
serpent = [[1, 2], [1, 1], [2, 1]]

# direction initiale du serpent
direction = [0, 1]


# direction: haut,       droite
#             [-1, 0]     [0 , 1]
#              bas,      gauche
#             [1, 0]     [0 , -1]

# note: on remonte en negatif


score = 0


#####################
# Fonctions principales


def mouvement_automatique():
    global direction
    move(direction)
    racine.after(1000, lambda: mouvement_automatique())


def affichage_score():
    global score

    score += 1

    print("score:", score)


def creation_fruit(nzone, mzone):
    '''creation d'un fruit a une position aleatoire'''
    global serpent

    # on verifie que le serpent n'est pas a cette position
    t = True

    while t:

        c, d = random.randint(1, nzone), random.randint(1, mzone)

        t = False
        for element in serpent:
            if element == [c, d]:
                t = True

    return [c, d]


def game_loose():
    print("game over")


def move(fleche):
    '''deplace le serpent sur la tableau'''
    global direction, serpent, tableau, nmur, mmur, fruit

    if [direction[0] + fleche[0], direction[1] + fleche[1]] == [0, 0]:
        pass
        # on ne fait rien
    else:

        direction = fleche

        A, B = serpent[0][0] + fleche[0], serpent[0][1] + fleche[1]

        for element in serpent:
            if element == [A, B]:
                game_loose()

        if fruit == [A, B]:
            # si on touche le fruit
            serpent[1:] = copy.deepcopy(serpent)
            serpent[0] = copy.deepcopy([A, B])

            affichage_score()

            fruit = creation_fruit(nmur-1, mmur-1)
            tableau[fruit[0]][fruit[1]] = 5

        else:
            a = serpent[-1][0]
            b = serpent[-1][1]

            serpent[1:] = copy.deepcopy(serpent[:-1])

            # l'anciene position de la queue du serpent redevient du terrain
            tableau[a][b] = 1

            serpent[0] = copy.deepcopy([A, B])

        if tableau[A][B] == 0:
            game_loose()
        else:
            tableau[A][B] = 3

    afficher_tableau(tableau)


def quadrillage(n, m):
    '''creer un tableau de dimension n*m'''
    global nmur, mmur, fruit

    fruit = creation_fruit(n - 2, m - 2)

    nmur = n - 1
    mmur = m - 1

    tableau = []

    for i in range(n):
        tableau.append([])
        for a in range(m):
            k = 1

            for element in serpent:
                if element == [i, a]:
                    k = 3

            if [i, a] == fruit:
                k = 5

            if k != 3:
                if i in [0, n-1] or a in [0, m-1]:
                    k = 0

            tableau[i].append(k)

    return tableau


def afficher_tableau(tableau):
    '''affiche le tableau de manière formatté'''
    for element in (tableau):
        for thing in element:
            print(thing, end=' ')
        print('\n')


####################
# Programme principale
tableau = quadrillage(10, 10)


afficher_tableau(tableau)

racine = tk.Tk()

mouvement_automatique()

haut = tk.Button(racine, text="^", command=lambda: move([-1, 0])).grid()
droite = tk.Button(racine, text=">", command=lambda: move([0, 1])).grid()
bas = tk.Button(racine, text="v", command=lambda: move([1, 0])).grid()
gauche = tk.Button(racine, text="<", command=lambda: move([0, -1])).grid()


racine.mainloop()
