"""
Date started   : 09 Apr 2021
Authors        : MANOJ_KUMAR_S | SARAVANA_M | HARI_PRASAD_J
"""
import sqlite3


conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()


class LibraryStaff:
    TOTAL_LIBRARIAN = 0

    def __init__(self, user_name, pass_word):
        self.user_name = user_name
        self.pass_word = pass_word
        LibraryStaff.TOTAL_LIBRARIAN += 1
        cursor.execute("INSERT INTO Librarian (id, username, password) VALUES ({}, '{}', '{}')".format(LibraryStaff.TOTAL_LIBRARIAN, self.user_name, self.pass_word))
        conn.commit()


def create_new_user(user_name, pass_word):
    LibraryStaff(user_name, pass_word)


def update_password(user_name, new_password):
    cursor.execute("UPDATE Librarian SET password='{}' WHERE username='{}'".format(new_password, user_name))
    conn.commit()


def validate_user(user_name, pass_word):
    cursor.execute("SELECT password FROM Librarian where username='{}'".format(user_name))
    if pass_word == cursor.fetchall()[0][0]:
        return 1
    else:
        return 0
