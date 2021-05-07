import sqlite3
import numpy as np
import datetime

# connecting to the database
import pandas as pd

conn = sqlite3.connect("dataBase/MasterDB.db")
cursor = conn.cursor()


def get_user_names():
    # Return the users list from DB
    cursor.execute("SELECT username FROM Librarian")
    users = np.array(cursor.fetchall())
    return users.flatten().tolist()

def get_students_register_number():
    cursor.execute("SELECT rollno FROM student_details")
    book_ids = np.array(cursor.fetchall())
    return book_ids.flatten().tolist()

def get_book_id():
    cursor.execute("SELECT book_id FROM book_details")
    roll_no = np.array(cursor.fetchall())
    return roll_no.flatten().tolist()

def get_faculty_roll_no():
    cursor.execute("SELECT roll_number FROM faculty_details")
    faculty_roll_no = np.array(cursor.fetchall())
    return faculty_roll_no.flatten().tolist()

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


def add_book_2_library(book_id, type, title, author, publisher):
    cursor.execute("INSERT INTO book_details VALUES ('{}', '{}', '{}', '{}', '{}')".format(book_id, title.lower(),
                                                                                           type, author.lower(), publisher.lower()))
    conn.commit()
    cursor.execute("SELECT titles FROM available_books")
    availe_books_title = np.array(cursor.fetchall()).flatten().tolist()
    if title in availe_books_title:
        cursor.execute(
            "UPDATE available_books SET numbers = (SELECT numbers FROM available_books where titles='{}')+1 WHERE titles='{}'".format(
                title.lower(), title.lower()))
        conn.commit()
    else:
        cursor.execute("INSERT INTO available_books values ('{}', {})".format(title.lower(), 1))
        conn.commit()


def add_issued_book_to_db(role, roll_no, book_id, validation_day=14):
    validation_date = (datetime.date.today() + datetime.timedelta(days=validation_day)).strftime("%d/%m/%Y")
    cursor.execute("INSERT INTO books_burrowed VALUES ('{}', '{}', '{}', '{}')".format(role, roll_no, book_id, validation_date))
    cursor.execute("SELECT title FROM book_details WHERE book_id='{}'".format(book_id))
    burrowed_book_title = cursor.fetchall()[0][0]
    cursor.execute(
        "UPDATE available_books SET numbers = (SELECT numbers FROM available_books where titles='{}')-1 where "
        "titles='{}'".format(burrowed_book_title, burrowed_book_title))
    conn.commit()



def add_2_report(ty, roll_no, book_id, curr_librarian, validation_day=14):
    today_date = datetime.date.today().strftime("%d-%m-%Y")
    curr_time = datetime.datetime.now().strftime("%H:%M:%S")
    valid_date = (datetime.date.today() + datetime.timedelta(days=validation_day)).strftime("%d-%m-%Y")
    cursor.execute("SELECT title, author FROM book_details WHERE book_id='{}'".format(book_id))
    title, author = cursor.fetchall()[0]
    cursor.execute("INSERT INTO FullReport (type, rollno, book_id, title_of_book, Author_of_book, given_by, given_date, given_time, validate_date)"
                   "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(ty, roll_no, book_id, title, author,
                                                                                     curr_librarian, today_date,
                                                                                     curr_time, valid_date))
    conn.commit()


def return_book(ty, roll_no, book_id, curr_librarian):
    today_date = datetime.date.today().strftime("%d/%m/%Y")
    curr_time = datetime.datetime.now().strftime("%H:%M:%S")
    cursor.execute("SELECT title, author FROM book_details WHERE book_id='{}'".format(book_id))
    title, author = cursor.fetchall()[0]
    cursor.execute("UPDATE FullReport SET "
                   "returned_to='{}', return_date='{}', return_time='{}', is_book_returned='{}' WHERE "
                   "type='{}' AND rollno='{}' AND book_id='{}' AND is_book_returned='no';".format(curr_librarian,
                                                                                    today_date,
                                                                                    curr_time,
                                                                                    "yes", ty, roll_no, book_id))
    conn.commit()
    cursor.execute("DELETE FROM books_burrowed WHERE rollno='{}' AND bookid='{}'".format(roll_no, book_id))
    cursor.execute(
        "UPDATE available_books SET numbers = (SELECT numbers FROM available_books where titles='{}')+1 WHERE titles='{}'".format(
            title.lower(), title.lower()))
    conn.commit()


def add_student_2_db(roll_no, stu_name, year, stu_semester, stu_dept):
    cursor.execute("INSERT OR IGNORE INTO student_details VALUES ('{}', '{}', '{}', '{}', '{}')".format(roll_no.lower(), stu_name, year,
                                                                                              stu_semester, stu_dept))
    conn.commit()


def add_faculty_2_db(roll_no, name, designation, department):
    cursor.execute("INSERT OR IGNORE INTO faculty_details VALUES ('{}', '{}', '{}', '{}')".format(roll_no.lower(), name,
                                                                                        designation, department))
    conn.commit()

def gen_book_id_for_new_book():
    cursor.execute("SELECT book_id FROM book_details")
    xx = cursor.fetchall()
    ids = len(np.array(xx).flatten()) + 1
    return "CS" + str(ids)


