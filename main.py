from Scanner import Scanner
from tkinter import *
from DataParser import DataParser

file_manager = DataParser("gobuster.txt", "w", "nmap2.txt", "nikto.txt", "gobuster.txt")

metasploitable_ip = "192.168.1.83"
user_scanner = Scanner(metasploitable_ip, None, file_manager)
def scan():
    print("scanning started")
    #port_list = user_scanner.get_open_ports()
    user_scanner.enumerate_p80_p443()
    #user_scanner.enumerate_all()

def click():
    scan()

window = Tk()
window.title("Auto-Enumerator")
window.minsize(550, 350)
window.maxsize(550, 350)

# create textbox
ip_entry = Entry(window, width=20, bg="black", fg="white")
print(ip_entry.get())
ip_entry.place(x=190, y=200)


# submit button:
submit = Button(window, text="Scan", width=12, height=1, command=click)
submit.place(x=210, y=250)

window.mainloop()