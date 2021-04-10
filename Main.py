from utils import *
import sqlite3
import tkinter as tk

conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Librarian")
print(cursor.fetchall())

