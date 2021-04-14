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
current_user = log_page.CURRENT_USERNAME

log_page.show()


window.mainloop()

conn.close()
close_db()
