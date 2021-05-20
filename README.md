# projet_snake
programmation du jeu snake

## participants:
HARNOUFI Salah-Eddine
ENEKEYE BOAYEKAHO Karim Maurel
ISSOUF Haled
TANG Leon
CHERIF Nour
SISSOKO Abdullah
**chef de projet:
HARNOUFI SALAH EDDINE

## lien discord:

## Intervention extérieur:
Yingqin-SU, correction de plusieurs erreur de syntaxe

-------------------------------------

## Documentation:

Variables principales utilisés:

tableau: liste à 2d, contenant l'information sur le type de terrain

dessin: liste à 2d, contenant le quadrillage representée à l'écran

serpent: liste à 2d, contenant l'ensemble des coordonées du serpent

fruit: liste, contenant les coordonnées du fruit

direction: direction dans laquelle va le serpent
	# direction: haut [-1, 0], bas [1, 0], gauche [0, -1], droite [0 , 1]

game: booléun, indiquant si le jeu est est en cours ou non

vitesse: variable, définit la vitesse de déplacement du serpent

## Touches de contrôles:

les flèches directionnelles pour se déplacer ou
les touches visible a l'ecran

## Language de programmation:

python 3.8

## Modules importés:

tkinter, copy, random

------------------------------------------------

## comment jouer? 

Pour jouer il suffit de presser la touche "Démarrer", pour faire une pause il suffit d'appuyer sur la touche "arrêter" et pour recommencer
il suffit tout simplement d'appuyer sur la toucher "recommencer".


## régle du jeu:

obtenir le maximum de fruit sans toucher les murs ni soi même car sinon c'est perdu

à chaque fois que vous gagner un fruit votre score augmente et vous devenez plus grand

## personnaliser la vitesse

3 vitesses sont disponibles, lent, normal, rapide; avant chaque début de partie il vous suffit d'appuyer sur un de ces touches pour en changer la vitesse


##

Le score et la vitesse sont afficher à l'écran, bonne partie !

-----------------------------------------------------

## Evolution du code

vous pouvez modifier la vitesse via la variable vitesse, par exemple
pour créer différents niveau qui vont de plus en plus vite

aussi, vous pouvez modifier la taille du quadrillage en 2 temps :..
d'un part en modifiant l'appel de la fonction quadrillage..
tableau, dessin = quadrillage(17, 17)..
ici le quadrillage est de 17 * 17 et en modifiant dans la fonction game_loose()..
lorsqu'on reset le terrain.

## Evolution de l'esthetique

Par défault l'esthetique n'est pas le plus intéressant et c'est le but..
il vaut mieux laisser un esthethique relativement faible..
pour laisser le code clair et aussi pour se concentrer sur l'essentiel..
les fonctionnalités,

On pourrait mettre le code dit esthetique dans un fichier de code différent,
qui reprend exactement le code base et en y ajoutant les surchouches esthetique..
de telle manière le code n'est pas surchargé, on peut repartir le travail facilement..
un qui se concentre sur l'apparence, un autre sur l'apparence, design/moteur
et plus important encore le code est bien plus facile a faire évolué

Par exemple, on pourrait personnaliser les boutons de vitesse tel que..
lorsque l'on appuie sur un des boutons de vitesse, celui-ci change de couleur..
etc... on pourrait meme rajouter un son, une animation etc.. jusqu'à l'infini

