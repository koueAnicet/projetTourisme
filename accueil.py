
from subprocess import call
from sys import path
from tkinter import*
from unittest import main
import webbrowser# pour executer un lien 
import hashlib  # module d'harchage
import re  # module de verification email
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #pour afficher les image
import os
# import fonctions,connexion,inscription

accueil =Tk()
accueil.title(" page d'accueil")
accueil.configure()

#accueil.wm_attributes('-transparentcolor','black')#transparence

#adaptation à l'ecran
# l=accueil.winfo_width()
# h=accueil.winfo_height()

accueil.geometry("1990x1200")

def inscription():
    
    frameInscription= Frame(accueil, width=400, height=1000, highlightbackground="black", highlightthickness=2, highlightcolor='green',bg="gray")
    frameInscription.place(x=780,y=250)
    nomLabel= Label(frameInscription,text="Nom", width=50, bg="gray", font=("Italique", 13, "bold"))
    nomLabel.pack(pady=5,)
    #---------entry name--------
    nomEntry=Entry(frameInscription,width=50, borderwidth=2)
    nomEntry.pack(pady=30,ipady=10)

    #-----Label lastname--------
    prenomLabel= Label(frameInscription,text="Prenom", width=50, bg="gray", font=("Italique", 13, "bold"))
    prenomLabel.pack()
    #---------entry lastname--------
    prenomEntry=Entry(frameInscription,width=50, borderwidth=2)
    prenomEntry.pack(pady=30,ipady=10)

    #-----Label email--------
    emailLabel= Label(frameInscription,text="Prenom", width=50, bg="gray" ,font=("Italique", 13, "bold"))
    emailLabel.pack()
    #---------entry email--------
    emailEntry=Entry(frameInscription,width=50, borderwidth=2)
    emailEntry.pack(pady=30,ipady=10)

    #-----Label password--------
    passwordLabel= Label(frameInscription,text="Password", width=50, bg="gray", font=("Italique", 13, "bold"))
    passwordLabel.pack()
    #---------entry password--------
    passwordEntry=Entry(frameInscription,width=50, borderwidth=2)
    passwordEntry.pack(pady=30,ipady=10) 
    def conditionSave():
        frameInscription.place_forget()
        connexion()

    #-----------button-------------
    saveBtn= Button(frameInscription,text="save", width=20, fg="red",font=("Simple", 13, "bold"), highlightbackground="gray",borderwidth=1, command=conditionSave)
    saveBtn.pack(pady=20,ipady=5)
    


def connexion():
    
    frame= Frame(accueil, width=400, height=800, highlightbackground="black", highlightthickness=2, highlightcolor='green',bg="gray")
    # frame.winfo_geometry
    frame.place(x=780,y=280)



    #-----Label email--------
    emailLabel= Label(frame,text="Email", width=50, bg="gray" ,font=("Italique", 13, "bold"))
    emailLabel.pack(pady=15,)
    #---------entry email--------
    emailEntry=Entry(frame,width=50)
    emailEntry.pack(pady=30,ipady=10)

    #-----Label password--------
    passwordLabel= Label(frame,text="Password", width=50, bg="gray", font=("Italique", 13, "bold"))
    passwordLabel.pack()
    #---------entry password--------
    passwordEntry=Entry(frame,width=50)
    passwordEntry.pack(pady=30,ipady=10) 


    def condtionCnnexion():

        frame.place_forget()
        #-----
        accueil.destroy()
        main()

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
    saveBtn= Button(frame,text="connect", width=20, fg="red",font=("Italique", 13, "bold"),highlightbackground='#00aeff', command=condtionCnnexion)
    
    saveBtn.pack(pady=30,ipady=5)
    

def main():
    fenetre =Tk()
    fenetre.title()
    fenetre.configure()
    
    #fenetre.wm_attributes('-transparentcolor','black')#transparence

    #adaptation à l'ecran
    # l=fenetre.winfo_width()
    # h=fenetre.winfo_height()
    # fenetre.geometry("%dx%d"%(l,h))

    #titre de du projet et sa frame
    frameLab =Frame(fenetre, width=1990, height=1200, bg='#0FE3FF')
    frameLab.pack()
    lab = Label(frameLab ,bg='#0FE3FF', font=("Gras italique", 40, "bold"))#text="""Bienvenue sur les Hotels d'Assinie Mafia"""
    lab.place( x=800,y=10,)

    img = ImageTk.PhotoImage(Image.open("images/img2main.jpeg"))
    img_label=Label(fenetre,image= img, width=1990, height=500).pack(expand="y",)

    #frame de diff hotels
    frameCadreImage=Frame(fenetre,)
    frameCadreImage.pack()

    #Hotel1
    frameCadre=Frame(frameCadreImage, width=350, height=250, bg="")
    frameCadre.grid(row=0, column=0, padx=0, pady=10, sticky=N)

    # imagCadre1 = ImageTk.PhotoImage(Image.open("images/cdre1.jpeg"))
    # img_label=Label(frameCadre,image= imagCadre1, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    btnCadre1=Button(frameCadre, text="Detail", bg="black",)
    btnCadre1.place(x=273, y=225)

    labCadre1=Label(frameCadre, text="Villa Assinie Bord de Lagune", font=('Simple', 25, 'bold') )
    labCadre1.place(x=10, y=25)
    #frameCadre.wm_attributes('-transparent','black')#transparence

    #Hotel2
    frameCadre1=Frame(frameCadre, width=350, height=250, bg="red")
    frameCadre1.grid(row=0, column=1,padx=0, pady=10, sticky=N)

    # imagCadre2 = ImageTk.PhotoImage(Image.open("images/cadr2.jpeg"))
    # img_label2=Label(frameCadre1,image= imagCadre2, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    labCadre2=Label(frameCadre1, text="La Maison Blanche", font=('Simple', 25, ) )
    labCadre2.place(x=70, y=25, )

    btnCadre2=Button(frameCadre1, text="Detail", bg="black",)
    btnCadre2.place(x=290, y=218)

    # #diffHotel3
    frameCadre3=Frame(frameCadre, width=350, height=250, bg="light green")
    frameCadre3.grid(row=1, column=0,)

    # imagCadre3 = ImageTk.PhotoImage(Image.open("images/cadr3.jpeg"))
    # img_label3=Label(frameCadre3,image= imagCadre3, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    labCadre3=Label(frameCadre3, text="Hotel Akwa Beach", font=('Simple', 25, ) )
    labCadre3.place(x=70, y=25, )

    btnCadre4=Button(frameCadre3, text="Detail", bg="black", )
    btnCadre4.place(x=290, y=218)

    # #diffHotel4
    frameCadre4=Frame(frameCadre, width=350, height=250, bg="lightblue")
    frameCadre4.grid(row=1, column=1, padx=10)

    # imagCadre4 = ImageTk.PhotoImage(Image.open("images/cdre4.jpg"))
    # img_label4=Label(frameCadre4,image= imagCadre4, width=350, height=250).grid(row=0, column=0,)#pack(expand=True)

    labCadre4=Label(frameCadre4, text="Assinie Lodge", font=('Simple', 25, ) )
    labCadre4.place(x=70, y=25, )

    btnCadre4=Button(frameCadre4, text="Detail", bg="black",)
    btnCadre4.place(x=290, y=218)



    # #diffHotel3
    # frameCadre4=Frame(frameCadre4, width=350, height=250, bg="blue")
    # frameCadre4.grid(row=0, column=3, padx=10)

    # #diffHotel5
    # frameCadre=Frame(frameCadreImage, width=350, height=250, bg="gray")
    # frameCadre.grid(row=1, column=0, pady=20)
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