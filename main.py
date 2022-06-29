from Scanner import Scanner
from tkinter import *
from DataParser import DataParser

file_manager = DataParser(None, None, "nmap2.txt", "nikto.txt", "gobuster.txt")

metasploitable_ip = "192.168.1.83"

def scan():
    print("scanning started")
    user_scanner = Scanner(metasploitable_ip, None)
    port_list = user_scanner.get_open_ports()
    user_scanner.enumerate_p80_p443()
    user_scanner.enumerate_all()

def click():
    # scan()
    print("Hello")

window = Tk()
window.title("Auto-Enumerator")
window.minsize(550, 350)
window.maxsize(550, 350)

# create label


# submit button:
submit = Button(window, text="Scan", width=10, height=5, command=click)
submit.place(x=100, y=100)

window.mainloop()