from tkinter import*
def connexion():
    connexion =Tk()
    connexion.configure(bg="#00aeff")
    connexion.title("Connexion")
    connexion.geometry("400x900+800+90")

    frame= Frame(connexion, width=400, height=800, highlightbackground="black", highlightthickness=2, highlightcolor='green',bg="gray")
    frame.winfo_geometry
    frame.pack(pady=210)



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

    #-----------button-------------
    saveBtn= Button(frame,text="connect", width=20, fg="red",font=("Italique", 13, "bold"),highlightbackground='#00aeff')
    saveBtn.pack(pady=30,ipady=10)


    connexion.mainloop()