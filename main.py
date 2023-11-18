from customtkinter import *
from PIL import Image
import os

def create_account():
    name = placeholderName.get().lower()
    lastname = placeholderLastName.get().lower()
    if not name.isspace() and name.isalpha() and not lastname.isspace() and lastname.isalpha():
        user_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker', f'{name}.{lastname}')
        if not os.path.exists(user_path):
            os.makedirs(user_path)
        print(user_path) #TODO transition to main page

def connect_account(name, lastname):
    print(f'{name}.{lastname}')

app = CTk()
app.geometry('1200x800')
app.title('Expenses Tracker')
app.resizable(False, False)

CreateAccountFrame = CTkFrame(app)
ListAccountFrame = CTkScrollableFrame(app, orientation='vertical')

app.columnconfigure((0,1), weight=1)
app.rowconfigure(0, weight=1)
CreateAccountFrame.grid(row=0, column=0, sticky='nsew')
ListAccountFrame.grid(row=0, column=1, sticky='nsew')

#TODO color font white and black
#Create Account Frame
imgProfile = CTkImage(dark_image=Image.open('./Images/icon-create-account.png'), size=(100,100))
profile = CTkLabel(CreateAccountFrame, image=imgProfile, text='').place(relx=0.5, rely=0.40, anchor='center')
placeholderName = CTkEntry(CreateAccountFrame, placeholder_text='Name', width=200, height=35)
placeholderName.place(relx=0.5, rely=0.5, anchor='center')
placeholderLastName = CTkEntry(CreateAccountFrame, placeholder_text='Last name', width=200, height=35)
placeholderLastName.place(relx=0.5, rely=0.55, anchor='center')
CTkButton(CreateAccountFrame, text='Create Account', corner_radius=15, width=150, height=30, command=create_account).place(relx=0.5, rely=0.62, anchor='center')

def check_account():
    main_path = os.path.join(os.path.expanduser('~'), 'Documents', 'Expenses_Tracker')
    if not os.path.exists(main_path):
        os.makedirs(main_path)
    users = os.listdir(main_path)
#List Account Frame
    for x in users:
        n = x.split('.')
        CTkButton(ListAccountFrame, height=80, text=f'{n[0].capitalize()} {n[1].capitalize()}', command=lambda name=n[0], lastname=n[1]: connect_account(name, lastname), font=('Helvetica', 24)).pack(pady=10, fill='x')

check_account()

app.mainloop()