import webbrowser# pour executer un lien 
import hashlib  # module d'harchage
import re  # module de verification email
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #pour afficher les image

fenetre =Tk()
fenetre.title()
fenetre.configure()

frameLab =Frame(fenetre, width=1990, height=70, bg='#0FE3FF')
frameLab.pack()
lab = Label(frameLab ,bg='#0FE3FF', font=("Gras italique", 40, "bold"))#text="""Bienvenue sur les Hotels d'Assinie Mafia"""
lab.place( x=800,y=10,)
img = ImageTk.PhotoImage(Image.open("125365_v3.jpeg"))
img_label=Label(fenetre,image= img, width=1990, height=500).pack(expand=True)
#diffHotel
frameCadreImage=Frame(fenetre,)
frameCadreImage.pack()
#diffHotel1
frameCadre=Frame(frameCadreImage, width=350, height=250, bg="red")
frameCadre.grid(row=0, column=0, pady=10)
#diffHotel2
frameCadre1=Frame(frameCadreImage, width=350, height=250, bg="yellow")
frameCadre1.grid(row=0, column=1, padx=10)
#diffHotel2
frameCadre2=Frame(frameCadreImage, width=350, height=250, bg="light green")
frameCadre2.grid(row=0, column=2, padx=10)
#diffHotel3
frameCadre3=Frame(frameCadreImage, width=350, height=250, bg="lightblue")
frameCadre3.grid(row=0, column=3, padx=10)
#diffHotel3
frameCadre4=Frame(frameCadreImage, width=350, height=250, bg="blue")
frameCadre4.grid(row=0, column=5, padx=10)

#diffHotel1
frameCadre=Frame(frameCadreImage, width=350, height=250, bg="gray")
frameCadre.grid(row=1, column=0, pady=20)
#diffHotel2
frameCadre11=Frame(frameCadreImage, width=350, height=250, bg="green")
frameCadre11.grid(row=1, column=1, padx=10)
#diffHotel2
frameCadre12=Frame(frameCadreImage, width=350, height=250, bg="brown")
frameCadre12.grid(row=1, column=2, padx=10)
#diffHotel3
frameCadre13=Frame(frameCadreImage, width=350, height=250, bg="pink")
frameCadre13.grid(row=1, column=3, padx=10)
#diffHotel3
frameCadre14=Frame(frameCadreImage, width=350, height=250, bg="orange")
frameCadre14.grid(row=1, column=5, padx=10)

frame = Frame(fenetre)
canvas = Canvas(frame)
Label(canvas, text = "Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font = "-size 100").pack()
scrollbar = Scrollbar(frame)
scrollbar.pack(side = RIGHT, fill = Y)
canvas.configure(yscrollcommand = scrollbar.set)
canvas.pack()
frame.pack()

# installer un env virtule: python3 -m venv env et pour l'activer :source env/bin/activate, pour quiter: deactivate
#webbrowser.open('https://openclassrooms.com/forum/sujet/mettre-un-lien-vers-un-navigateur')
fenetre.mainloop()