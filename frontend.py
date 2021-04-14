import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import *


class LoginPage:
    def __init__(self, window):
        self.LOGIN_BG = Image.open(r'Assets/bg3.png')
        self.LOGIN_BG = ImageTk.PhotoImage(self.LOGIN_BG)
        self.bg_s = tk.Label(window, image=self.LOGIN_BG)
        self.CURRENT_USERNAME = None
        self.window = window

        self.signin_b = tk.Button(window, text='     Sign in     ', font=('Lato', 12), borderwidth=0.5,
                                  bg='white',fg="grey", command=lambda: self.on_click_signin())
        self.new_user_b = tk.Button(window, text='New User?', font=('lato', 12), borderwidth=0.1,
                                    bg='white',fg='grey', command=lambda: self.on_click_new())
        self.forget_pass_b = tk.Button(window, text='Forget Password?', borderwidth=0.1, font=('lato', 12),
                                       bg='white',fg='grey', command=lambda: self.onclick_forget_pass())

        self.user_name_box = ttk.Combobox(window, width=23,font=('lato', 18), textvariable=str)
        self.user_name_box['values'] = get_user_names()
        self.pass_word_box = tk.Entry(window, borderwidth=2, show='*', fg="grey", font=("lato", 18))
        self.user_name_label = tk.Label(window, text='USERNAME', font=('Lato', 20), bg="white", fg = "grey")
        self.pass_word_label = tk.Label(window, text='PASSWORD', font=('mistral', 20), bg="white", fg = "grey")

        self.error_in_login = tk.Label(window, text='Check your input !', font=('lato', 12),
                                       bg='white', fg='red')

    def show(self):
        self.bg_show()
        self.signin_b.place(x=1166, y=500, height=27)
        self.new_user_b.place(x=950, y=450, height=27)
        self.forget_pass_b.place(x=1050, y=450, height=27)

        self.user_name_box.place(x=950, y=270)
        self.pass_word_box.place(x=950, y=380, width=302)
        self.user_name_label.place(x=945, y=230)
        self.pass_word_label.place(x=945, y=340)

    def bg_show(self):
        self.bg_s.place(x=-2, y=-2)

    def clear(self):
        self.signin_b.place_forget()
        self.new_user_b.place_forget()
        self.forget_pass_b.place_forget()

        self.user_name_box.place_forget()
        self.pass_word_box.place_forget()
        self.user_name_label.place_forget()
        self.pass_word_label.place_forget()
        self.bg_s.place_forget()

    def clear_bg(self):
        self.bg_s.place_forget()

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
            self.clear()
            self.clear_bg()
            self.clear_error_ms()
            FirstPage(self.window, inp_username).show()
        else:
            self.error_in_login.place(x=1120, y=220)

    def onclick_forget_pass(self):
        username = self.user_name_box.get()
        if username=="":
            self.error_in_login.place(x=1120, y=220)
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
        self.LOGIN_BG = Image.open(r'Assets/FP.png')
        self.LOGIN_BG = ImageTk.PhotoImage(self.LOGIN_BG)
        self.bg_s = tk.Label(window, image=self.LOGIN_BG)
        self.back_btn = tk.Button(window, text="  Back  ", borderwidth=0.25, bg="white", fg="dark gray",
                                  font=('lato', 12), command=lambda : self.onclick_back_button())
        self.new_user_lable = tk.Label(window, text='USERNAME', bg='white', fg="grey", font=("lato", 20))
        self.user_name_box = ttk.Combobox(window, width=25,font=('times new roman', 18), textvariable=str)
        self.user_name_box['values'] = get_user_names()
        self.new_pass_lable = tk.Label(window, text='NEW PASSWORD ', bg='white', fg="grey", font=("lato", 20))
        self.new_pass_box = tk.Entry(window, borderwidth=1, show='*', bg='white', font=('times new roman', 18), fg="grey")
        self.update_button = tk.Button(window, text=' Update ', borderwidth=0.25, bg='white', fg ="dark grey",
                                       font=('lato', 12), command=lambda: self.onclick_update())
        self.window = window
        self.error_in_login = tk.Label(window, text='Check your input !', font=('lato', 15),
                                       bg='white', fg='grey')

    def show(self):
        self.update_button.place(x=780, y=370, height=27)
        self.new_user_lable.place(x=490, y=170)
        self.new_pass_lable.place(x=490, y=270)
        self.user_name_box.place(x=530, y=220)
        self.new_pass_box.place(x=530, y=320, width=314)
        self.bg_s.place(x=-2, y=-2)
        self.back_btn.place(x=700, y=370, height=27)

    def clear_error(self):
        self.error_in_login.place_forget()

    def onclick_back_button(self):
        self.clear_error()
        self.clear()
        LoginPage(self.window).show()

    def onclick_update(self):
        username = self.user_name_box.get()
        updated_password = self.new_pass_box.get()
        if username=="" and updated_password=="":
            self.error_in_login.place(x=700, y=160)
        else:
            self.clear_error()
            update_password(username, updated_password)
            self.clear()
            LoginPage(self.window).show()

    def clear(self):
        self.back_btn.place_forget()
        self.update_button.place_forget()
        self.user_name_box.place_forget()
        self.new_pass_box.place_forget()
        self.new_user_lable.place_forget()
        self.new_pass_lable.place_forget()
        self.bg_s.place_forget()


