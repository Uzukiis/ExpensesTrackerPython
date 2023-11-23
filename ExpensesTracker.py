from customtkinter import *
from PIL import Image
import os
import tkinter

saldo = 0

app = CTk()
app.geometry('1200x800')
app.title('Expenses Tracker')
app.resizable(False, False)

login_frame = CTkFrame(app)
main_frame = CTkFrame(app)

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
login_frame.grid(row=0, column=0, sticky='news')
main_frame.grid(row=0, column=0, sticky='news')
login_frame.columnconfigure(0, weight=1)
login_frame.rowconfigure(0, weight=1)

login_frame.tkraise()

main_frame.columnconfigure(0, weight=3)
main_frame.columnconfigure(1, weight=8)
main_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)


# funkcje do zakładek

# Budżet
def budzet_funkcja():
    budzetFrame.tkraise()
    budzetbutton.configure(text_color="#00A2E8", hover_color=("#ebebeb", "#242424"))
    wydatkibutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    historiabutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    ustawieniabutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")


def set_budget():
    global notAValueText
    global setValue_var
    global budgetwindow
    budgetwindow = CTkToplevel()
    budgetwindow.geometry('500x300')
    budgetwindow.resizable(width=False, height=False)
    CTkLabel(budgetwindow,
             text="Ustaw nowy budżet",
             text_color=("#000000", "#ffffff"),
             font=("outfit", 28),
             fg_color=("#ebebeb", "#242424")).pack(pady=20)
    CTkEntry(budgetwindow, textvariable=setValue_var, placeholder_text=saldo).pack()
    CTkButton(budgetwindow,
              text="Gotowe",
              text_color="#ffffff",
              font=("outfit", 28),
              fg_color="#00A2E8",
              hover_color="#0082C8",
              text_color_disabled="#00A2E8",
              command=set_new_budget).pack(pady=20)
    notAValueText = CTkLabel(
        budgetwindow,
        text="Wpisana wartość musi być liczbą!",
        text_color="#ff5555",
        font=("outfit", 28),
    )


def set_new_budget():
    try:
        saldo = setValue_var.get()  # odczytaj wartość z obiektu StringVar()
    except Exception:
        notAValueText.pack()
    else:
        budgetwindow.destroy()
        saldoValue.configure(text=f"{saldo} zł")
        currentBudgetValueText.configure(text=f"{saldo} zł")


def wydatki_funkcja():
    wydatkiFrame.tkraise()
    budzetbutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    wydatkibutton.configure(text_color="#00A2E8", hover_color=("#ebebeb", "#242424"))
    historiabutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    ustawieniabutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")


def historia_funkcja():
    historiaFrame.tkraise()
    budzetbutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    wydatkibutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    historiabutton.configure(text_color="#00A2E8", hover_color=("#ebebeb", "#242424"))
    ustawieniabutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")


def ustawienia_funkcja():
    ustawieniaFrame.tkraise()
    budzetbutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    wydatkibutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    historiabutton.configure(text_color=("#000000", "#ffffff"), hover_color="#00A2E8")
    ustawieniabutton.configure(text_color="#00A2E8", hover_color=("#ebebeb", "#242424"))


# inne funkcje


def create_account():
    name = placeholderName.get().lower()
    lastname = placeholderLastName.get().lower()
    if not name.isspace() and name.isalpha() and not lastname.isspace() and lastname.isalpha():
        user_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{name}.{lastname}')
        if not os.path.exists(user_path):
            os.makedirs(user_path)
        print(user_path)  # TODO transition to main page
        main_frame.tkraise()


def connect_account(name, lastname):
    print(f'{name}.{lastname}')  # TODO transition to main page
    main_frame.tkraise()
    wydatki_funkcja()


# zakładki
saldoValue = CTkLabel(main_frame,
                      text=f"{saldo} zł",
                      text_color=("#000000", "#ffffff"),
                      font=("outfit", 28))
saldoValue.grid(row=0, column=0, sticky="nswe")
budzetbutton = CTkButton(main_frame,
                         text="Budżet",
                         text_color=("#000000", "#ffffff"),
                         font=("outfit", 28),
                         fg_color=("#ebebeb", "#242424"),
                         hover_color="#00A2E8",
                         text_color_disabled="#00A2E8",
                         command=budzet_funkcja)
budzetbutton.grid(row=1, column=0, sticky="nswe")

wydatkibutton = CTkButton(main_frame,
                          text="Wydatki",
                          text_color=("#000000", "#ffffff"),
                          font=("outfit", 28),
                          fg_color=("#ebebeb", "#242424"),
                          hover_color="#00A2E8",
                          text_color_disabled="#00A2E8",
                          command=wydatki_funkcja)
wydatkibutton.grid(row=2, column=0, sticky="nswe")

