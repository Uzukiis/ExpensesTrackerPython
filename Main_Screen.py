import customtkinter as ctk
import fonts
import tkinter


saldo=0


#window
window = ctk.CTk()
window.title("Expenses Tracker")
window.geometry("1280x800")
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=8)
window.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
#funkcje do zakładek
def budzetFunkcja():
    budzetFrame.tkraise()
    budzetbutton.configure(state="disabled")
    wydatkibutton.configure(state="normal")
    historiabutton.configure(state="normal")
    ustawieniabutton.configure(state="normal")
def wydatkiFunkcja():
    wydatkiFrame.tkraise()
    budzetbutton.configure(state="normal")
    wydatkibutton.configure(state="disabled")
    historiabutton.configure(state="normal")
    ustawieniabutton.configure(state="normal")
def historiaFunkcja():
    historiaFrame.tkraise()
    budzetbutton.configure(state="normal")
    wydatkibutton.configure(state="normal")
    historiabutton.configure(state="disabled")
    ustawieniabutton.configure(state="normal")
def ustawieniaFunkcja():
    ustawieniaFrame.tkraise()
    budzetbutton.configure(state="normal")
    wydatkibutton.configure(state="normal")
    historiabutton.configure(state="normal")
    ustawieniabutton.configure(state="disabled")

#inne funkcje
def trybFunkcja():
    global tryb
    wybranyTryb = tryb.get()
    print(tryb)


#zakładki
saldo=ctk.CTkLabel(window,
                   text=f"{saldo}zł",
                   text_color=("#000000","#ffffff"),
                   font=("outfit",28))
saldo.grid(row=0,column=0,sticky="nswe")
budzetbutton = ctk.CTkButton(window,
                            text = "Budżet",
                            text_color=("#000000","#ffffff"),
                            font=("outfit",28),
                            fg_color=("#ebebeb","#242424"),
                            hover_color="#00A2E8",
                            text_color_disabled="#00A2E8",
                            command = budzetFunkcja)
budzetbutton.grid(row=1, column=0, sticky="nswe")

wydatkibutton = ctk.CTkButton(window,
                            text = "Wydatki",
                            text_color=("#000000","#ffffff"),
                            font=("outfit",28),
                            fg_color=("#ebebeb","#242424"),
                            hover_color="#00A2E8",
                            text_color_disabled="#00A2E8",
                            command = wydatkiFunkcja)
wydatkibutton.grid(row=2, column=0, sticky="nswe")

historiabutton = ctk.CTkButton(window,
                            text = "Historia",
                            text_color=("#000000","#ffffff"),
                            font=("outfit",28),
                            fg_color=("#ebebeb","#242424"),
                            hover_color="#00A2E8",
                            text_color_disabled="#00A2E8",
                            command = historiaFunkcja)
historiabutton.grid(row=3, column=0, sticky="nswe")

ustawieniabutton = ctk.CTkButton(window,
                                text = "Ustawienia",
                                text_color=("#000000","#ffffff"),
                                font=("outfit",28),
                                fg_color=("#ebebeb","#242424"),
                                hover_color="#00A2E8",
                                text_color_disabled="#00A2E8",
                                command = ustawieniaFunkcja)
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
ustawieniatekst=ctk.CTkLabel(ustawieniaFrame, text="Ustaw tryb aplikacji")
ustawieniatekst.pack()


tryb = tkinter.IntVar(value=0)
sysmode = ctk.CTkRadioButton(ustawieniaFrame, text="Taki jak system",
                                             command = lambda: ctk.set_appearance_mode("system"), variable= tryb, value=1)
lightmode = ctk.CTkRadioButton(ustawieniaFrame, text="Tryb jasny",
                                             command=lambda: ctk.set_appearance_mode("light"), variable= tryb, value=2)
darkmode = ctk.CTkRadioButton(ustawieniaFrame, text="Tryb ciemny",
                                             command=lambda: ctk.set_appearance_mode("dark"), variable= tryb, value=3)
sysmode.pack()
lightmode.pack()
darkmode.pack()

ustawieniaFrame.grid(row=0,column=1,rowspan=8,sticky="nswe")

wydatkiFunkcja()


window.mainloop()
