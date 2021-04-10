"""
Date started   : 09 Apr 2021
Authors        : MANOJ_KUMAR_S | SARAVANAN_M | HARI_PRASAD_J
"""
import sqlite3


conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()


def create_new_user(user_name, pass_word):
    cursor.execute("SELECT id FROM Librarian")
    TOTAL_LIBRARIAN = len(cursor.fetchall())
    TOTAL_LIBRARIAN += 1
    cursor.execute("INSERT INTO Librarian (id, username, password) VALUES ({}, '{}', '{}')".format(TOTAL_LIBRARIAN, user_name, pass_word))
    conn.commit()


def update_password(user_name, new_password):
    cursor.execute("UPDATE Librarian SET password='{}' WHERE username='{}'".format(new_password, user_name))
    conn.commit()


def validate_user(user_name, pass_word):
    cursor.execute("SELECT password FROM Librarian where username='{}'".format(user_name))
    if pass_word == cursor.fetchall()[0][0]:
        return 1
    else:
        return 0
