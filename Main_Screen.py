import customtkinter as ctk
import fonts

#zmienne
saldo=0
obecnyframe="wydatki"




#window
window = ctk.CTk()
window.title("Expense Tracker")
window.geometry("1280x800")
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=8)
window.rowconfigure((0,1,2,3,4,5,6,7), weight=1)


#zakładki
saldo=ctk.CTkLabel(window,
                   text=f"{saldo}zł",
                   text_color=("#000000","#ffffff"),
                   font=("outfit",28))
saldo.grid(row=0,column=0,sticky="nswe")
budzetbutton = ctk.CTkButton(window,
                            text = "Budżet",
                            font=("outfit",28),
                            fg_color="#242424",
                            command = lambda: budzetFrame.tkraise())
budzetbutton.grid(row=1, column=0, sticky="nswe")

wydatkibutton = ctk.CTkButton(window,
                            text = "Wydatki",
                            font=("outfit",28),
                            fg_color="#242424",
                            command = lambda: wydatkiFrame.tkraise())
wydatkibutton.grid(row=2, column=0, sticky="nswe")

historiabutton = ctk.CTkButton(window,
                            text = "Historia",
                            font=("outfit",28),
                            fg_color="#242424",
                            command = lambda: historiaFrame.tkraise())
historiabutton.grid(row=3, column=0, sticky="nswe")

ustawieniabutton = ctk.CTkButton(window,
                                text = "Ustawienia",
                                font=("outfit",28),
                                fg_color="#242424",
                                command=lambda: ustawieniaFrame.tkraise())
ustawieniabutton.grid(row=4, column=0, sticky="nswe")

#prawa strona
wydatkiFrame = ctk.CTkFrame(window)
wydatkitekst=ctk.CTkLabel(wydatkiFrame, text="wydatki text")
wydatkitekst.pack()
wydatkiFrame.grid(row=0,column=1,rowspan=8,sticky="nswe")

budzetFrame = ctk.CTkFrame(window)
budzettekst=ctk.CTkLabel(budzetFrame, text="budzet text")
budzettekst.pack()
budzetFrame.grid(row=0,column=1,rowspan=8,sticky="nswe")

historiaFrame = ctk.CTkFrame(window)
historiatekst=ctk.CTkLabel(historiaFrame, text="historia text")
historiatekst.pack()
historiaFrame.grid(row=0,column=1,rowspan=8,sticky="nswe")

ustawieniaFrame = ctk.CTkFrame(window)
ustawieniatekst=ctk.CTkLabel(ustawieniaFrame, text="ustawienia text")
ustawieniatekst.pack()
ustawieniaFrame.grid(row=0,column=1,rowspan=8,sticky="nswe")


window.mainloop()