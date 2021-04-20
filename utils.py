import sqlite3
import numpy as np
import datetime

# connecting to the database
conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()


def get_user_names():
    # Return the users list from DB
    cursor.execute("SELECT username FROM Librarian")
    users = np.array(cursor.fetchall())
    return users.flatten().tolist()


def create_new_user(user_name, pass_word, namee, desig):
    # Creating the new user and adding that to DB
    cursor.execute("SELECT id FROM Librarian")
    TOTAL_LIBRARIAN = len(cursor.fetchall())
    TOTAL_LIBRARIAN += 1
    cursor.execute(
        "INSERT INTO Librarian (id, username, password, name, designation) VALUES ({}, '{}', '{}', '{}', '{}')".format(
                                                                                            TOTAL_LIBRARIAN,
                                                                                            user_name, pass_word,
                                                                                            namee, desig))
    conn.commit()


def update_password(user_name, new_password):
    # Updates the password of the user in case of forgetting the password
    cursor.execute("UPDATE Librarian SET password='{}' WHERE username='{}'".format(new_password, user_name))
    conn.commit()


def validate_user(user_name, pass_word):
    # Validates entered password to the DB password for signing in
    cursor.execute("SELECT password FROM Librarian where username='{}'".format(user_name))
    try:
        if pass_word == cursor.fetchall()[0][0]:
            return True
        else:
            return False
    except:
        return False


def add_book_2_library(book_id, title, author):
    cursor.execute("INSERT INTO book_details VALUES ('{}', '{}', '{}')".format(book_id, title, author))
    conn.commit()
    cursor.execute("SELECT titles FROM available_books")
    availe_books_title = np.array(cursor.fetchall()).flatten().tolist()
    if title in availe_books_title:
        cursor.execute(
            "UPDATE available_books SET numbers = (SELECT numbers FROM available_books where titles='{}')+1".format(
                title))
        conn.commit()
    else:
        cursor.execute("INSERT INTO available_books values ('{}', {})".format(title, 1))
        conn.commit()


def add_issued_book_to_db(roll_no, book_id, validation_day=14):
    validation_date = (datetime.date.today() + datetime.timedelta(days=validation_day)).strftime("%d/%m/%Y")
    cursor.execute("INSERT INTO books_burrowed VALUES ('{}', '{}', '{}')".format(roll_no, book_id, validation_date))
    cursor.execute("SELECT title FROM book_details WHERE book_id='{}'".format(book_id))
    burrowed_book_title = cursor.fetchall()[0][0]
    cursor.execute(
        "UPDATE available_books SET numbers = (SELECT numbers FROM available_books where titles='{}')-1".format(
            burrowed_book_title))
    conn.commit()


def add_2_report(roll_no, book_id, curr_librarian, validation_day=14):
    today_date = datetime.date.today().strftime("%d/%m/%Y")
    curr_time = datetime.datetime.now().strftime("%H:%M:%S")
    valid_date = (datetime.date.today() + datetime.timedelta(days=validation_day)).strftime("%d/%m/%Y")
    cursor.execute("SELECT title, author FROM book_details WHERE book_id='{}'".format(book_id))
    title, author = cursor.fetchall()[0]
    cursor.execute("INSERT INTO FullReport "
                   "(rollno, book_id, title_of_book, author_of_book, given_by, given_date, given_time, validate_date)"
                   "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(roll_no, book_id, title, author,
                                                                                     curr_librarian, today_date,
                                                                                     curr_time, valid_date))
    conn.commit()


def return_book(roll_no, book_id, curr_librarian):
    today_date = datetime.date.today().strftime("%d/%m/%Y")
    curr_time = datetime.datetime.now().strftime("%H:%M:%S")
    cursor.execute("SELECT title, author FROM book_details WHERE book_id='{}'".format(book_id))
    title, author = cursor.fetchall()[0]
    cursor.execute("UPDATE FullReport SET "
                   "returned_to='{}', return_date='{}', return_time='{}', is_book_returned='{}' WHERE "
                   "rollno='{}' AND book_id='{}' AND is_book_returned='{}';".format(curr_librarian,
                                                                                    today_date,
                                                                                    curr_time,
                                                                                    "yes", roll_no, book_id, "no"))
    conn.commit()
    cursor.execute("DELETE FROM books_burrowed WHERE rollno='{}' AND bookid='{}'".format(roll_no, book_id))
    cursor.execute(
        "UPDATE available_books SET numbers = (SELECT numbers FROM available_books where titles='{}')+1".format(
            title))
    conn.commit()


def add_student_2_db(roll_no, stu_name, stu_semester, stu_dept):
    cursor.execute("INSERT INTO student_details VALUES ('{}', '{}', '{}', '{}')".format(roll_no, stu_name,
                                                                                        stu_semester, stu_dept))
    conn.commit()


def close_db():
    conn.close()
