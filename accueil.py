from sys import path
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image #pour afficher les image
import webbrowser# pour executer un lien 
import hashlib  # module d'harchage
import re  # module de verification email
import sqlite3
import fonctions


import os
# import fonctions,connexion,inscription

accueil =Tk()
accueil.title(" page d'accueil")
accueil.configure()

#accueil.wm_attributes('-transparentcolor','black')#transparence

l=accueil.winfo_width()
h=accueil.winfo_height()
accueil.geometry("%dx%d"%(l,h))

#accueil.geometry("1990x1200")


#les caracteres de verifcation de mot de passe
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def inscription():
    
    
    frameInscription= Frame(accueil, width=400, height=1000, highlightbackground="black", highlightthickness=2, highlightcolor='green',bg="lightgray")
    frameInscription.place(x=750,y=170)

    nomLabel= Label(frameInscription,text="Nom", width=40, bg="lightgray", font=("Italique", 15, "bold"))
    nomLabel.pack(pady=5,)
    #---------entry name--------
    nomEntry=Entry(frameInscription,width=50, borderwidth=10)
    nomEntry.pack(pady=30,ipady=10)

    #-----Label lastname--------
    prenomLabel= Label(frameInscription,text="Prenom", width=40, bg="lightlightgray", font=("Italique", 15, "bold"))
    prenomLabel.pack()
    #---------entry lastname--------
    prenomEntry=Entry(frameInscription,width=50, borderwidth=10)
    prenomEntry.pack(pady=30,ipady=10)

    #-----Label email--------
    emailLabel= Label(frameInscription,text="Email", width=40, bg="lightlightgray" ,font=("Italique", 15, "bold"))
    emailLabel.pack()
    #---------entry email--------
    emailEntry=Entry(frameInscription,width=50, borderwidth=10)
    emailEntry.pack(pady=30,ipady=10)

    #-----Label password--------
    passwordLabel= Label(frameInscription,text="Password", width=40, bg="lightgray", font=("Italique", 15, "bold"))
    passwordLabel.pack()
    #---------entry password--------
    passwordEntry=Entry(frameInscription,width=50, borderwidth=10, show="*")
    passwordEntry.pack(pady=30,ipady=10) 
    #-----Label password--------
    passwordLabel= Label(frameInscription,text="confirmer password", width=40, bg="lightlightgray", font=("Italique", 15, "bold"), )
    passwordLabel.pack()
    #---------entry password--------
    confirm_passwordEntry=Entry(frameInscription,width=50, borderwidth=10, show="*")
    confirm_passwordEntry.pack(pady=30,ipady=10) 
    
    def conditionInscription():
            #encodage
        hash_mdp = confirm_passwordEntry.get().encode()

        # instancier l'objet sha3_256 
        d = hashlib.sha3_256(hash_mdp)

        #impression(hachage) 
        hachage = d.hexdigest() 

       
        
        #dictionnaire de recuperation
        d={
            "nom": nomEntry.get().capitalize(),
            "prenom": prenomEntry.get().capitalize(),
            "email": emailEntry.get(),
            "mdp": hachage
        }
        if nomEntry.get()=="" or prenomEntry.get()=="" or emailEntry.get()=="" or passwordEntry.get()=="" or confirm_passwordEntry.get()=="":
            messagebox.showerror("error","Remplissez tous les champs!")
        elif emailEntry.get().isspace() or passwordEntry.get().isspace() or confirm_passwordEntry.get().isspace():   
                    messagebox.showerror('error',"pas d'espacement!")
        
        elif passwordEntry.get() == confirm_passwordEntry.get():
            #----------verificationde email------------
            if (re.search(regex,emailEntry.get())):
                conn = sqlite3.connect("database.db")
                
                c = conn.cursor()
                
                #--------------creation de la table dans la base de donnees---------
                c.execute("""CREATE TABLE IF NOT EXISTS user(
                    nom text,
                    prenom text,
                    email text,
                    mdp integer
                )""")


                #--------enregistrement des element dans la base de donnees---------- 
                c.execute("INSERT INTO user VALUES(:nom, :prenom, :email, :mdp)", d)
                
                #---------ajout dans la base de donnees-----
                conn.commit()
                conn.close()
                messagebox.showinfo("validEmail","Inscription reusie!")
                frameInscription.place_forget()
                connexion()
            else:
                messagebox.showerror('error',"Email Invalide!")
                
        else:
            messagebox.showerror('error',"mot de pass n'est pas identique!")
        
   
        
    #-----------button-------------
    saveBtn= Button(frameInscription,text="S'insris", width=20, fg="red",font=("Simple", 15, "bold"), highlightbackground="lightgray",borderwidth=1, command=conditionInscription)
    saveBtn.pack(pady=20,ipady=5)
    


