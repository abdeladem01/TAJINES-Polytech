# Binome: Abdeladem Saoud Fattah - Marouane Boubia              ##                                                                                                                                                   Bînome : Fattah Abdeladem Saoud - Boubia Marouane
 ##################################################################
  ### Ensemble des Programmes ### ###  Abdeladem Saoud Fattah  ###
   ##         du Jeu          ##   ##      Marouane Boubia     ##
    #       de Quilles        # ||| #         Groupe 5         #
     #########################       ##########################
from turtle import*
from tkinter import messagebox
import time
setup(1200,650)
title("Tajines : Le JEU")
tracer(100,50)
#Fonctions pour dessiner le fond, le soleil et les nuages###################
def FondCieletTerre():
  fillcolor("#00FF27")
  up()
  goto(-2000,20)
  pos1=pos()
  begin_fill()
  goto(2000,20)
  pos2=pos()
  goto(2000,-1000)
  goto(-2000,-1000)
  goto(pos1)
  end_fill()
  fillcolor("#18ECEF")
  goto(pos1)
  begin_fill()
  goto(pos2)
  goto(2000,1000)
  goto(-2000,1000)
  goto(pos1)
  end_fill()
def soleil(x,y):
  up()
  seth(0)
  goto(x,y)
  color("yellow")
  begin_fill()
  circle(120)
  end_fill()
  color("black")

def nuage(x,y):
  setheading(0)
  up()
  goto(x,y)
  down()
  pencolor("white")
  fillcolor("white")
  begin_fill()
  circle(20,180)
  right(100)
  circle(30,180)
  right(100)
  circle(35,180)
  right(70)
  circle(20,180)
  setheading(290)
  circle(30,180)
  setheading(280)
  circle(20,180)
  setheading(90)
  circle(30)
  pencolor("black")
  end_fill()
  up()
  seth(0)
def tomate(x,y,p):
    i=0
    xinitial=x
    yinitial=y
    j=0
    v=100
    while j<3 :
        while i<4:
            color("red")
            up()
            fillcolor("red")
            begin_fill()
            goto(x,y)
            down()
            circle(10*p,360)
            end_fill()
            color("#1C6108")
            up()
            goto(x+5,(y+15))
            color("#1C6108")
            down()
            width(4)
            circle(-2*p,90)
            seth(90)
            circle(-3*p,60)
            x-=v
            y-=50
            p*=1.2
            i+=1
        j+=1
        i=0
        p=1
        v-=100
        if j==1:
            x=xinitial+250
        else :
            x=xinitial+500
        y=yinitial
def herbe(x,y,p):
    v=100
    j=0
    i=0
    xinitial=x
    yinitial=y
    while j<4:
        i=0
        while i<4:
            up()
            goto(x,y)
            color("#00980C")
            down()
            seth(0)
            width(4)
            circle(-10*p,90)
            seth(90)
            circle(-15*p,60)
            x-=v
            y-=50
            p*=1.2
            i+=1
        j+=1
        p=1
        if j==1:
            v=10
            x=xinitial+250
        elif j==2:
            v=-10
            x=xinitial+400
        elif j==3:
            v=-100
            x=xinitial+700
        y=yinitial

#Fonction afin de dessiner les quilles (Tajines)######################
def BasTagine(x,y,p):
  fillcolor("saddlebrown")
  begin_fill()
  up()
  goto(x,y)
  down()
  right(30)
  forward(10*p)
  left(30)
  forward(30*p)
  left(30)
  forward(10*p)
  right(30)
  goto(x,y)
  end_fill()
  fillcolor("chocolate")
  begin_fill()
  up()
  goto(x,y)
  down()
  forward(50*p)
  circle(8.5*p,180)
  forward(50*p)
  circle(8.5*p,180)
  end_fill()

def HautTajine(x,y,p):
  setheading(0)
  fillcolor("saddlebrown")
  up()
  goto(x,y+17*p)
  begin_fill()
  left(45)
  down()
  forward(35.355*p)
  right(90)
  down()
  forward(35.355*p)
  setheading(-180)
  forward(50*p)
  end_fill()
  #On reprendra la fonctionBasTajine après avec dimensions reduites
  setheading(0) #On reste l'angle pour 0°
  fillcolor("chocolate")
  up()
  goto(x+20*p,y+40*p)
  begin_fill()
  down()
  forward(10*p)
  circle(3*p,180)
  forward(10*p)
  circle(3*p,180)
  end_fill()
  up()
