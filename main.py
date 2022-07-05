from Scanner import Scanner
from tkinter import *

user_scanner = Scanner(None, "w", "nmap2.txt", "nikto.txt", "gobuster.txt", None)

def scan():
    print("scanning started")
    port_list = user_scanner.get_open_ports()
    print(port_list)
    user_scanner.enumerate_p80_p443()
    exit()

def click():
    user_scanner.target = target.get()
    if user_scanner.target is None:
        print("Invalid")
        return
    # user_scanner.validate_IP_or_domain()
    scan()


# Tkinter Window
window = Tk()
window.title("Auto-Enumerator")
window.minsize(550, 350)
window.maxsize(550, 350)

# create textbox
target = Entry(window, width=20, bg="black", fg="white")
target.place(x=190, y=200)

user_scanner.target = target.get()
print(user_scanner.target)

# submit button:
submit = Button(window, text="Scan", width=12, height=1, command=click)
submit.place(x=210, y=250)


window.mainloop()
