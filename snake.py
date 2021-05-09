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

game = False

vitesse = 200


#####################
# Fonctions principales

def changementVitesse(vit):
    global vitesse
    if not game and score == 0:
        vitesse = vit
        affiche = "lent"
        if vit == 200:
            affiche = "normal"
        elif vit == 100:
            affiche = "rapide"
        quelVitesse.configure(text="vitesse:" + affiche)


def pause():
    global game, speed, vitesse

    if game:
        game = False
        bouton.configure(text="démarrer")
    else:
        game = True
        bouton.configure(text="arrêter")
        racine.after(1500, lambda: mouvement_automatique())


def mouvement_automatique():
    global game, vitesse
    if game:
        move()
        racine.after(vitesse, lambda: mouvement_automatique())


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
    global serpent, direction, score, game, tableau, dessin

    bouton.configure(text="recommencer")
    label.configure(text="Vous avez perdu, votre score est:"+str(score))

    # variable a reset

    serpent = [[1, 2], [1, 1], [2, 1]]

    direction = [0, 1]

    score = 0

    game = False

    tableau = []
    dessin = []

    canvas.delete("all")

    tableau, dessin = quadrillage(17, 17)


def changementDirection(fleche):
    '''change la direction dans laquelle se déplace le snake
    sauf s'il c'est dans la direction opposée'''
    global direction
    if game:
        if [direction[0] + fleche[0], direction[1] + fleche[1]] != [0, 0]:
            direction = fleche


def move():
    '''deplace le serpent sur la tableau'''
    global direction, serpent, tableau, dessin, nmur, mmur, fruit, game

    if game:

        A, B = serpent[0][0] + direction[0], serpent[0][1] + direction[1]

        defaite = False

        if tableau[A][B] == 0:
            defaite = True
        else:
            tableau[A][B] = 3

            canvas.itemconfigure(dessin[A][B], fill="red")

        for element in serpent:
            if element == [A, B]:
                defaite = True
                break

        if defaite:
            game_loose()
        else:

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


tableau, dessin = quadrillage(17, 17)


afficher_tableau(tableau)

bouton = tk.Button(racine, text="démarrer", command=lambda: pause())
bouton.grid()


haut = tk.Button(racine, text="^", command=lambda: changementDirection([-1, 0])).grid()
droite = tk.Button(racine, text=">", command=lambda: changementDirection([0, 1])).grid()
bas = tk.Button(racine, text="v", command=lambda: changementDirection([1, 0])).grid()
gauche = tk.Button(racine, text="<", command=lambda: changementDirection([0, -1])).grid()

lent = tk.Button(racine, text="lent", command=lambda: changementVitesse(500))
lent.grid()

normal = tk.Button(racine, text="normal", command=lambda: changementVitesse(200))
normal.grid()

rapide = tk.Button(racine, text="rapide", command=lambda: changementVitesse(100))
rapide.grid()

quelVitesse = tk.Label(racine, text="le code de Salah")
quelVitesse.grid()

racine.bind("<Up>", lambda event: changementDirection([-1, 0]))
racine.bind("<Right>", lambda event: changementDirection([0, 1]))
racine.bind("<Down>", lambda event: changementDirection([1, 0]))
racine.bind("<Left>", lambda event: changementDirection([0, -1]))

racine.mainloop()
