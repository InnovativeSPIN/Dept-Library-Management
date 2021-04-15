"""
Date started   : 09 Apr 2021
Authors        : MANOJ_KUMAR_S | SARAVANAN_M | HARI_PRASAD_J
"""
from frontend import *


window = tk.Tk()
window.geometry('1366x768')
window.minsize(1366, 768)
window.maxsize(1366, 768)
window.title('Library Management System')
#window.wm_overrideredirect(True)
log_page = LoginPage(window)
log_page.show()

window.mainloop()
close_db()
