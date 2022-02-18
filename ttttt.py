
from tkinter import *
from random import *
 
def NouveauLance():
    nb = randint(1,6)
    Texte.set('Résultat -> ' + str(nb))   
     
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Dé à 6 faces')
 
# Création d'un widget Button (bouton Lancer)
BoutonLancer = Button(Mafenetre, text ='Lancer', command = NouveauLance)
BoutonLancer.pack(side = LEFT, padx = 5, pady = 5)
 
Texte = StringVar()
NouveauLance()
 
 
# Création d'un widget Label (texte 'Résultat -> x')
LabelResultat = Label(Mafenetre, textvariable=Texte , fg ='red', bg ='white')
LabelResultat.pack(side = LEFT, padx = 5, pady = 5)
Mafenetre.mainloop()