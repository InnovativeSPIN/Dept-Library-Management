"""
Date started   : 09 Apr 2021
Authors        : MANOJ_KUMAR_S | SARAVANAN_M | HARI_PRASAD_J
"""
import sqlite3
import numpy as np


conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()


def get_user_names():
    cursor.execute("SELECT username FROM Librarian")
    users = np.array(cursor.fetchall())
    return users.flatten().tolist()


def create_new_user(user_name, pass_word):
    cursor.execute("SELECT id FROM Librarian")
    TOTAL_LIBRARIAN = len(cursor.fetchall())
    TOTAL_LIBRARIAN += 1
    cursor.execute(
        "INSERT INTO Librarian (id, username, password) VALUES ({}, '{}', '{}')".format(TOTAL_LIBRARIAN,
                                                                                        user_name, pass_word))
    conn.commit()


def update_password(user_name, new_password):
    cursor.execute("UPDATE Librarian SET password='{}' WHERE username='{}'".format(new_password, user_name))
    conn.commit()


def validate_user(user_name, pass_word):
    cursor.execute("SELECT password FROM Librarian where username='{}'".format(user_name))
    try:
        if pass_word == cursor.fetchall()[0][0]:
            return True
        else:
            return False
    except:
        return False


def close_db():
    conn.close()
