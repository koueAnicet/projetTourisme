
from tkinter import*
import webbrowser# pour executer un lien 
import hashlib  # module d'harchage
import re  # module de verification email
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #pour afficher les image
import fonctions,connexion,inscription

accueil =Tk()
accueil.title()
accueil.configure()

#accueil.wm_attributes('-transparentcolor','black')#transparence

#adaptation à l'ecran
# l=accueil.winfo_width()
# h=accueil.winfo_height()

accueil.geometry("1990x1200")


#titre de du projet et sa frame
frameLab =Frame(accueil, width=1990, height=70, bg='#0FE3FF')
frameLab.pack(expand="y")
lab = Label(frameLab  ,bg='#0FE3FF', font=("Gras italique", 40, "bold"))#text="""Bienvenue sur les Hotels d'Assinie Mafia"""
lab.place( x=600,y=10,)

img = ImageTk.PhotoImage(Image.open("images/125365_v3.jpeg"))
img_label=Label(accueil,image= img, width=1990, height=1200).pack(expand="y",)

#frame connexion & inscription
btnInscription=Button(accueil, text="Inscription", command=inscription.inscription)
btnInscription.place(x=1500, y=10)

btnConnexion=Button(accueil, text="Connexion", command=connexion.connexion)
btnConnexion.place(x=1600, y=10) 

frame= Frame(inscription, width=400, height=999, highlightbackground="black", highlightthickness=2, highlightcolor='green',bg="gray")
frame.pack(pady=150)

#-----Label name--------
nomLabel= Label(frame,text="Nom", width=50, bg="gray", font=("Italique", 13, "bold"))
nomLabel.pack(pady=5,)
#---------entry name--------
nomEntry=Entry(frame,width=50, borderwidth=2)
nomEntry.pack(pady=30,ipady=10)

#-----Label lastname--------
prenomLabel= Label(frame,text="Prenom", width=50, bg="gray", font=("Italique", 13, "bold"))
prenomLabel.pack()
#---------entry lastname--------
prenomEntry=Entry(frame,width=50, borderwidth=2)
prenomEntry.pack(pady=30,ipady=10)

#-----Label email--------
emailLabel= Label(frame,text="Prenom", width=50, bg="gray" ,font=("Italique", 13, "bold"))
emailLabel.pack()
#---------entry email--------
emailEntry=Entry(frame,width=50, borderwidth=2)
emailEntry.pack(pady=30,ipady=10)

#-----Label password--------
passwordLabel= Label(frame,text="Password", width=50, bg="gray", font=("Italique", 13, "bold"))
passwordLabel.pack()
#---------entry password--------
passwordEntry=Entry(frame,width=50, borderwidth=2)
passwordEntry.pack(pady=30,ipady=10) 

#-----------button-------------
saveBtn= Button(frame,text="save", width=20, fg="red",font=("Simple", 13, "bold"), highlightbackground="gray",borderwidth=1)
saveBtn.pack(pady=20,)


accueil.mainloop()