def connexion():
    
    frameConnexion= Frame(accueil, width=400, height=800, highlightbackground="black", highlightthickness=2, highlightcolor='green',bg="lightgray")
    # frameConnexion.winfo_geometry
    frameConnexion.place(x=770,y=170)



    #-----Label email--------
    emailLabel= Label(frameConnexion,text="Email",  width=40, bg="lightgray" ,font=("Italique", 15, "bold"))
    emailLabel.pack(pady=15,)
    #---------entry email--------
    emailEntry=Entry(frameConnexion,width=50, borderwidth=10)
    emailEntry.pack(pady=30,ipady=10)

    #-----Label password--------
    passwordLabel= Label(frameConnexion,text="Password", width=40, bg="lightgray", font=("Italique", 15, "bold"))
    passwordLabel.pack()
    #---------entry password--------
    passwordEntry=Entry(frameConnexion,width=50,  borderwidth=10, show='*')
    passwordEntry.pack(pady=30,ipady=10) 


    def conditionConnexion():

        
        if emailEntry.get()=="" or passwordEntry.get()=="":
            messagebox.showerror("error","veuillez remplier les champs")

        elif emailEntry.get() and passwordEntry.get():
        
    
            #encodage
            hash_pwd_connexion = passwordEntry.get().encode()
            # instancier l'objet sha3_256 
            donnesConnexion= hashlib.sha3_256(hash_pwd_connexion)

            #impression(hachage) 
            hachees = donnesConnexion.hexdigest()
            d={"email": emailEntry.get(), "mdp": hachees}
            #--------------connexion a base de donne--------------------
            conn = sqlite3.connect('database.db')
            #designer le cursor "c"
            c =conn.cursor()

            c.execute("SELECT  email,mdp FROM user WHERE email=:email AND mdp=:mdp ",d)

            donneeParcourie=c.fetchall()
            
            for i in donneeParcourie:
                if emailEntry.get() in i  and hachees in i:
                    messagebox.showinfo('info',"vous etes connecté!")
                    accueil.destroy()
                    main()
                    break
                    
            #------------------------fermerture de la connexion------------------------------
            conn.commit()   
            conn.close()
            #-----
           

        # frameLab =Frame(accueil, width=1990, height=70, bg='#0FE3FF')
        # frameLab.pack()
        # lab = Label(frameLab ,bg='#0FE3FF', font=("Gras italique", 40, "bold"))#text="""Bienvenue sur les Hotels d'Assinie Mafia"""
        # lab.place( x=800,y=10,)

        # img = ImageTk.PhotoImage(Image.open("images/125365_v3.jpeg"))
        # img_label=Label(accueil,image= img, width=1990, height=500).pack(expand="y",)
        # #frame de diff hotels
        # frameCadreImage=Frame(accueil,)
        # frameCadreImage.pack()

        # #Hotel1
        # frameCadre=Frame(frameCadreImage, width=350, height=250, bg="")
        # frameCadre.grid(row=0, column=0, padx=0, pady=10, sticky=N)

        # imagCadre1 = ImageTk.PhotoImage(Image.open("images/cdre1.jpeg"))
        # img_label=Label(frameCadre,image= imagCadre1, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

        # btnCadre1=Button(frameCadre, text="Detail", bg="black",)
        # btnCadre1.place(x=273, y=225)

        # labCadre1=Label(frameCadre, text="Villa Assinie Bord de Lagune", font=('Simple', 25, 'bold') )
        # labCadre1.place(x=10, y=25)
        # #frameCadre.wm_attributes('-transparent','black')#transparence

        # #Hotel2
        # frameCadre1=Frame(frameCadre, width=350, height=250, bg="red")
        # frameCadre1.grid(row=0, column=1,padx=0, pady=10, sticky=N)

        # imagCadre2 = ImageTk.PhotoImage(Image.open("images/cadr2.jpeg"))
        # img_label2=Label(frameCadre1,image= imagCadre2, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

        # labCadre2=Label(frameCadre1, text="La Maison Blanche", font=('Simple', 25, ) )
        # labCadre2.place(x=70, y=25, )

        # btnCadre2=Button(frameCadre1, text="Detail", bg="black", )
        # btnCadre2.place(x=290, y=218)

        # # #diffHotel3
        # frameCadre3=Frame(frameCadre, width=350, height=250, bg="light green")
        # frameCadre3.grid(row=1, column=0,)

        # imagCadre3 = ImageTk.PhotoImage(Image.open("images/cadr3.jpeg"))
        # img_label3=Label(frameCadre3,image= imagCadre3, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

        # labCadre3=Label(frameCadre3, text="Hotel Akwa Beach", font=('Simple', 25, ) )
        # labCadre3.place(x=70, y=25, )

        # btnCadre4=Button(frameCadre3, text="Detail", bg="black",)
        # btnCadre4.place(x=290, y=218)

        # # #diffHotel4
        # frameCadre4=Frame(frameCadre, width=350, height=250, bg="lightblue")
        # frameCadre4.grid(row=1, column=1, padx=10)

        # imagCadre4 = ImageTk.PhotoImage(Image.open("images/cdre4.jpg"))
        # img_label4=Label(frameCadre4,image= imagCadre4, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

        # labCadre4=Label(frameCadre4, text="Assinie Lodge", font=('Simple', 25, ) )
        # labCadre4.place(x=70, y=25, )

        # btnCadre4=Button(frameCadre4, text="Detail", bg="black", )
        # btnCadre4.place(x=290, y=218)


    #-----------button-------------
    saveBtn= Button(frameConnexion,text="Se connecté", width=20, fg="red",font=("Italique", 15, "bold"),highlightbackground='#00aeff', command=conditionConnexion)
    
    saveBtn.pack(pady=30,ipady=5)
    

