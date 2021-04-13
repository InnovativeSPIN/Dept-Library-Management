from utils import *
import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from frontend import *

CURRENT_USER = None

conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()

window = tk.Tk()
window.geometry('1366x768')
window.minsize(1366, 768)
window.maxsize(1366, 768)
window.title('Library Management System')

log_page = LoginPage(window)


def just_new():
    new_title = tk.Label(window, text='New User', font=('times new roman', 25), bg='white', fg='blue')
    new_title.place(x=1080, y=150)

    new_user_lable = tk.Label(window, text='Username :', bg='white', font=(None, 15))
    new_user_lable.place(x=1000, y=220)

    new_user_box = tk.Entry(window, borderwidth=2, bg='white', font=('times new roman', 14))
    new_user_box.place(x=1120, y=220)

    new_pass_lable = tk.Label(window, text='New Password : ', bg='white', font=(None, 15))
    new_pass_lable.place(x=960, y=270)

    new_pass_box = tk.Entry(window, borderwidth=2, bg='white', font=('times new roman', 14))
    new_pass_box.place(x=1120, y=270)

    conf_new_pass_lable = tk.Label(window, text='Confirm Password : ', bg='white', font=(None, 15))
    conf_new_pass_lable.place(x=930, y=320)

    conf_new_pass_box = tk.Entry(window, borderwidth=2, bg='white', font=('times new roman', 14))
    conf_new_pass_box.place(x=1120, y=320)

    conf_button = tk.Button(window, text='sign on', bg='white', font=(None, 18))
    conf_button.place(x=1250, y=380)





current_user = log_page.CURRENT_USERNAME
log_page.show()

window.mainloop()

conn.close()
close_db()