#On a besoin de 3 fontions pour dessiner le haut du tajine:
def triangle(x,y,p): #Fonction 1 : Triangle Tajine
  up()
  goto(x,y)
  down()
  fillcolor("saddlebrown")
  begin_fill()
  forward(36*p)
  left(120)
  forward(20*p)
  left(93.559)
  forward(32*p)
  end_fill()

def ovalTajine(r,p): #Fonction 2 : Lt7t dial tajine
    setheading(0)
    right(45)
    for boucle in range(2):
        circle(r*p,90)
        circle((r*p)/20,90)

def chapeauTajine(x,y,p): #Fonction 3 : L9bda dial tajine
  setheading(0)
  up()
  goto(x+23*p,y+15*p)
  down()
  fillcolor("chocolate")
  begin_fill()
  forward(6*p)
  circle(1.5*p,180)
  forward(6*p)
  circle(1.5*p,180)
  end_fill()

def HautTajineOuvert(x,y,p):
  setheading(0)
  triangle(x+30,y+30,p)
  fillcolor("maroon")
  begin_fill()
  ovalTajine(25,p)
  end_fill()
  chapeauTajine((x+30),(y+30),p)

#Fonctions pour dessiner le four##################################
def calligraphie():
  up()
  goto(0,140)
  color("#ffd700")
  write("بوليطيك مطعم",move=False, align="center", font=("AlHor", 40, "bold"))
  up()
  goto(0,100)
  write("Tajines Polytech", move=False, align="center", font=("FreeSerif", 40, "bold"))
  goto(-270,80)
  seth(0)
  down()
  fd(40)
  up()
  fd(10)
  sety(70)
  write("Spécialités marocaines depuis 2005", move=True, align="left", font=("Liberation Serif", 20, "bold"))
  sety(80)
  fd(10)
  down()
  fd(40)
def background(x,y): #je defini le mur en pierre du bk
  setup(1200,650)
  pensize(3)
  up()
  goto(x,y)
  down()
  fillcolor("brown")
  begin_fill()
  right(90)
  forward(260)
  left(90)
  forward(70)
  left(90)
  forward(120)
  right(90)
  forward(915)
  right(90)
  forward(120)
  left(90)
  forward(70)
  left(90)
  forward(260)
  left(90)
  forward(1050)
  end_fill()

def perspective(x,y):
  seth(0)
  up()
  goto(x,y)
  down()
  left(45)
  forward(50)
  position1=pos()
  right(45)
  forward(844.3)
  position2=pos()
  right(45)
  forward(50)
  left(45)
  up()
  goto(position1) #Etape repetitive à faire avec un while et chaine de caractere
  down()
  seth(90)
  forward(84.64)
  position11=pos()
  up()
  goto(position2)
  down()
  forward(84.64)
  position22=pos() #Fin duwhile à faire
  up()
  goto(x,y) #coloriage coté gauche
  fillcolor("#6C1C12")
  begin_fill()
  goto(position1)
  goto(position11)
  goto(x,y+120)
  goto(x,y)
  end_fill()
  goto(x+844.3,y) #coloriage coté droit
  begin_fill()
  goto(position2)
  goto(position22)
  goto(x+915,y+120)
  goto(x+915,y)
  goto(position2)
  end_fill()
  fillcolor("#7B241C")
  begin_fill()
  goto(position1) #Coloriage Milieu
  goto(position11)
  goto(position22)
  goto(position2)
  goto(position1)
  end_fill()



