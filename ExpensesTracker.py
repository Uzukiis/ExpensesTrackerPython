import shutil
from customtkinter import *
from PIL import Image
import os
import tkinter
from datetime import datetime
app = CTk()
app.geometry('1200x800')
app.title('Expenses Tracker')
app.resizable(False, False)
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

login_frame = CTkFrame(app)
login_frame.grid(row=0, column=0, sticky='news')
login_frame.columnconfigure(0, weight=1)
login_frame.rowconfigure(0, weight=1)
main_frame = CTkFrame(app)
main_frame.grid(row=0, column=0, sticky='news')
main_frame.columnconfigure(0, weight=3)
main_frame.columnconfigure(1, weight=8)
main_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
login_frame.tkraise()

calkowite_saldo = 0
zmianaBudzetu = ""
zmianaBudzetuText = ""
imie = ''
nazwisko = ''
max_idFiles = 0

def checkfile():
    global calkowite_saldo
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', 'calkowite_saldo')
    file_path = os.path.join(main_path, 'saldo.txt')
    if not os.path.exists(main_path):
        os.makedirs(main_path)
    else:
        try:
            with open(file_path, 'r') as file:
                calkowite_saldo = int(file.read())
                saldoValue.configure(text=f'{calkowite_saldo} zł')
                currentBudgetValueText.configure(text=f'{calkowite_saldo} zł')
        except Exception:
            print('ERROR #1')


def change_budget():
    global zmianaBudzetu
    global zmianaBudzetuText
    zmianaBudzetu = "ustaw"
    zmianaBudzetuText = "Ustaw nowy budżet"
    set_budget()


def add_budget():
    global zmianaBudzetu
    global zmianaBudzetuText
    zmianaBudzetu = "dodaj"
    zmianaBudzetuText = "Dodaj budżet"
    set_budget()


def subtract_budget():
    global zmianaBudzetu
    global zmianaBudzetuText
    zmianaBudzetu = "odejmij"
    zmianaBudzetuText = "Odejmij budżet"
    set_budget()

