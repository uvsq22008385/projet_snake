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
    racine.after(3000, lambda: mouvement_automatique())


def affichage_score():
    global score

    score += 1

    afficher = "score:" + str(score)

    print(afficher)

    label.configure(text=afficher)


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
    global direction, serpent, tableau, dessin, nmur, mmur, fruit

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

            canvas.itemconfigure(dessin[fruit[0]][fruit[1]], fill="yellow")

        else:
            a = serpent[-1][0]
            b = serpent[-1][1]

            serpent[1:] = copy.deepcopy(serpent[:-1])

            # l'anciene position de la queue du serpent redevient du terrain
            tableau[a][b] = 1

            canvas.itemconfigure(dessin[a][b], fill="pink")

            serpent[0] = copy.deepcopy([A, B])

        if tableau[A][B] == 0:
            game_loose()
        else:
            tableau[A][B] = 3

            canvas.itemconfigure(dessin[A][B], fill="red")

    afficher_tableau(tableau)


def quadrillage(n, m):
    '''creer un tableau de dimension n*m'''
    global nmur, mmur, fruit

    fruit = creation_fruit(n - 2, m - 2)

    nmur = n - 1
    mmur = m - 1

    tableau = []
    dessin = []

    for i in range(n):
        tableau.append([])
        dessin.append([])
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

            taille_case_x = 500/n
            taille_case_y = 500/m

            x0 = a * taille_case_x
            y0 = i * taille_case_y
            x1 = (a + 1) * taille_case_x
            y1 = (i + 1) * taille_case_y

            if k == 1:
                color = "pink"
            elif k == 3:
                color = "red"
            elif k == 5:
                color = "yellow"
            elif k == 0:
                color = "blue"

            dessin[i].append(canvas.create_rectangle((x0, y0), (x1, y1), fill=color))

    return tableau, dessin


def afficher_tableau(tableau):
    '''affiche le tableau de manière formatté'''
    for element in (tableau):
        for thing in element:
            print(thing, end=' ')
        print('\n')


####################
# Programme principale

racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="white")
canvas.grid()

label = tk.Label(racine, text="score:0")
label.grid()


tableau, dessin = quadrillage(10, 10)


afficher_tableau(tableau)


mouvement_automatique()

haut = tk.Button(racine, text="^", command=lambda: move([-1, 0])).grid()
droite = tk.Button(racine, text=">", command=lambda: move([0, 1])).grid()
bas = tk.Button(racine, text="v", command=lambda: move([1, 0])).grid()
gauche = tk.Button(racine, text="<", command=lambda: move([0, -1])).grid()


racine.mainloop()