def ptitCarreauCoteGauche(x,y):
  width(0.8)
  i=1
  ord=y
  seth(45)
  while i<5 :
    up()
    ord=ord+20.5
    goto(x,ord)
    down()
    fd(50)
    i+=1
  up()
  ord=ord+20
  goto(x,ord)
  down()
  fd(25.5)
  ord=y
  j=0
  while j<3:
    up()
    seth(45)
    goto(x,ord)
    fd(25)
    down()
    seth(90)
    fd(20.5)
    positionsupp=pos()
    ord+=41
    j+=1
  j=0
  ord=y+20.5
  while j<2:
    up()
    goto(x,ord)
    seth(45)
    fd(12.5)
    seth(90)
    down()
    fd(20.5)
    up()
    bk(20.5)
    right(45)
    fd(25)
    left(45)
    down()
    fd(20.5)
    ord+=41
    j+=1
  up()
  goto(positionsupp)
  seth(45)
  bk(12.5)
  left(45)
  down()
  fd(9)

def ptitCarreauCoteDroit(x,y):
  width(0.8)
  i=1
  ord=y
  seth(-45)
  abs=x+260
  while i<5 :
    up()
    ord=ord+20.5
    goto(abs,ord)
    down()
    bk(50)
    i+=1
  up()
  ord=ord+20
  goto(abs,ord)
  down()
  bk(25.5)
  j=0
  ord=y
  while j<3:
    up()
    seth(-45)
    goto(abs,ord)
    bk(25)
    down()
    seth(90)
    fd(20.5)
    positionsupp=pos()
    ord+=41
    j+=1
  j=0
  ord=y+20.5
  while j<2:
    up()
    goto(abs,ord)
    seth(-45)
    bk(12.5)
    seth(90)
    down()
    fd(20.5)
    up()
    bk(20.5)
    right(135)
    bk(25)
    left(135)
    down()
    fd(20.5)
    ord+=41
    j+=1
  up()
  goto(positionsupp)
  seth(-45)
  fd(12.5)
  left(135)
  down()
  fd(9)
  


def socle(x,y): #je defini le socle
  up()
  goto(x,y)
  down()
  fillcolor("#2D2929")
  begin_fill()
  seth(-90)
  forward(50)
  left(90)
  forward(20)
  sauvegarde1=pos()
  left(90)
  forward(20)
  sauvegarde11=pos()
  right(90)
  forward(808.95)
  sauvegarde22=pos()
  right(90)
  forward(20)
  sauvegarde2=pos()
  left(90)
  forward(20)
  left(90)
  forward(50)
  left(90)
  forward(850)
  end_fill()
  fillcolor("#4F4646")
  begin_fill()#Perspective haut
  seth(45)
  fd(10)
  right(45)
  fd(835)
  right(45)
  fd(10)
  seth(180)
  up()
  fd(850)
  end_fill()#Fin perspective haut
  goto(sauvegarde1)
  begin_fill()#perspective gauche
  down()
  seth(45)
  fd(7)
  left(45)
  fd(15)
  up()
  goto(sauvegarde11)
  goto(sauvegarde1)
  end_fill()#Fin perspective gauche
  goto(sauvegarde2)
  begin_fill()#perspective droite
  down()
  seth(135)
  fd(7)
  right(45)
  fd(15)
  up()
  goto(sauvegarde22)
  goto(sauvegarde2)
  end_fill()#Fin perspective droite


#je defini les petits carreau en pierre du mur
#les 4 procédures qui suivent sert à définir les "colonnes" de notre mur
def petitCarreau(x,y):
  seth(-90)
  j=0
  while j<4:
    i=0
    while i<20:
      up()
      goto(x,y)
      down()
      forward(20)
      x+=50
      i+=1
    x=-475
    y-=40
    j+=1


def petitCarreauvide(x,y):
  j=0
  while j<3:
    i=0
    while i<2:
      up()
      goto(x,y)
      down()
      forward(20)
      x+=950
      i+=1
    x=-475
    y-=40
    j+=1


def petitCarreau2(x,y):
  j=0
  while j<3:
    i=0
    while i<21:
      up()
      goto(x,y)
      down()
      forward(20)
      x+=50
      i+=1
    x=-500
    y-=40
    j+=1


def petitCarreau2vide(x,y):
  j=0
  while j<3:
    i=0
    while i<2:
      up()
      goto(x,y)
      down()
      forward(20)
      x+=1000
      i+=1
    x=-500
    y-=40
    j+=1


