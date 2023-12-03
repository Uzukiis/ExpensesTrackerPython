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
        with open(file_path, 'w') as file:
            file.write('0')
    else:
        try:
            with open(file_path, 'r') as file:
                calkowite_saldo = int(file.read())
                saldoValue.configure(text=f'{calkowite_saldo} zł')
                currentBudgetValueText.configure(text=f'{calkowite_saldo} zł')
        except Exception:
            print('ERROR #1')

def budget_operation(operation):
    global zmianaBudzetu
    global zmianaBudzetuText
    match operation:
        case 'ustawianie':
            zmianaBudzetu = "ustaw"
            zmianaBudzetuText = "Ustaw nowy budżet"
        case 'dodawanie':
            zmianaBudzetu = "dodaj"
            zmianaBudzetuText = "Dodaj budżet"
        case 'odejmowanie':
            zmianaBudzetu = "odejmij"
            zmianaBudzetuText = "Odejmij budżet"
    set_budget()

def set_budget(): #Window budget
    global setValue_var
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
    history_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}','historia')

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
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        milisecond = datetime.now().microsecond // 1000
        main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}','saldo', f'{month}.{year}')
        history_file_path = os.path.join(history_path, f'{year}.{month}.{day}_{hour}.{minute}.{second}.{milisecond}.txt')
        with open(history_file_path, 'w') as file:
            file.write(f'{year}.{month}.{day} {hour}.{minute}/{zmianaBudzetu}')
        if zmianaBudzetu != 'ustaw':
            if not os.path.exists(main_path):
                os.makedirs(main_path)
                max_idFiles = 0
            else:
                files = os.listdir(main_path)
                max_idFiles = len(files)

            max_idFiles = max_idFiles + 1
            file_path = os.path.join(main_path, f'{max_idFiles}.txt')
            with open(file_path,'w') as file:
                file.write(f'{zmianaBudzetu};{setValue_var.get()}')
        with open(os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', 'calkowite_saldo', 'saldo.txt'), 'w') as file:
            file.write(str(calkowite_saldo))

def changeButton(funkcja): #Funkcje do zakladek
    frameFunkcji = [budzetFrame, wydatkiFrame, historiaFrame, ustawieniaFrame]
    button = [budzetbutton, wydatkibutton, historiabutton, ustawieniabutton]

    history_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}','historia')
    wydatki_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}','wydatki')

    if funkcja == 1:
        if not os.path.exists(wydatki_path):
            os.makedirs(wydatki_path)
        else:
            wydatki = os.listdir(wydatki_path)
            n=0
            if len(wydatki) != 0:
                for h in reversed(wydatki):
                    with open(os.path.join(wydatki_path, h), 'r') as file:
                        zawartosc = file.read()
                        zawartosc = zawartosc.split('/')
                        n+=1
                        #TODO: frame do zmiany

            #             CTkLabel(ListHistoryFrame, text=f'{zawartosc[0].capitalize()}             {zawartosc[1].capitalize()}            {zawartosc[2].capitalize()}', font=('Helvetica', 24), height=60, width=600, fg_color=('#ebebeb', '#242424')).grid(row=n, column=1, pady=10)
            # else:
            #     CTkLabel(ListHistoryFrame, text=f'Nic tu nie ma', font=('Helvetica', 24), height=60, width=600, fg_color='#00A2E8').grid(row=1, column=1)

    if funkcja == 2:
        if not os.path.exists(history_path):
            os.makedirs(history_path)
        else:
            history = os.listdir(history_path)
            n=0
            if len(history) != 0:
                for h in reversed(history):
                    with open(os.path.join(history_path, h), 'r') as file:
                        zawartosc = file.read()
                        zawartosc = zawartosc.split('/')
                        n+=1
                        CTkLabel(ListHistoryFrame, text=f'{zawartosc[0].capitalize()}                              {zawartosc[1].capitalize()}', font=('Helvetica', 24), height=60, width=600, fg_color=('#ebebeb', '#242424')).grid(row=n, column=1, pady=10)
            else:
                CTkLabel(ListHistoryFrame, text=f'Nic tu nie ma', font=('Helvetica', 24), height=60, width=600, fg_color='#00A2E8').grid(row=1, column=1)
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
    imie = name
    nazwisko = lastname
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
wydatkiFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')
wydatkiFrame.columnconfigure(0, weight=1)
wydatkiFrame.rowconfigure(0, weight=1)
listWydatkiFrame = CTkScrollableFrame(wydatkiFrame,orientation='vertical', fg_color=("#CFCFCF", "#333333"))
listWydatkiFrame.grid(sticky='nswe')
listWydatkiFrame.columnconfigure((0,1,2),weight=1)


expenseCostVar = tkinter.StringVar()

