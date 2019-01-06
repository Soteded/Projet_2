from tkinter import *
from random import *
from time import *
x1,y1,dx,dy = 530,350,2,0

a,b=0,0

hauteur = 720
largeur = 1080
y1_j1,y2_j1,y1_j2,y2_j2 = 300,420,300,420

score_j1,score_j2=0,0

coul_j1,coul_ball,coul_fond,coul_j2=0,0,1,0
couleurs={0:'white',1:'black',2:'blue',3:'red',4:'green',5:'yellow'}

x_bul=0
y_bul=0

temps_debut = 0
temps_fin = 0

bounus = None
couleur_bonus_list = ["green","yellow","red"]
last_hit = 0

def parametre1():
    def precedent1():
        parametrage1.destroy()
        menu_principal()
    
    def suivant1():
        parametrage1.destroy()
        parametre2()
    
    def tests():
        global a,b
        a = ligne_text.get()
        b = vit_bal.get()

    parametrage1 = Tk()
    parametrage1.focus_force()
    titre = Label(parametrage1,text="Paramètrage de la partie :")
    titre.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

    nbr_pts_gag = Label(parametrage1,text="Nombre de points pour gagner :")
    nbr_pts_gag.grid(row=2,column=1,padx=5,pady=5)
    text_pw = IntVar()
    ligne_text = Entry(parametrage1, textvariable=text_pw,width=5)
    ligne_text.grid(row=2,column=2,padx=10)

    vit_ball = Label(parametrage1,text="Vitesse de la balle :")
    vit_ball.grid(row=3,column=1,padx=5,pady=5)
    vitesse = IntVar()
    vit_bal = Entry(parametrage1, textvariable=vitesse,width=5)
    vit_bal.grid(row=3,column=2,padx=10)

    btn_test = Button(parametrage1,text="Appliquer",command=tests)
    btn_test.grid(row=2,column=3,rowspan=2)

    precedent1_1 = Button(parametrage1,text="Précédent",command=precedent1)
    precedent1_1.grid(row=4,column=0,padx=10,pady=10)
    suivant1 = Button(parametrage1,text="Suivant",command=suivant1)
    suivant1.grid(row=4,column=4,padx=10,pady=10)

    parametrage1.mainloop()

def parametre2():
    def precedent2():
        parametrage2.destroy()
        parametre1()
    
    def suivant3():
        global temps_debut
        temps_debut = time()
        parametrage2.destroy()
        le_jeu()

    def coul_suiv_j1():
        global coul_j1
        coul_j1 += 1
        couleurs[coul_j1%5]
        canvas.create_rectangle((5,75),(15,175),fill=couleurs[coul_j1%5])
    def coul_prec_j1():
        global coul_j1
        coul_j1 -= 1
        couleurs[coul_j1%5]
        canvas.create_rectangle((5,75),(15,175),fill=couleurs[coul_j1%5])

    def coul_suiv_ball():
        global coul_ball
        coul_ball += 1
        couleurs[coul_ball%5]
        canvas.create_oval((160,115),(180,135),fill=couleurs[coul_ball%5])
    def coul_prec_ball():
        global coul_ball
        coul_ball -= 1
        couleurs[coul_ball%5]
        canvas.create_oval((160,115),(180,135),fill=couleurs[coul_ball%5])

    def coul_suiv_fond():
        global coul_fond
        coul_fond += 1
        couleurs[coul_fond%5]
        canvas.config(bg=couleurs[coul_fond%5])
    def coul_prec_fond():
        global coul_fond
        coul_fond -= 1
        couleurs[coul_fond%5]
        canvas.config(bg=couleurs[coul_fond%5])

    def coul_suiv_j2():
        global coul_j2
        coul_j2 += 1
        couleurs[coul_j2%5]
        canvas.create_rectangle((485,75),(495,175),fill=couleurs[coul_j2%5])
    def coul_prec_j2():
        global coul_j2
        coul_j2 -= 1
        couleurs[coul_j2%5]
        canvas.create_rectangle((485,75),(495,175),fill=couleurs[coul_j2%5])

    parametrage2 = Tk()
    parametrage2.focus_force()
    canvas=Canvas(width=500,height=300,bg="black")
    canvas.grid(row=1,column=1,columnspan=4)
    canvas.create_oval((160,115),(180,135),fill='white')
    canvas.create_rectangle((5,75),(15,175),fill='white')
    canvas.create_rectangle((485,75),(495,175),fill='white')
    
    text_couleur_j1 = Label(parametrage2,text="Couleur J1")
    text_couleur_j1.grid(row=2,column=1)
    cprec1 = Button(parametrage2,text="Couleur précédente",command=coul_prec_j1)
    cprec1.grid(row=3,column=1)
    csuiv1 = Button(parametrage2,text="Couleur suivante",command=coul_suiv_j1)
    csuiv1.grid(row=4,column=1)

    text_couleur_ball = Label(parametrage2,text="Couleur Balle")
    text_couleur_ball.grid(row=2,column=2)
    cprec2 = Button(parametrage2,text="Couleur précédente",command=coul_prec_ball)
    cprec2.grid(row=3,column=2)
    csuiv2 = Button(parametrage2,text="Couleur suivante",command=coul_suiv_ball)
    csuiv2.grid(row=4,column=2)

    text_couleur_fond = Label(parametrage2,text="Couleur fond")
    text_couleur_fond.grid(row=2,column=3)
    cprec3 = Button(parametrage2,text="Couleur précédente",command=coul_prec_fond)
    cprec3.grid(row=3,column=3)
    csuiv3 = Button(parametrage2,text="Couleur suivante",command=coul_suiv_fond)
    csuiv3.grid(row=4,column=3)

    text_couleur_j2 = Label(parametrage2,text="Couleur J2")
    text_couleur_j2.grid(row=2,column=4)
    cprec4 = Button(parametrage2,text="Couleur précédente",command=coul_prec_j2)
    cprec4.grid(row=3,column=4)
    csuiv4 = Button(parametrage2,text="Couleur suivante",command=coul_suiv_j2)
    csuiv4.grid(row=4,column=4)

    precedent1_2 = Button(parametrage2,text="Précédent",command=precedent2)
    precedent1_2.grid(row=5,column=1,padx=10,pady=10)
    suivant2 = Button(parametrage2,text="Jouer !",command=suivant3)
    suivant2.grid(row=5,column=4,padx=10,pady=10)
    parametrage2.mainloop()