#les 2 fonctions qui suivent servent à dessiner les lignes de notre mur de pierre
def ligneCarreau(x,y):
  seth(0)
  i=0
  while i<7:
    up()
    goto(x,y)
    down()
    forward(1055)
    y-=20
    i+=1


def lignevideCarreau(x,y):
  seth(0)
  i=1
  while i<6:
    up()
    goto(x,y)
    down()
    forward(70)
    up()
    goto(x+985,y)
    down()
    forward(70)
    y-=20
    i+=1

def four(): #Fonction unissant tous les éléments du decor
  background(-525,200)
  pensize(1)
  perspective(-455,-60)
  ptitCarreauCoteGauche(-455,-60)
  ptitCarreauCoteDroit(200,-60)
  width(1)
  socle(-419.6,-10)
  pensize(1)
  petitCarreau(-475,200)
  petitCarreauvide(-475,40)
  petitCarreau2(-500,180)
  petitCarreau2vide(-500,60)
  ligneCarreau(-525,180)
  lignevideCarreau(-525,40)

#####################################################################################
import random  #On importe random qui nous sera utile pour le tour de l'ordinateur
###########Partie 1##################################################################
#Programme 1 : Affichage des quilles :
def afficheQuilles(q,NTotal):    #q est la liste des quilles debouts et NTotal est le nombre de quilles totales
    v=0 #Etant donné qu'on va effectué une verification de gauche à droite, k est 0 au début, sa valeur va avancer dans la boucle while (ligne 24)
    ligne=[] #ligne est une liste vierge
    quilles=""
    for liste in q:
          j=liste[0] #j prend donc la valeur la petite de l'intervalle [deb,fin]
          while j<=liste[1]:
              if j not in ligne:
                  ligne.append(j) #Ajouter à la liste ligne (vierge au début la valeur de j, si j n'y est pas déja)
              j+=1
    while v<NTotal:  #On commence ainsi la vérification de gauche à droite dont j'ai parlé en commentaire dans la ligne 12
        if v in ligne : 
            quilles=quilles+"|"   #Si k appartient à la liste des lignes (quilles debout) alors afficher une quille
        else :
            quilles=quilles+"."   #Dans ce cas, la quille est représentée par un point car elle n'appartient pas à la liste, conséquence du fait qu'elle est tombée
        v+=1
    return quilles 

#Programme 2: Tour de l'ordinateur : 
def ordijoue(q):
  p=str(random.choice(["G","M","D"])) 
  #L'ordi choisi entre Gauche Milieu Droite (str pour string c-a-d chaine de car)
  L=len(q)
  i=str(random.randint(1,L)) #L'odri choisi au hasard un entier entre 1 et L
  v=i+":"+p
  return v

#Programme 3: Tour du joueur :
def joueurJoue(q):
  l=int(numinput("Tajines : LE JEU","Choisissez un numéro de ligne : ")) #l pour ligne.
  while (l<1 or l>len(q))  :
    l=int(numinput("Tajines : LE JEU","Erreur, vous avez entré un mauvais numéro de ligne, veuillez rechoisir un numéro de ligne : "))
  p=str(textinput("Tajines : LE JEU","Choisissez une position parmi" '\n\n' " M (milieu) , G (gauche) et D (droite) : ")) #p pour position ou endroit de tir.
  while p!="G" and p!="M" and p!="D" : 
    p=str(textinput("Tajines : LE JEU","Erreur, vous avez séléctionné précedemment une mauvaise position. " '\n\n' "Choisissez une nouvelle position parmi M (milieu) , G (gauche) et D (droite) : "))
  v=str(l)+":"+p 
  return v

#Programme 4: Fonction du jeu :
#Afin de simplifier le travail, On va définir 3 fonctions : jouerC sur le coté(droite ou gauche) et jouerM sur le milieu et jouer qui combine les deux programmes d'avant.

