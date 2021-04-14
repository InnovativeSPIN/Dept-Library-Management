import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *


class LoginPage:
    def __init__(self, window):
        self.LOGIN_BG = Image.open('dataBase/images/home_bg.jpg')
        self.LOGIN_BG = ImageTk.PhotoImage(self.LOGIN_BG)
        self.bg_s = tk.Label(window, image=self.LOGIN_BG)
        self.title = tk.Label(window, text='LIBRARY MANAGEMENT SYSTEM', bg='#E1751A', font=('lato', 38))
        self.CURRENT_USERNAME = None
        self.window = window

        # Initialization of buttons
        self.signin_b = tk.Button(window, text='sign in', font=('lato', 14), bg='#E1751A',
                                  fg='black', command=lambda: self.on_click_signin())
        self.new_user_b = tk.Button(window, text='New User?', font=('lato', 12), borderwidth=0.1, bg='white',
                                    fg='#E1751A', command=lambda: self.on_click_new())
        self.forget_pass_b = tk.Button(window, text='Forget Password?', borderwidth=0.1, font=('lato', 12), bg='white',
                                       fg='#E1751A', command=lambda: self.onclick_forget_pass())

        # Initialization of textBoxes
        self.user_name_box = ttk.Combobox(window, width=22, font=('times new roman', 18), textvariable=str)
        self.user_name_box['values'] = get_user_names()
        self.pass_word_box = tk.Entry(window, borderwidth=3, show='*', font=(None, 18))
        self.user_name_label = tk.Label(window, text='USERNAME', font=('lato', 20), bg='white')
        self.pass_word_label = tk.Label(window, text='PASSWORD', font=('lato', 20), bg='white')

        self.error_in_login = tk.Label(window, text='Check your password', font=('times new roman', 12),
                                       bg='red', fg='black')

    def show(self):
        self.bg_show()
        self.signin_b.place(x=728, y=390, height=27)
        self.new_user_b.place(x=380, y=394, height=27)
        self.forget_pass_b.place(x=500, y=394, height=27)

        self.user_name_box.place(x=500, y=280)
        self.pass_word_box.place(x=500, y=340, width=302)
        self.user_name_label.place(x=320, y=277)
        self.pass_word_label.place(x=320, y=337)

    def bg_show(self):
        self.bg_s.place(x=-2, y=-2)
        self.title.place(x=240, y=40)

    def clear(self):
        self.signin_b.place_forget()
        self.new_user_b.place_forget()
        self.forget_pass_b.place_forget()

        self.user_name_box.place_forget()
        self.pass_word_box.place_forget()
        self.user_name_label.place_forget()
        self.pass_word_label.place_forget()

    def clear_bg(self):
        self.bg_s.place_forget()
        self.title.place_forget()

    def clear_error_ms(self):
        try:
            self.error_in_login.place_forget()
        except Exception:
            pass

    def on_click_signin(self):
        self.clear_error_ms()
        inp_username = self.user_name_box.get()
        inp_password = self.pass_word_box.get()
        validation = validate_user(inp_username, inp_password)
        if validation:
            self.CURRENT_USERNAME = inp_username
        else:
            self.error_in_login.place(x=620, y=240)

    def onclick_forget_pass(self):
        username = self.user_name_box.get()
        if username=="":
            self.error_in_login.place(x=620, y=240)
        else:
            self.clear_error_ms()
            self.clear()
            forget_page = ForgetPassword(self.window)
            forget_page.show()

    def on_click_new(self):
        self.clear()
        self.clear_error_ms()
        new_user_page = NewUserPage(self.window)
        new_user_page.show()


class ForgetPassword:
    def __init__(self, window):
        self.new_user_lable = tk.Label(window, text='Username :', bg='white', font=(None, 15))
        self.user_name_box = ttk.Combobox(window, width=22, font=('times new roman', 18), textvariable=str)
        self.user_name_box['values'] = get_user_names()
        self.new_pass_lable = tk.Label(window, text='New Password : ', bg='white', font=(None, 15))
        self.new_pass_box = tk.Entry(window, borderwidth=2, bg='white', font=('times new roman', 14))
        self.update_button = tk.Button(window, text='Upadate', bg='white', font=(None, 18),
                                         command=lambda : self.onclick_update())
        self.window = window

        self.error_in_login = tk.Label(window, text='Check your password', font=('times new roman', 12),
                                       bg='red', fg='black')

    def show(self):
        self.update_button.place(x=728, y=390, height=27)
        self.user_name_box.place(x=500, y=280)
        self.new_pass_box.place(x=500, y=340, width=302)
        self.new_user_lable.place(x=320, y=277)
        self.new_pass_lable.place(x=320, y=337)

    def clear_error(self):
        self.error_in_login.place_forget()

    def onclick_update(self):
        username = self.user_name_box.get()
        updated_password = self.new_pass_box.get()
        if username=="" and updated_password=="":
            self.error_in_login.place(x=500, y=500)
        else:
            self.clear_error()
            update_password(username, updated_password)
            self.clear()
            LoginPage(self.window).show()

    def clear(self):
        self.update_button.place_forget()
        self.user_name_box.place_forget()
        self.new_pass_box.place_forget()
        self.new_user_lable.place_forget()
        self.new_pass_lable.place_forget()


class NewUserPage:
    def __init__(self, window):
        self.new_user_lable = tk.Label(window, text='Username :', bg='white', font=(None, 15))
        self.new_user_box = tk.Entry(window, borderwidth=2, bg='white', font=('times new roman', 14))
        self.new_pass_lable = tk.Label(window, text='New Password : ', bg='white', font=(None, 15))
        self.new_pass_box = tk.Entry(window, borderwidth=2, bg='white',show='*', font=('times new roman', 14))
        self.conf_new_pass_lable = tk.Label(window, text='Confirm Password : ', bg='white', font=(None, 15))
        self.conf_new_pass_box = tk.Entry(window, borderwidth=2,show='*', bg='white', font=('times new roman', 14))
        self.register_button = tk.Button(window, text='Register', bg='white', font=(None, 18),
                                         command=lambda : self.on_click_register(self.new_user_box, self.new_pass_box))
        self.window = window
        self.error_msg = tk.Label(window, text='Fill all', font=('times new roman', 12),
                                       bg='red', fg='black')

    def show(self):
        self.register_button.place(x=728, y=390, height=27)

        self.new_user_box.place(x=500, y=280)
        self.new_pass_box.place(x=500, y=340, width=302)
        self.conf_new_pass_box.place(x=500, y=400)

        self.new_user_lable.place(x=320, y=277)
        self.new_pass_lable.place(x=320, y=337)
        self.conf_new_pass_lable.place(x=315, y=397)

    def on_click_register(self, username_box, password_box):
        new_user = username_box.get()
        new_password = password_box.get()
        if new_password=="" or new_user=="":
            self.error_msg.place(x=430, y=200)
        else:
            create_new_user(new_user, new_password)
            self.clear()
            try:
                self.error_msg.place_forget()
            except:
                pass
            LoginPage(self.window).show()

    def clear(self):
        self.register_button.place_forget()
        self.new_user_box.place_forget()
        self.new_pass_box.place_forget()
        self.conf_new_pass_box.place_forget()

        self.new_user_lable.place_forget()
        self.new_pass_lable.place_forget()
        self.conf_new_pass_lable.place_forget()