def le_jeu():
    def gametick():
        global x1,y1,dx,dy
        global hauteur,largeur
        global score_j1,score_j2
        global a,b
        
        def scores(score_j1,score_j2):
            score = Label(fenetre_jeu,text=str(score_j1) + "-" + str(score_j2))
            score.grid(row=2,column=2)

        def victoire_j1():
            global score_j1,score_j2
            global temps_debut,temps_fin
            temps_jeu = int(temps_fin-temps_debut)
            minutes = int(temps_jeu/60)
            secondes = int(temps_jeu%60)
            victoire = Tk()
            victoire.title("Joueur 1")
            lab=Label(victoire, text="Le joueur 1 à gagné "+str(score_j1)+str(" ")+"à "+str(score_j2)+str(" ")+"en "+str(minutes)+"min"+str(secondes)+"sec")
            lab.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
            dy = 0
            score_j1,score_j2=0,0
            end_menu_rejouer = Button(victoire,text="Rejouer",command=lambda:jouer2())
            end_menu_rejouer.grid(row=2,column=2,padx=10,pady=10)
            def jouer2():
                victoire.destroy()
                le_jeu()
            end_menu_menu = Button(victoire,text="Menu",command=lambda:retour_menu())
            end_menu_menu.grid(row=2,column=1,padx=10,pady=10)
            def retour_menu():
                victoire.destroy()
                menu_principal()
            victoire.mainloop()

        def victoire_j2():
            global score_j1,score_j2
            global temps_debut,temps_fin
            temps_jeu = int(temps_fin-temps_debut)
            minutes = int(temps_jeu/60)
            secondes = int(temps_jeu%60)
            victoire = Tk()
            victoire.title("Joueur 2")
            lab=Label(victoire, text="Le joueur 2 à gagné "+str(score_j2)+str(" ")+" à "+str(score_j1)+str(" ")+"en "+str(minutes)+"min"+str(secondes)+"sec")
            lab.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
            dy = 0
            score_j1,score_j2=0,0
            end_menu_rejouer = Button(victoire,text="Rejouer",command=lambda:jouer2())
            end_menu_rejouer.grid(row=2,column=2,padx=10,pady=10)
            def jouer2():
                victoire.destroy()
                le_jeu()
            end_menu_menu = Button(victoire,text="Menu",command=lambda:retour_menu())
            end_menu_menu.grid(row=2,column=1,padx=10,pady=10)
            def retour_menu():
                victoire.destroy()
                menu_principal()
            victoire.mainloop()

        def bonus():
            global bounus,couleur_bonus,j1,j2,b
            if bounus == None:
                x_bul = randrange(50,largeur-90)
                y_bul = randrange(5,hauteur-5)
                couleur_bonus = couleur_bonus_list[randrange(0,3,1)]
                bul_bonus = canvas.create_oval(x_bul,y_bul,x_bul+40,y_bul+40,fill=couleur_bonus)
            if (canvas.coords(ball)[1]<=canvas.coords(bul_bonus)[3]) and (canvas.coords(ball)[3]>=canvas.coords(bul_bonus)[1]) and (canvas.coords(ball)[2]>=canvas.coords(bul_bonus)[0]) and (canvas.coords(ball)[0]<=canvas.coords(bul_bonus)[2]):
                if couleur_bonus == "green":
                    if last_hit == True:
                        canvas.delete(j1)
                        j1 = canvas.create_rectangle((15,y1_j1-20),(30,y2_j1+20),fill=couleurs[coul_j1%5])
                    if last_hit == False:
                        canvas.delete(j2)
                        j2 = canvas.create_rectangle((1050,y1_j2+20),(1065,y2_j2-20),fill=couleurs[coul_j2%5])
                if couleur_bonus == "yellow":
                    b += b
                if couleur_bonus == 'red':
                    if last_hit == True:
                        canvas.delete(j2)
                        j2 = canvas.create_rectangle(450,y1_j2+20,425,y2_j2-20,fill=couleurs[coul_j2%5])
                    if last_hit == False:
                        canvas.delete(j1)
                        j1 = canvas.create_rectangle(50,y1_j1+20,75,y2_j1-20,fill=couleurs[coul_j1%5])
                canvas.delete(bul_bonus)
                bounus = None
            canvas.after(1000,bonus)

        scores(score_j1,score_j2)
        
        if ((canvas.coords(ball)[1]<=canvas.coords(j1)[3]) and (canvas.coords(ball)[1]>=canvas.coords(j1)[1]) and (canvas.coords(ball)[0]<=canvas.coords(j1)[2]) and (canvas.coords(ball)[0]>=canvas.coords(j1)[0])):
            b = -int(b)
            dy += randrange(-100,100)/100
            last_hit = True
        if ((canvas.coords(ball)[2]>=canvas.coords(j2)[0]) and (canvas.coords(ball)[2]<=canvas.coords(j2)[2]) and (canvas.coords(ball)[3]>=canvas.coords(j2)[1]) and (canvas.coords(ball)[1]<=canvas.coords(j2)[3])):
            b = -int(b)
            dy += randrange(-100,100)/100
            last_hit = False
        if (canvas.coords(ball)[3]>=hauteur) or (canvas.coords(ball)[1]<=0):
            dy = -dy
        
        if (canvas.coords(ball)[0] <= 0):
            dy = 0
            score_j2 += 1
            scores(score_j1,score_j2)
            fenetre_jeu.destroy()
            le_jeu()

        elif (canvas.coords(ball)[2] >= largeur):
            dy = 0
            score_j1 += 1
            scores(score_j1,score_j2)
            fenetre_jeu.destroy()
            le_jeu()

        global temps_fin
        if score_j1==int(a):
            temps_fin = time()
            fenetre_jeu.destroy()
            victoire_j1()
        elif score_j2==int(a):
            temps_fin = time()
            fenetre_jeu.destroy()
            victoire_j2()

        canvas.move(ball,b,dy)
        fenetre_jeu.after(10,gametick)

    def j1Up(event):
        touche = event.keysym
        if (touche == "z"):
            canvas.move(j1,0,-10)
        elif (touche == "s"):
            canvas.move(j1,0,10)

    def j2Up(event):
        touche2 = event.keysym
        if (touche2 == "Up"):
            canvas.move(j2,0,-10)
        elif (touche2 == "Down"):
            canvas.move(j2,0,10)

    fenetre_jeu = Tk()
    fenetre_jeu.title("J'aime le topinambour")
    fenetre_jeu.focus_force()

    fenetre_jeu.bind("z", j1Up)
    fenetre_jeu.bind("s", j1Up)
    fenetre_jeu.bind("<Up>", j2Up)
    fenetre_jeu.bind("<Down>", j2Up)

    global hauteur,largeur
    global y1_j1,y2_j1,y1_j2,y2_j2

    canvas = Canvas(width=largeur,height=hauteur,bg=couleurs[coul_fond%5])
    canvas.grid(row=1,column=1,columnspan=3)
    ball = canvas.create_oval((x1,y1),(x1+20,y1+20),fill=couleurs[coul_ball%5])
    j1 = canvas.create_rectangle((15,y1_j1),(30,y2_j1),fill=couleurs[coul_j1%5])
    j2 = canvas.create_rectangle((1050,y1_j2),(1065,y2_j2),fill=couleurs[coul_j2%5])

    gametick()
    fenetre_jeu.mainloop()

def menu_principal():
    menu = Tk()
    menu.title("pong.exe")
    menu.focus_force()
    titre = Label(menu,text="Jeu pong",width=10)
    titre.grid(row=1,column=2,padx=10,pady=10)
    but_quitter = Button(menu,text="Quitter",command=menu.quit)
    but_quitter.grid(row=2,column=3,padx=10,pady=10)
    but_play = Button(menu,text="Jouer",command=lambda:jouer())
    but_play.grid(row=2,column=1,padx=10,pady=10)
    def jouer():
        menu.destroy()
        parametre1()
    menu.mainloop()

menu_principal()