class NewUserPage:
    def __init__(self, window):
        self.LOGIN_BG = Image.open(r'Assets/NU.png')
        self.LOGIN_BG = ImageTk.PhotoImage(self.LOGIN_BG)
        self.bg_s = tk.Label(window, image=self.LOGIN_BG)
        self.back_btn = tk.Button(window, text="   Back   ", borderwidth=0.25, bg="white", fg="dark gray",
                                  font=('lato', 12), command=lambda : self.onclick_back_button())
        self.new_user_lable = tk.Label(window, text='USERNAME ', bg='white',fg="grey", font=("lato", 20))
        self.new_user_box = tk.Entry(window, borderwidth=2, bg='white', font=('times new roman', 14))
        self.new_pass_lable = tk.Label(window, text='NEW PASSWORD ', bg='white',fg="grey", font=("lato", 20))
        self.new_pass_box = tk.Entry(window, borderwidth=2, bg='white', show='*', font=('times new roman', 14))
        self.conf_new_pass_lable = tk.Label(window, text='CONFIRM PASSWORD', bg='white',fg="grey", font=("lato", 20))
        self.conf_new_pass_box = tk.Entry(window, borderwidth=2, show='*', bg='white', font=('times new roman', 14))
        self.register_button = tk.Button(window, text=' Register ', bg='white', fg="dark gray", font=("lato", 13),
                                         borderwidth=0.25, command=lambda : self.on_click_register())
        self.window = window
        self.error_in_login = tk.Label(window, text='Check your input !', font=('lato', 15),
                                       bg='white', fg='red')

    def clear_error(self):
        try:
            self.error_in_login.place_forget()
        except:
            pass

    def onclick_back_button(self):
        self.clear_error()
        self.clear()
        LoginPage(self.window).show()

    def show(self):
        self.register_button.place(x=780, y=480, height=27)
        self.back_btn.place(x=700, y=480, height=27)
        self.new_user_box.place(x=520, y=250, width=302)
        self.new_pass_box.place(x=520, y=330, width=302)
        self.conf_new_pass_box.place(x=520, y=410, width=302)

        self.new_user_lable.place(x=460, y=200)
        self.new_pass_lable.place(x=460, y=290)
        self.conf_new_pass_lable.place(x=460, y=370)
        self.bg_s.place(x=-2, y=-2)

    def on_click_register(self):
        new_user = self.new_user_box.get()
        new_password = self.new_pass_box.get()
        if new_user=="" or new_password=="":
            self.error_in_login.place(x=700, y=180)
        else:
            create_new_user(new_user, new_password)
            self.clear()
            self.clear_error()
            LoginPage(self.window).show()

    def clear(self):
        self.register_button.place_forget()
        self.back_btn.place_forget()
        self.new_user_box.place_forget()
        self.new_pass_box.place_forget()
        self.conf_new_pass_box.place_forget()

        self.new_user_lable.place_forget()
        self.new_pass_lable.place_forget()
        self.conf_new_pass_lable.place_forget()
        self.bg_s.place_forget()


class FirstPage:
    def __init__(self, window, username):
        self.window = window
        self.curr_user = username
        self.signout_b = tk.Button(window, text='   Sign out   ', font=('Lato', 12), borderwidth=0.25,
                                  bg='white',fg="grey", command=lambda: self.on_click_signout())
        self.welcome_msg = tk.Label(window, text='Welcome {} !'.format(username), font=('Lato', 18), bg="white", fg="black")

    def show(self):
        self.signout_b.place(x=1200, y=75, height=26)
        self.welcome_msg.place(x=965, y=30)

    def clear(self):
        self.signout_b.place_forget()
        self.welcome_msg.place_forget()

    def on_click_signout(self):
        self.clear()
        LoginPage(self.window).show()
