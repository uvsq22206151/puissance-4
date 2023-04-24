def Gagner(p:Plateau): #Renvoie la couleur gagnante si une couleur gagne sinon None
    li:int
    col:int
    for li in range(3): #test verticalement
        for col in range(7):
            if(p[li][col] == p[li+1][col] == p[li+2][col] == p[li-3][col] and (p[li][col]==PR or p[li][col]==PJ)): 
                return p[li][col]
            
    for li in range(6): #test horizontalement
        for col in range(4):
             if(p[li][col] == p[li][col+1] == p[li][col+2] == p[li][col+3]and (p[li][col]==PR or p[li][col]==PJ)): 
                return p[li][col]
             
    for li in range(3): #diagonale haut gauche vers bas droite
        for col in range(4): 
            if(p[li][col] == p[li+1][col+1] == p[li+2][col+2] == p[li+3][col+3]and (p[li][col]==PR or p[li][col]==PJ)): 
                return p[li][col]
            
    for li in range(3,6): #diagonale bas gauche vers haut droite
        for col in range(4): 
            if(p[li][col] == p[li-1][col+1] == p[li-2][col+2] == p[li-3][col+3]and (p[li][col]==PR or p[li][col]==PJ)): 
                return p[li][col]
    return None



def quitterManche(canvas, quitter_button):
    reponse = askokcancel("quitter", "Etes vous sÃ»r de vouloir quitter la partie ? ")
    if reponse:
        quitter_button.destroy()
        canvas.destroy() 
        lancerMenu()




        def proposerJouer(canvas,quitter_button,choix_joueur,couleur_joueur): 
        global coup_jouer
        cmd = root.register(lambda s: not s or s.isdigit()) #La valeur saisie doit Ãªtre un entier
        jouer_label = Label(root, text="Le joueur "+choix_joueur+" doit choisir une colonne entre 1 a 7 : ", font=("arial" , 15))
        canvas.create_window(250, 20, window=jouer_label)
        colonne_jouer = Entry(root, font=("arial" , 15), validate="key", vcmd=(cmd, "%P"))
        canvas.create_window(500, 20, window=colonne_jouer, width=30)
        jouer_button= Button(text='Jouer', font=("arial" , 15), bg=couleur_joueur , fg='darkblue', command=lambda: [jouer(canvas,quitter_button,couleur_joueur,choix_joueur,colonne_jouer)])
        canvas.create_window(570, 20, window=jouer_button)

def remplirPlateau(canvas):
    for ligne in range(6):
        for colonne in range(7):                
            if p[ligne][colonne]=='R':
                ajouterJeton(canvas,colonne,ligne,'red')
            elif p[ligne][colonne]=='J':
                ajouterJeton(canvas,colonne,ligne,'yellow')
            else:
                ajouterJeton(canvas,colonne,ligne,'white')

def plateauDeJeu (vide):
    
    global coup_jouer
    global p
    global vicPR
    global vicPJ
    
    choix_joueur:str #Joeur qui doit jouer

    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    a = canvas.create_rectangle(100, 40, 700, 600, fill='blue')

    if vide:
        p = initPlateau()
        # Affichage du plateau vide
        for colonne in range(7):
            for ligne in range(6):
                ajouterJeton(canvas,colonne,ligne,'white')
    else:
        remplirPlateau(canvas)
    
    # Boutons 
    quitter_button= Button(root, text="Quitter la manche", font=("arial" , 15), bg='red' , fg='darkblue', command=lambda: [quitterManche (canvas, quitter_button)])
    quitter_button.pack()
    sauvegarder_button= Button(root, text="Sauvegarder la manche", font=("arial" , 15), bg='red' , fg='darkblue', command=lambda: [sauvegarderPartie(p)])
    sauvegarder_button.pack()

    choix_joueur = nomPR
    couleur_joueur = 'red'
    if((vicPJ+vicPR)%2==0): #Alternance des joueurs au debut
        choix_joueur=nomPR
        couleur_joueur = 'red'
    else:
        choix_joueur=nomPJ
        couleur_joueur = 'yellow'
    coup_jouer=0