def set_budget(): #Window budget
    global setValue_var
    global setString_var
    global budgetwindow
    global calkowite_saldo
    budgetwindow = CTkToplevel()
    budgetwindow.geometry('500x300')
    budgetwindow.attributes("-topmost", True)
    budgetwindow.after(10, lambda: budgetwindow.focus_force())
    budgetwindow.resizable(width=False, height=False)
    CTkLabel(budgetwindow, text=zmianaBudzetuText, text_color=('#000000', '#ffffff'), font=('outfit', 28), fg_color=('#ebebeb', '#242424')).pack(pady=20)
    CTkEntry(budgetwindow, textvariable=setValue_var, placeholder_text=0).pack() #TODO po skonczeniu wyczyść tekst użytkownika do wartości początkowej 0
    CTkButton(budgetwindow, text='Gotowe', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', command=set_new_budget).pack(pady=20)

def set_new_budget(): #Program budget
    global calkowite_saldo
    global currentBudgetValueText
    global zmianaBudzetu
    try:
        if zmianaBudzetu == "ustaw":
            calkowite_saldo = setValue_var.get()  # Odczytaj wartość z obiektu StringVar()
        elif zmianaBudzetu == "dodaj":
            calkowite_saldo += setValue_var.get()  # Odczytaj wartość z obiektu StringVar()
        elif zmianaBudzetu == "odejmij":
            calkowite_saldo -= setValue_var.get()  # Odczytaj wartość z obiektu StringVar()
    except Exception:
        CTkLabel(budgetwindow, text='Wpisana wartość musi być liczbą!', text_color='#ff5555', font=('outfit', 28)).pack()
    else:
        saldoValue.configure(text=f'{calkowite_saldo} zł')
        currentBudgetValueText.configure(text=f'{calkowite_saldo} zł')
        budgetwindow.destroy()
        month = datetime.now().month
        year = datetime.now().year
        main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', f'{month}.{year}')
        zadanie = setString_var.get()

        if not os.path.exists(main_path):
            os.makedirs(main_path)
            max_idFiles = 0
        else:
            files = os.listdir(main_path)
            print(f'Pliki: {files}')
            max_idFiles = len(files)
            print(f'Max id: {max_idFiles}')

        max_idFiles = max_idFiles + 1
        file_path = os.path.join(main_path, f'{max_idFiles}.txt')
        with open(file_path,'w') as file:
            file.write(f'{zadanie};{setValue_var.get()}')
        with open(os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', 'calkowite_saldo', 'saldo.txt'), 'w') as file:
            file.write(str(calkowite_saldo))

def changeButton(funkcja): #Funkcje do zakladek
    frameFunkcji = [budzetFrame, wydatkiFrame, historiaFrame, ustawieniaFrame]
    button = [budzetbutton, wydatkibutton, historiabutton, ustawieniabutton]
    frameFunkcji[funkcja].tkraise()
    active_button = {'text_color': '#00A2E8', 'hover_color': ('#ebebeb', '#242424')}
    deactive_button = {'text_color': ('#000000', '#ffffff'), 'hover_color': '#00A2E8'}
    for x in frameFunkcji:
        if x == frameFunkcji:
            button[funkcja].configure(active_button)
        else:
            button[funkcja].configure(deactive_button)

def create_account():
    name = placeholderName.get().lower()
    lastname = placeholderLastName.get().lower()
    global imie
    global nazwisko
    imie = name
    nazwisko = lastname
    if not name.isspace() and name.isalpha() and not lastname.isspace() and lastname.isalpha():
        user_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{name}.{lastname}')
        if not os.path.exists(user_path):
            os.makedirs(user_path)
        checkfile()
        main_frame.tkraise()
        changeButton(1)

def connect_account(name, lastname):
    global imie
    global nazwisko
    imie=name
    nazwisko=lastname
    checkfile()
    main_frame.tkraise()
    changeButton(1)

CreateAccountFrame = CTkFrame(login_frame)
ListAccountFrame = CTkScrollableFrame(login_frame, orientation='vertical')

login_frame.columnconfigure((0, 1), weight=1)
login_frame.rowconfigure(0, weight=1)
CreateAccountFrame.grid(row=0, column=0, sticky='nsew')
ListAccountFrame.grid(row=0, column=1, sticky='nsew')

# Create Account Frame
imgProfile = CTkImage(dark_image=Image.open('./Images/icon-create-account.png'), size=(100, 100))
CTkLabel(CreateAccountFrame, image=imgProfile, text='').place(relx=0.5, rely=0.40, anchor='center')
placeholderName = CTkEntry(CreateAccountFrame, placeholder_text='Imię', width=200, height=35)
placeholderName.place(relx=0.5, rely=0.5, anchor='center')
placeholderLastName = CTkEntry(CreateAccountFrame, placeholder_text='Nazwisko', width=200, height=35)
placeholderLastName.place(relx=0.5, rely=0.55, anchor='center')
CTkButton(CreateAccountFrame, text='Create Account', corner_radius=15, width=150, height=30, command=create_account).place(relx=0.5, rely=0.62, anchor='center')

def check_account():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker')
    if not os.path.exists(main_path):
        os.makedirs(main_path)
    users = os.listdir(main_path)
    # List Account Frame
    for x in users:
        n = x.split('.')
        CTkButton(ListAccountFrame, height=80, text=f'{n[0].capitalize()} {n[1].capitalize()}', command=lambda name=n[0], lastname=n[1]: connect_account(name, lastname), font=('Helvetica', 24)).pack(pady=10, fill='x')

check_account()

# zakładki
saldoValue = CTkLabel(main_frame, text=f'{calkowite_saldo} zł', text_color=('#000000', '#ffffff'), font=('outfit', 28))
saldoValue.grid(row=0, column=0, sticky='nswe')

styleButton = {'text_color':('#000000', '#ffffff'), 'font':('outfit', 28), 'fg_color':('#ebebeb', '#242424'), 'hover_color':'#00A2E8', 'text_color_disabled':'#00A2E8'}
budzetbutton = CTkButton(main_frame, text='Budżet', **styleButton, command=lambda: changeButton(0))
budzetbutton.grid(row=1, column=0, sticky='nswe')

wydatkibutton = CTkButton(main_frame, text='Wydatki', **styleButton, command=lambda: changeButton(1))
wydatkibutton.grid(row=2, column=0, sticky='nswe')

historiabutton = CTkButton(main_frame, text='Historia', **styleButton, command=lambda: changeButton(2))
historiabutton.grid(row=3, column=0, sticky='nswe')

ustawieniabutton = CTkButton(main_frame, text='Ustawienia', **styleButton, command=lambda: changeButton(3))
ustawieniabutton.grid(row=4, column=0, sticky='nswe')

#prawa strona
wydatkiFrame = CTkFrame(main_frame)
CTkLabel(wydatkiFrame, text='wydatki text').pack()

wydatkiFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')

budzetFrame = CTkFrame(main_frame)
(CTkLabel(budzetFrame,
        text='Obecny budżet: ',
        text_color=('#000000', '#ffffff'),
        font=('outfit', 28)
          ).grid(row=1, column=1, sticky='nswe'))
currentBudgetValueText = CTkLabel(budzetFrame, text=f'{calkowite_saldo} zł', text_color=('#000000', '#ffffff'), font=('outfit', 28))
CTkButton(budzetFrame, text='Ustaw nowy budżet', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', width=300, command=change_budget).grid(row=3, column=1)
setValue_var = tkinter.IntVar()
setString_var = tkinter.StringVar()
CTkButton(budzetFrame, text="-", text_color='#ffffff', font=('outfit', 28), fg_color='#aa3333', hover_color='#991111',command=subtract_budget).grid(row=3, column=0, sticky="e")
CTkButton(budzetFrame, text="+", text_color='#ffffff', font=('outfit', 28), fg_color='#33aa33', hover_color='#118811',command=add_budget).grid(row=3, column=2, sticky="w")
currentBudgetValueText.grid(row=2, column=1)

budzetFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')
budzetFrame.columnconfigure((0,1,2),weight=1)
budzetFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)



historiaFrame = CTkFrame(main_frame)
CTkLabel(historiaFrame, text='historia text').pack()
historiaFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')

ustawieniaFrame = CTkFrame(main_frame)
ustawieniaFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')

CTkLabel(ustawieniaFrame, text='Ustaw tryb aplikacji').pack()


def changeTheme(value):
    match value:
        case 'Systemowy':
            set_appearance_mode('system')
        case 'Jasny':
            set_appearance_mode('light')
        case 'Ciemny':
            set_appearance_mode('dark')


optionmenu_var = StringVar(value='Systemowy')
Opcja = CTkOptionMenu(ustawieniaFrame, values=['Systemowy', 'Jasny', 'Ciemny'], command=lambda value=optionmenu_var.get(): changeTheme(value), variable=optionmenu_var).pack()

def deleteAccount():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}')
    shutil.rmtree(main_path)
    sys.exit()

def deleteApplication():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker')
    shutil.rmtree(main_path)
    sys.exit()

def ExitApplication():
    sys.exit()

CTkLabel(ustawieniaFrame, text='Inne ustawienia').pack()
CTkButton(ustawieniaFrame, text='Usuń konto', fg_color='#aa3333', hover_color='#991111', command=deleteAccount).pack(pady=20)
CTkButton(ustawieniaFrame, text='Usuń wszystkie dane z aplikacji', fg_color='#aa3333', hover_color='#991111', command=deleteApplication).pack(pady=20)
CTkButton(ustawieniaFrame, text='Wyłącz aplikacje', command=ExitApplication).pack(pady=40)

app.mainloop()