def add_new_expense(kategoria, koszt):
    global calkowite_saldo
    print(koszt)
    print(kategoria)
    wydatki_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}', 'wydatki')
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    milisecond = datetime.now().microsecond // 1000
    wydatki_file_path = os.path.join(wydatki_path, f'{year}.{month}.{day}_{hour}.{minute}.{second}.{milisecond}.txt')

    koszt = int(koszt)
    calkowite_saldo -= koszt
    saldoValue.configure(text=f'{calkowite_saldo} zł')
    currentBudgetValueText.configure(text=f'{calkowite_saldo} zł')

    with open(wydatki_file_path, 'w') as file:
        file.write(f'{year}.{month}.{day} {hour}.{minute}/{kategoria}/{koszt}')

    expensewindow.destroy()
def nowy_wydatek():
    global expensewindow
    global opcja
    global koszt_wydatku
    expensewindow = CTkToplevel()
    expensewindow.geometry('500x350')
    expensewindow.attributes("-topmost", True)
    expensewindow.after(10, lambda: expensewindow.focus_force())
    expensewindow.resizable(width=False, height=False)
    CTkLabel(expensewindow, text="Dodaj wydatek", text_color=('#000000', '#ffffff'), font=('outfit', 28), fg_color=('#ebebeb', '#242424')).pack(pady=30)
    koszt_wydatku = CTkLabel(expensewindow, text="Podaj koszt wydatku").pack(pady=10)
    CTkEntry(expensewindow, textvariable=expenseCostVar, placeholder_text=0).pack()
    CTkLabel(expensewindow,text="Wybierz kategorię").pack(pady=10)
    expenseCategory_Var = StringVar()
    opcja = CTkOptionMenu(expensewindow, values=['Zakupy', 'Podróż', 'Rozrywka'], variable = expenseCategory_Var,).pack()
    CTkButton(expensewindow, text='Gotowe', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', command= lambda: add_new_expense(expenseCategory_Var.get(), expenseCostVar.get())).pack(pady=20)


CTkButton(listWydatkiFrame, text='Dodaj wydatek', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', width=300, command=nowy_wydatek).pack()

budzetFrame = CTkFrame(main_frame)
(CTkLabel(budzetFrame,
        text='Obecny budżet: ',
        text_color=('#000000', '#ffffff'),
        font=('outfit', 28)
          ).grid(row=1, column=1, sticky='nswe'))
currentBudgetValueText = CTkLabel(budzetFrame, text=f'{calkowite_saldo} zł', text_color=('#000000', '#ffffff'), font=('outfit', 28))
CTkButton(budzetFrame, text='Ustaw nowy budżet', text_color='#ffffff', font=('outfit', 28), fg_color='#00A2E8', hover_color='#0082C8', text_color_disabled='#00A2E8', width=300, command=lambda: budget_operation('ustawianie')).grid(row=3, column=1)
setValue_var = tkinter.IntVar()
CTkButton(budzetFrame, text="-", text_color='#ffffff', font=('outfit', 28), fg_color='#aa3333', hover_color='#991111',command=lambda: budget_operation('odejmowanie')).grid(row=3, column=0, sticky="e")
CTkButton(budzetFrame, text="+", text_color='#ffffff', font=('outfit', 28), fg_color='#33aa33', hover_color='#118811',command=lambda: budget_operation('dodawanie')).grid(row=3, column=2, sticky="w")
currentBudgetValueText.grid(row=2, column=1)

budzetFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')
budzetFrame.columnconfigure((0,1,2),weight=1)
budzetFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)

historiaFrame = CTkFrame(main_frame)
historiaFrame.grid(row=0, column=1, rowspan=8, sticky='nswe')
historiaFrame.columnconfigure(0, weight=1)
historiaFrame.rowconfigure(0, weight=1)
ListHistoryFrame = CTkScrollableFrame(historiaFrame, orientation='vertical', fg_color=("#CFCFCF", "#333333"))
ListHistoryFrame.grid(sticky='nswe')
ListHistoryFrame.columnconfigure((0,1,2),weight=1)
CTkLabel(ListHistoryFrame,text="HISTORIA").grid(column=1)

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
CTkOptionMenu(ustawieniaFrame, values=['Systemowy', 'Jasny', 'Ciemny'], command=lambda value=optionmenu_var.get(): changeTheme(value), variable=optionmenu_var).pack()

def deleteAccount():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{imie}.{nazwisko}')
    shutil.rmtree(main_path)
    sys.exit()

def deleteApplication():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker')
    shutil.rmtree(main_path)
    sys.exit()

def exitApplication():
    sys.exit()

CTkLabel(ustawieniaFrame, text='Inne ustawienia').pack()
CTkButton(ustawieniaFrame, text='Usuń konto', fg_color='#aa3333', hover_color='#991111', command=deleteAccount).pack(pady=20)
CTkButton(ustawieniaFrame, text='Usuń wszystkie dane z aplikacji', fg_color='#aa3333', hover_color='#991111', command=deleteApplication).pack(pady=20)
CTkButton(ustawieniaFrame, text='Wyłącz aplikacje', command=exitApplication).pack(pady=40)
app.mainloop()