def add_by_excel(filepath, types=None):
    if types!=None:
        try:
            data = pd.read_excel(filepath)
        except:
            return False
        if types=="book":
            columns = ["title", "type", "author", "publisher"]
            data = data[columns]
            book_ids = []
            for i in range(len(data)):
                row = (data.iloc[i]).values
                gen_id = gen_book_id_for_new_book()
                book_ids.append(gen_id)
                add_book_2_library(book_id=gen_id, type=row[1], title=row[0].lower(),
                                   author=row[2], publisher=row[-1])

            data["book_id"] = np.array(book_ids)
            new_path = "/".join(filepath.split("/")[:-1])
            data.to_csv(new_path+"/added_books_with_GeneratedBooks_id.csv")

        if types=="student":
            columns = ["rollno", "name", "year", "semester", "department"]
            data = data[columns]
            for i in range(len(data)):
                row = (data.iloc[i]).values
                add_student_2_db(roll_no=row[0], stu_name=row[1], year=row[2],
                                 stu_semester=row[3], stu_dept=row[4])

        if types=="faculty":
            columns=["roll_number", "name", "designation", "department"]
            data = data[columns]
            for i in range(len(data)):
                row = (data.iloc[i]).values
                add_faculty_2_db(row[0], row[1], row[2], row[3])
        return True
    else:
        return False


def get_available_book_by_title(title_substr):
    cursor.execute("SELECT titles FROM available_books WHERE numbers > 0;")
    titles = np.array(cursor.fetchall()).flatten()
    ls = []
    for title in titles:
        if title_substr.lower() in title.lower().split():
            cursor.execute("SELECT book_id, title, author, type FROM book_details where title='{}'".format(title.lower()))
            ls += np.array(cursor.fetchall()).tolist()
    return ls


def get_available_book_ids():
    cursor.execute("SELECT titles FROM available_books WHERE numbers > 0;")
    titles = np.array(cursor.fetchall()).flatten()
    ls = []
    for title in titles:
        cursor.execute("SELECT book_id FROM book_details where title='{}'".format(title.lower()))
        ls += np.array(cursor.fetchall()).flatten().tolist()
    return ls

def get_available_book_by_type(typee):
    cursor.execute("SELECT titles FROM available_books WHERE numbers > 0;")
    titles = np.array(cursor.fetchall()).flatten()
    ls = []
    for title in titles:
        cursor.execute("SELECT book_id, title, author, type FROM book_details where title='{}' AND type='{}'".format(title.lower(), typee))
        ls += np.array(cursor.fetchall()).tolist()
    return ls



def get_student_burrowed_details(reg_no):
    cursor.execute("SELECT book_id, title_of_book, given_date, validate_date FROM FullReport WHERE rollno='{}' AND is_book_returned='no' AND type='Student'".format(reg_no))
    return np.array(cursor.fetchall()).tolist()


def get_faculty_burrowed_details(roll_no):
    cursor.execute("SELECT book_id, title_of_book, given_date, validate_date FROM FullReport WHERE rollno='{}' AND is_book_returned='no' AND type='Faculty'".format(roll_no))
    return np.array(cursor.fetchall()).tolist()

def get_stu_details(roll_no):
    cursor.execute("SELECT name, year, department FROM student_details WHERE rollno='{}'".format(roll_no))
    return np.array(cursor.fetchall()).squeeze().tolist()

def get_all_roll_no():
    cursor.execute("SELECT rollno FROM student_details")
    xx = np.array(cursor.fetchall()).flatten().tolist()
    cursor.execute("SELECT roll_number FROM faculty_details")
    yy = np.array(cursor.fetchall()).flatten().tolist()
    return xx+yy


def get_faculty_details(roll_no):
    cursor.execute("SELECT name, designation, department FROM faculty_details WHERE roll_number='{}'".format(roll_no))
    return np.array(cursor.fetchall()).squeeze().tolist()

def get_burrowed_books(role, roll_no):
    cursor.execute("SELECT book_id, title_of_book FROM FullReport WHERE rollno='{}' AND is_book_returned='no' AND type='{}'".format(roll_no, role))
    return np.array(cursor.fetchall()).tolist()

def get_full_report():
    cursor.execute("SELECT type, rollno, book_id, title_of_book, given_by, given_date, given_time, validate_date, "
                   "returned_to, return_date, return_time FROM FullReport")
    return np.array(cursor.fetchall()).tolist()

def get_report_by(col_name, name, role="Student"):
    cursor.execute("SELECT type, rollno, book_id, title_of_book, given_by, given_date, given_time, validate_date, "
                   "returned_to, return_date, return_time FROM FullReport WHERE {}='{}' AND type='{}'".format(col_name, name, role))
    return np.array(cursor.fetchall()).tolist()

def get_report_by_date(role, from_date, to_date):
    cursor.execute("SELECT type, rollno, book_id, title_of_book, given_by, given_date, given_time, validate_date, "
                   "returned_to, return_date, return_time FROM FullReport WHERE  given_date >= '{}' AND given_date<='{}' AND type='{}'".format(from_date, to_date, role))
    return np.array(cursor.fetchall()).tolist()


def close_db():
    conn.close()
