------------Introduction----------
J'ai réalisé un jeu de plateforme en 2D avec le langage Python et la librairie
Pygame. J'ai programmé ce jeu avec l'IDE Pycharm. Pour les graphismes, je les ai fait
moi-même avec PixelEdit principalement.


------------Déroulement du jeu-----------------

	---menu/gameover---
	------------------
Au lancement du projet, on arrive directement sur le menu. 
On peut choisir de sélectionner un item avec les flèches Up et Down du clavier. Pour
activer l'item sélectionné il faut cliquer sur la touche entrée du clavier.

Ce sera également le cas pour l'écran de Gameover.


	------Jeu------
	---------------
Si on a choisi l'item "Play" dans le menu, on arrive ensuite sur l'écran de jeu.

	----déplacements du personnage----
Nous incarnons un personnage blanc. On peut le déplacer de gauche à droite avec les
flèches Right et Left du clavier. On peut également le faire sauter en cliquant sur
la barre espace du clavier mais uniquement si notre personnage n'est pas sur une 
échelle ou sur une corde.

On peut déplacer notre personnage quand il est sur une échelle avec les flèches Up
et Down du clavier.

Si notre personnage est sur une corde, on peut le déplacer de gauche à droite. On
peut également le faire tomber si nécessaire en le détachant de la corde en cliquant
sur la flèche Down du clavier.

	--creuser--
On peut creuser des trous dans la map en cliquant sur la touche "s" du clavier. Si
notre personnage est tourné à droite on creusera un trou à droite, si notre 
personnage est tourné à gauche on creusera à gauche. Attention on peut creuser 
uniquement si le sol est en brique.

Notre personnage peut passer à travers un trou sans problème. 
Attention si ce trou ce trouvent sur la dernière ligne de la map, notre personnage 
en le traversant mourra.

Quand on creuse, au bout d'un certain temps le trou ce referme automatiquement.
Il faut faire attention que notre personnage ne passe pas à travers un trou au 
moment où il se referme parce que sinon il mourra.

	
	---ennemis---
Les ennemies ce balade dans la map de manière aléatoire. Si notre personnage touche
un ennemi, il meurt et donc l'écran gameover s'affiche.

Si un ennemie tombe dans un trou, au bout d'un certain temps il va pouvoir sortir de
ce trou. A ce moment là, il continue sa route et le trou ce referme.


	----briques de couleur----
Il y a dans la map, des tuiles de couleurs. C'est tuiles sont particulières dans le 
sens où les collisions fonctionneront uniquement si notre personnage est de la même
couleur que la tuile en question.

Si notre personnage n'est pas de la même couleur que les tuiles alors celle-ci 
seront semi-transparente.

Pour que notre personnage change de couleur, il suffit de ramasser un pot de peinture
plaçait dans la map. Il existe plusieurs pots de peinture de différentes couleurs:
blanc,rouge,jaune et bleu.

Si on ramasse un pot de peinture blanc, notre personnage redeviendra blanc
dans tout les cas.

On peut mélanger les couleurs si on ramasse plusieurs pots de peintures:

-blanc=personnage blanc(dans tout les cas)

-seulement rouge=personnage rouge,
-seulement bleu=personnage bleu,
-seulement jaune=personnage jaune,

-rouge+bleu=violet,
-bleu+jaune=vert,
-rouge+jaune=orange,

Si on mélange plus de trois couleurs(sans passer par le blanc), 
notre personnage deviendra marron.



	---changement de niveau----

Pour ce rendre au niveau suivant, il faut ramasser toutes les clés à molette plaçaient
dans la map.
Une fois que notre personnage a ramassé toutes les clés à molette de la map, une 
échelle s'affiche vers le haut de l'écran de jeu.

Il suffit de prendre cette échelle pour accéder au niveau suivant. Si il n'y a plus de 
niveau a visiter, c'est l'écran de menu qui s'affichera.
	
