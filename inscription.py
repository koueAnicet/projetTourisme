
from tkinter import*
def inscription():
    inscription =Tk()
    inscription.configure()
    inscription.title("Inscripton")
    inscription.geometry("400x900+800+90")
    inscription.configure(bg="#54add6")

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


    inscription.mainloop()