historiabutton = CTkButton(main_frame,
                           text="Historia",
                           text_color=("#000000", "#ffffff"),
                           font=("outfit", 28),
                           fg_color=("#ebebeb", "#242424"),
                           hover_color="#00A2E8",
                           text_color_disabled="#00A2E8",
                           command=historia_funkcja)
historiabutton.grid(row=3, column=0, sticky="nswe")

ustawieniabutton = CTkButton(main_frame,
                             text="Ustawienia",
                             text_color=("#000000", "#ffffff"),
                             font=("outfit", 28),
                             fg_color=("#ebebeb", "#242424"),
                             hover_color="#00A2E8",
                             text_color_disabled="#00A2E8",
                             command=ustawienia_funkcja)
ustawieniabutton.grid(row=4, column=0, sticky="nswe")

# prawa strona
wydatkiFrame = CTkFrame(main_frame)
CTkLabel(wydatkiFrame, text="wydatki text").pack()

wydatkiFrame.grid(row=0, column=1, rowspan=8, sticky="nswe")

budzetFrame = CTkFrame(main_frame)
BudgetText = CTkLabel(budzetFrame, text="Obecny budżet: ",
                      text_color=("#000000", "#ffffff"),
                      font=("outfit", 28))
currentBudgetValueText = CTkLabel(budzetFrame, text=f"{saldo} zł",
                                  text_color=("#000000", "#ffffff"),
                                  font=("outfit", 28))
setBudgetButton = CTkButton(budzetFrame,
                            text="Ustaw budżet",
                            text_color="#ffffff",
                            font=("outfit", 28),
                            fg_color="#00A2E8",
                            hover_color="#0082C8",
                            text_color_disabled="#00A2E8",
                            command=set_budget)
setValue_var = tkinter.IntVar()

BudgetText.pack(pady=100)
currentBudgetValueText.pack()
setBudgetButton.pack(pady=100)
tryb = tkinter.StringVar(value=0)
budzetFrame.grid(row=0, column=1, rowspan=8, sticky="nswe")

historiaFrame = CTkFrame(main_frame)
historiatekst = CTkLabel(historiaFrame, text="historia text")
historiatekst.pack()
historiaFrame.grid(row=0, column=1, rowspan=8, sticky="nswe")

ustawieniaFrame = CTkFrame(main_frame)
CTkLabel(ustawieniaFrame, text="Ustaw tryb aplikacji").pack()
CTkRadioButton(ustawieniaFrame, text="Taki jak system",
               command=lambda: set_appearance_mode("system"), variable=tryb, value=1).pack()
CTkRadioButton(ustawieniaFrame, text="Tryb jasny",
               command=lambda: set_appearance_mode("light"), variable=tryb, value=2).pack()
CTkRadioButton(ustawieniaFrame, text="Tryb ciemny",
               command=lambda: set_appearance_mode("dark"), variable=tryb, value=3).pack()

ustawieniaFrame.grid(row=0, column=1, rowspan=8, sticky="nswe")

CreateAccountFrame = CTkFrame(login_frame)
ListAccountFrame = CTkScrollableFrame(login_frame, orientation='vertical')

login_frame.columnconfigure((0, 1), weight=1)
login_frame.rowconfigure(0, weight=1)
CreateAccountFrame.grid(row=0, column=0, sticky='nsew')
ListAccountFrame.grid(row=0, column=1, sticky='nsew')

# Create Account Frame
imgProfile = CTkImage(dark_image=Image.open('./Images/icon-create-account.png'), size=(100, 100))
profile = CTkLabel(CreateAccountFrame, image=imgProfile, text='').place(relx=0.5, rely=0.40, anchor='center')
placeholderName = CTkEntry(CreateAccountFrame, placeholder_text='Name', width=200, height=35)
placeholderName.place(relx=0.5, rely=0.5, anchor='center')
placeholderLastName = CTkEntry(CreateAccountFrame, placeholder_text='Last name', width=200, height=35)
placeholderLastName.place(relx=0.5, rely=0.55, anchor='center')
CTkButton(CreateAccountFrame, text='Create Account', corner_radius=15, width=150, height=30,
          command=create_account).place(relx=0.5, rely=0.62, anchor='center')


def check_account():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker')
    if not os.path.exists(main_path):
        os.makedirs(main_path)
    users = os.listdir(main_path)
    # List Account Frame
    for x in users:
        n = x.split('.')
        CTkButton(ListAccountFrame, height=80, text=f'{n[0].capitalize()} {n[1].capitalize()}',
                  command=lambda name=n[0], lastname=n[1]: connect_account(name, lastname),
                  font=('Helvetica', 24)).pack(pady=10, fill='x')


check_account()

app.mainloop()
