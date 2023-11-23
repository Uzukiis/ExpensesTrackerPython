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
def set_budget(): #Window budget
    global setValue_var
    global setString_var
    global budgetwindow
    global calkowite_saldo
    budgetwindow = CTkToplevel()
    budgetwindow.geometry('500x300')
    budgetwindow.resizable(width=False, height=False)
    CTkLabel(budgetwindow, text='Ustaw nowy budżet', text_color=('#000000', '#ffffff'), font=('outfit', 28), fg_color=('#ebebeb', '#242424')).pack(pady=20)
    CTkEntry(budgetwindow, textvariable=setValue_var, placeholder_text=0).pack() #TODO po skonczeniu wyczyść tekst użytkownika do wartości początkowej 0
    CTkEntry(budgetwindow, textvariable=setString_var, placeholder_text='Zadanie').pack() #TODO po skonczeniu wyczyść tekst użytkownika
    CTkButton(budgetwindow, text='Gotowe', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', command=set_new_budget).pack(pady=20)

def set_new_budget(): #Program budget
    global calkowite_saldo
    try:
        calkowite_saldo += setValue_var.get()  #Odczytaj wartość z obiektu StringVar()
    except Exception:
        CTkLabel(budgetwindow, text='Wpisana wartość musi być liczbą!', text_color='#ff5555', font=('outfit', 28)).pack()
    else:
        budgetwindow.destroy()
        saldoValue.configure(text=f'{calkowite_saldo} zł')
        currentBudgetValueText.configure(text=f'{calkowite_saldo} zł')
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', f'{year}.{month}.{day}')
        zadanie = setString_var.get()
        if not os.path.exists(main_path):
            os.makedirs(main_path)
        file_path = os.path.join(main_path, f'Zadanie.txt')
        with open(file_path,'w') as file:
            file.write(f'{zadanie};{setValue_var.get()}')
        with open(os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', 'calkowite_saldo', 'saldo.txt'), 'w') as file:
            file.write(str(calkowite_saldo))

def changeButton(funkcja): #Funkcje do zakladek
    frameFunkcji = [budzetFrame, wydatkiFrame, historiaFrame, ustawieniaFrame]
    button = [budzetbutton, wydatkibutton, historiabutton, ustawieniabutton]
    frameFunkcji[funkcja].tkraise()
    active_button = {'text_color': '#00A2E8','hover_color': ('#ebebeb', '#242424')}
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
CTkLabel(budzetFrame, text='Obecny budżet: ', text_color=('#000000', '#ffffff'), font=('outfit', 28)).pack(pady=100)
currentBudgetValueText = CTkLabel(budzetFrame, text=f'{calkowite_saldo} zł', text_color=('#000000', '#ffffff'), font=('outfit', 28))
CTkButton(budzetFrame, text='Ustaw budżet', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', command=set_budget).pack(pady=100)
setValue_var = tkinter.IntVar()
setString_var = tkinter.StringVar()

currentBudgetValueText.pack()
tryb = tkinter.StringVar(value=0)
budzetFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')

historiaFrame = CTkFrame(main_frame)
CTkLabel(historiaFrame, text='historia text').pack()
historiaFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')

ustawieniaFrame = CTkFrame(main_frame)
CTkLabel(ustawieniaFrame, text='Ustaw tryb aplikacji').pack()
CTkRadioButton(ustawieniaFrame, text='Taki jak system', command=lambda: set_appearance_mode('system'), variable=tryb, value=1).pack()
CTkRadioButton(ustawieniaFrame, text='Tryb jasny', command=lambda: set_appearance_mode('light'), variable=tryb, value=2).pack()
CTkRadioButton(ustawieniaFrame, text='Tryb ciemny', command=lambda: set_appearance_mode('dark'), variable=tryb, value=3).pack()
ustawieniaFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')

app.mainloop()