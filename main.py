from Scanner import Scanner
from tkinter import *


def scan():
    print("scanning started")
    # port_list = user_scanner.get_open_ports()
    # user_scanner.enumerate_p80_p443()

def click():
    scan()

# user_scanner = Scanner(metasploitable_ip, None, None, "w", "nmap2.txt", "nikto.txt", "gobuster.txt", None)


# Tkinter Window
window = Tk()
window.title("Auto-Enumerator")
window.minsize(550, 350)
window.maxsize(550, 350)

# create textbox
target = Entry(window, width=20, bg="black", fg="white")
target.place(x=190, y=200)

# submit button:
submit = Button(window, text="Scan", width=12, height=1, command=click)
submit.place(x=210, y=250)

user_scanner = Scanner(None, "w", "nmap2.txt", "nikto.txt", "gobuster.txt", target)




window.mainloop()