def main():
    fenetre =Tk()
    fenetre.title("presentation")
    fenetre.configure()

    #fenetre.wm_attributes('-transparentcolor','black')#transparence

    #adaptation à l'ecran
    # l=fenetre.winfo_width()
    # h=fenetre.winfo_height()
    # fenetre.geometry("%dx%d"%(l,h))
    #----------------function deconnection
    def retourAccueil():
        fenetre.destroy()
        import accueil
    
    scro_x=Scrollbar(fenetre, orient=VERTICAL)
    
    
    #titre de du projet et sa frame
    frameLab =Frame(fenetre, width=1990, height=70, bg='#0FE3FF')
    frameLab.pack()

    lab = Label(frameLab ,bg='#0FE3FF', font=("Gras italique", 40, "bold"))#text="""Bienvenue sur les Hotels d'Assinie Mafia"""
    lab.place( x=800,y=10,)
    #---------button deconnection-------
    Button(fenetre,text="Déconnection", width=7,fg="red",font=("Simple",15,"bold"), command=retourAccueil).place(x=1790, y=10)

   # img = ImageTk.PhotoImage(Image.open("images/ci.jpeg"))
    #img_label=Label(fenetre,image= img, width=1990, height=500).pack(expand="y",)
    #frame de diff hotels
    frameCadreImage=Frame(fenetre,)
    frameCadreImage.pack()

    #Hotel1
    frameCadre=Frame(frameCadreImage, width=350, height=250, bg="")
    frameCadre.grid(row=0, column=0, padx=0, pady=10, sticky=N)

    imagCadre1 = ImageTk.PhotoImage(Image.open("images/cdre1.jpeg"))
    img_label=Label(frameCadre,image= imagCadre1, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    btnCadre1=Button(frameCadre, text="Detail", bg="black", command=fonctions.beach1 )
    btnCadre1.place(x=273, y=225)

    labCadre1=Label(frameCadre, text="Villa Assinie Bord de Lagune", font=('Simple', 17, 'bold') )
    labCadre1.place(x=10, y=25)
    #frameCadre.wm_attributes('-transparent','black')#transparence

    #Hotel2
    frameCadre1=Frame(frameCadre, width=350, height=250, bg="red")
    frameCadre1.grid(row=0, column=1,padx=0, pady=10, sticky=N)

    imagCadre2 = ImageTk.PhotoImage(Image.open("images/cadr2.jpeg"))
    img_label2=Label(frameCadre1,image= imagCadre2, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    labCadre2=Label(frameCadre1, text="La Maison Blanche", font=('Simple', 25, ) )
    labCadre2.place(x=70, y=25, )

    btnCadre2=Button(frameCadre1, text="Detail", bg="black",)
    btnCadre2.place(x=290, y=218)

    # #diffHotel3
    frameCadre3=Frame(frameCadre, width=350, height=250, bg="light green")
    frameCadre3.grid(row=1, column=0,)

    imagCadre3 = ImageTk.PhotoImage(Image.open("images/cadr3.jpeg"))
    img_label3=Label(frameCadre3,image= imagCadre3, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    labCadre3=Label(frameCadre3, text="Hotel Akwa Beach", font=('Simple', 25, ) )
    labCadre3.place(x=70, y=25, )

    btnCadre4=Button(frameCadre3, text="Detail", bg="black",)
    btnCadre4.place(x=290, y=218)

    # #diffHotel4
    frameCadre4=Frame(frameCadre, width=350, height=250, bg="lightblue")
    frameCadre4.grid(row=1, column=1, padx=10)

    imagCadre4 = ImageTk.PhotoImage(Image.open("images/cdre4.jpg"))
    img_label4=Label(frameCadre4,image= imagCadre4, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    labCadre4=Label(frameCadre4, text="Assinie Lodge", font=('Simple', 25, ) )
    labCadre4.place(x=70, y=25, )

    btnCadre4=Button(frameCadre4, text="Detail", bg="black", )
    btnCadre4.place(x=290, y=218)



    # #diffHotel3
    # frameCadre4=Frame(frameCadre4, width=350, height=250, bg="blue")
    # frameCadre4.grid(row=0, column=3, padx=10)

    # #diffHotel5
    # frameCadre=Frame(frameCadreImage, width=350, height=250, bg="lightgray")
    # # frameCadre.grid(row=1, column=0, pady=20)
    # #diffHotel5
    # frameCadre11=Frame(frameCadreImage, width=350, height=250, bg="green")
    # frameCadre11.grid(row=1, column=1, padx=10)
    # #diffHotel6
    # frameCadre12=Frame(frameCadreImage, width=350, height=250, bg="brown")
    # frameCadre12.grid(row=1, column=2, padx=10)
    # #diffHotel7
    # frameCadre13=Frame(frameCadreImage, width=350, height=250, bg="pink")
    # frameCadre13.grid(row=1, column=3, padx=10)
    # #diffHotel8
    # frameCadre14=Frame(frameCadreImage, width=350, height=250, bg="orange")
    # frameCadre14.grid(row=1, column=5, padx=10)

    # frame = Frame(fenetre)
    # canvas = Canvas(frame)
    # Label(canvas, text = "Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font = "-size 100").pack()
    # scrollbar = Scrollbar(frame)
    # scrollbar.pack(side = RIGHT, fill = Y)
    # canvas.configure(yscrollcommand = scrollbar.set)
    # canvas.pack()
    # frame.pack()

    # installer un env virtule: python3 -m venv env et pour l'activer :source env/bin/activate, pour quiter: deactivate
    #webbrowser.open('https://openclassrooms.com/forum/sujet/mettre-un-lien-vers-un-navigateur')
    fenetre.mainloop()

#titre de du projet et sa frame
frameLab =Frame(accueil, width=1990, height=70, bg='#0FE3FF')
frameLab.pack(expand="y")
lab = Label(frameLab  ,bg='#0FE3FF', font=("Gras italique", 40, "bold"))#text="""Bienvenue sur les Hotels d'Assinie Mafia"""
lab.place( x=600,y=10,)

img = ImageTk.PhotoImage(Image.open("images/img2main.jpeg"))
img_label=Label(accueil,image= img, width=1990, height=1200).pack(expand="y",pady=10)
#--------------frame de connexion et frameInscription-----------

#-------frame btnConnexion & btnInscription
btnInscription=Button(accueil, text="Inscription", command=inscription)
btnInscription.place(x=850, y=80)

btnConnexion=Button(accueil, text="Connexion", command=connexion)
btnConnexion.place(x=950, y=80) 






#-----Label name--------



accueil.mainloop()