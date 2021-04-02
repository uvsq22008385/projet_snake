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
# modules importés: tkinter
# import tkinter as tk

#####################
# Constantes

#####################
# Variables globales

#####################
# Fonctions principales


def quadrillage(n, m):
    '''creer un tableau de dimension n*m'''

    tableau = []

    for i in range(n):
        tableau.append([])
        for a in range(m):
            if i in [0, n-1] or a in [0, n-1]:
                tableau[i].append(0)
            else:
                tableau[i].append(1)

    return tableau


def afficher_tableau(tableau):
    '''affiche le tableau de manière formatté'''
    for element in (tableau):
        for thing in element:
            print(thing, end=' ')
        print('\n')


####################
# Programme principale

tableau = quadrillage(5, 5)

afficher_tableau(tableau)