#Sous procédure 1 : Si on joue G ou D :
def jouerCote(c,q):
    l=len(q)
    ligneChoisie=int(c[0]) #Etant donné que 'c' est écrit sous la forme i:P, ligneChoisi = i qui est la ligne choisi par l'ordi ou le joueur
    listeLigneChoisie=q[ligneChoisie-1] #listeLigneChoisie est la liste associée à la ligne choisie par le joueur ou l'ordi
    if c[2]=="G": # 'c' est sous la forme i:P ou P = c[2], et est le choix de l'endroit où on tire, ici gauche
        listeLigneChoisie[0]=listeLigneChoisie[0]+1
    else: # on tire logiquement à droite
        listeLigneChoisie[1]=listeLigneChoisie[1]-1
    for i in range(l): # On souhaite supprimer de la liste de quilles les lignes qui n'existent plus, devenue vide
        if q[i][0]>q[i][1]: # On supprime toute incohérence, par exemple supposons l'existence d'une ligne [3,3], en jouant elle peut devenir [3,2] ce qui est incohérent.
            q.remove(q[i]) # on supprime cette incohérence
            break # Cela va nous permettre d'arreter la boucle for si la condition est verifié avant la fin.

#Sous procédure 2 : Si on joue M :
def jouerMilieu(c,q):
    l=len(q)
    ligneChoisie=int(c[0])
    listeligneChoisie=q[ligneChoisie-1]
    nb=listeligneChoisie[1]-listeligneChoisie[0]+1 #nb est ici le nombres de quilles de laligne
    if nb<=2: # Si il reste au plus deux quilles sur la ligne choisie, elle est logiquement supprimée
        q.remove(listeligneChoisie)
    else: # Etant donné que nous allons couper la ligne en deux, nous créons les variables quilleSeparéeLigne1(à gauche) et quilleSeparéeLigne2 (à droite) :
        quilleSeparéeLigne2=listeligneChoisie[1]-(((nb-2)//2)-1) # On exprime la quille de la 2e ligne en fonction du nombre initial de quilles de la ligne et de la dernière quille de cette ligne
        quilleSeparéeLigne1=(quilleSeparéeLigne2)-3 # On supprime 2 quilles, ainsi la différence entre les quilles séparées est de 3
        q.append([listeligneChoisie[0],quilleSeparéeLigne1])
        q.append([quilleSeparéeLigne2,listeligneChoisie[1]]) 
        q.remove(listeligneChoisie)  # On ajoute les deux lignes séparées et on supprime la ligne initiale, ce qui revient à casser la ligne en deux.
        q.sort() #On range du plus petit au plus grand pour éviter une incohérence.
        for i in range(l): # Comme avant, on supprime les lignes incohérentes.
            if q[i][0]>q[i][1]:
                q.remove(q[i])
                break # De même ici, on force la sortie de la boucle for si la condition est vérifiée avant la fin de cette boucle.
        
def jouer(c,q):
    if c[2]=="M":   #c[2] est égale au caractère de position, c-a-d soit M G ou D, ici si c'est M
        jouerMilieu(c,q)  #on lance la procédure de jouerMilieu
    else: #Si non , c-a-d si c'est G ou D
        jouerCote(c,q) #On lance la procédure jouerCôté

#Voici donc le programme jeu:
def jeu():
  tracer(100,0)
  FondCieletTerre()
  herbe(-350,-100,1)
  tomate(-250,-100,1)
  soleil(-600,200)
  nuage(-470,230)
  nuage(550,150)
  four()
  calligraphie()
  messagebox.showinfo("Tajines: LE JEU","BIENVENUE DANS LE GRAND JEU DE TAJINES" '\n\n' "Profitez !!")
  score=0
  seth(0)
  intention=True
  while intention==True:
    tracer(100,0)
    color("black")
    up()
    goto(-50,230)
    fillcolor("#18ECEF")
    begin_fill()
    fd(700)
    seth(90)
    fd(400)
    left(90)
    fd(700)
    left(90)
    fd(400)
    end_fill()
    seth(0)
    fillcolor("#7B241C")
    goto(-400,-3)
    begin_fill()
    fd(800)
    left(90)
    fd(50)
    left(90)
    fd(800)
    left(90)
    fd(50)
    end_fill()
    m=0
    seth(0)
    goto(500,260)
    write("Que la partie commence !", move=False, align="right", font=("Liberation Serif", 35, "normal"))
    NTotal=int(random.randint(7,10)) #On a fait le choix de faire varier les quilles entre 5 à 40, ainsi avoir des parties courtes ou rapides
    q=[[0,NTotal-1]]  #Toutes les quilles sont debouts
    decalage=(844-(NTotal*80.55))/2
    x=-400+decalage
    r=afficheQuilles(q,NTotal)
    for y in r :
         BasTagine(x,2,0.75)
         HautTajine(x,2,0.75)
         x+=80
    gagnant=0 #Initialisation de la variable principale de la boucle de jeur
    tracer(True)
    speed(10)
    while gagnant==0 : #Quand gagnant ==0 personne n'a gagné, quand ==1 c'est le joueur qui gagne, et quand ==2 l'ordi a gagné.
      up()
      fillcolor("#18ECEF")
      goto(-50,230)
      begin_fill()
      fd(700)
      seth(90)
      fd(400)
      left(90)
      fd(700)
      left(90)
      fd(400)
      end_fill()
      goto(500,260)
      write("C'est votre tour!", move=False, align="right", font=("Liberation Serif", 35, "normal"))
      joueur=joueurJoue(q)
      jouer(joueur,q)
      x=-400+decalage
      speed(10)
      if m==0:
          t=r
          m+=1
      else:
          t=z
      p=afficheQuilles(q,NTotal)
      i=0
      while i<NTotal:
         if p[i]!=t[i]: #Si il ya changement par rapport à la situation intiale (r) c'est adire un caractere different dans p
             absi=x-10
             ordo=15
             color("#7B241C")
             fillcolor("#7B241C")
             up()
             goto(absi,ordo)
             seth(0)
             down()
             begin_fill()
             for j in range(2):
                 forward(80)
                 left(90) 
                 forward(40)
                 left(90)
             end_fill()
             color("black")
             HautTajineOuvert(x,2,0.75)
         x+=80
         i+=1
      if len(q)==0  : #Si il ne reste plus de ligne alors:
        gagnant=1 #Le joueur gagne
      else :
        ordi=str(ordijoue(q))
        up()
        fillcolor("#18ECEF")
        goto(-50,230)
        begin_fill()
        fd(700)
        seth(90)
        fd(400)
        left(90)
        fd(700)
        left(90)
        fd(400)
        end_fill()
        goto(500,260)
        write(["L'ordi a joué ... " ,ordi] , move=False, align="right", font=("Liberation Serif", 35, "normal"))
        jouer(ordi,q)
        x=-400+decalage
        speed(10)
        z=afficheQuilles(q,NTotal)
        i=0
        while i<NTotal:
          if z[i]!=p[i]:
             absi=x-10
             ordo=15
             color("#7B241C")
             fillcolor("#7B241C")
             up()
             goto(absi,ordo)
             seth(0)
             down()
             begin_fill()
             for j in range(2):
                 forward(80)
                 left(90) 
                 forward(40)
                 left(90)
             end_fill()
             color("black")
             HautTajineOuvert(x,2,0.75)
          x+=80
          i+=1
        time.sleep(2) #On laisse le temps au joueur pour voir ce que l'odri a joué
        if len(q)==0 : #De la même manière si il n'y a plus de quilles apres le jeu de l'ordi :
            gagnant=2 #Alors il gagne!
      if gagnant==1:
          score+=1
          messagebox.showinfo("Tajines : LE JEU", "Vous avez gagné, Youpi!")
      elif gagnant==2 :
          messagebox.showinfo("Tajines : LE JEU", "Vous avez perdu :'( | GAME OVER")
    up()
    color("#00FF27")
    fillcolor("#00FF27")
    up()
    goto(-400,-250)
    seth(0)
    down()
    begin_fill()
    for j in range(2):
      forward(-90)
      left(90) 
      forward(20)
      left(-90)
      forward(90)
      end_fill()
    up()
    goto(-470,-250)
    color("black")
    write("Score: "+ str(score), move=False, align="center", font=("Old English Text MT", 14, "normal"))
    intention=messagebox.askyesno("Tajines: LE JEU","Voulez vous rejouez?")
    if intention!=True :
      messagebox.showinfo("Tajines: LE JEU","Merci d'avoir joué! A bientôt" '\n\n' "Votre score : "+ str(score))
      bye()
jeu()
