import time
from Scanner import Scanner
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os

window_width = 1000
window_height = 500

scanner = Scanner(None, "w", "nmap2.txt", "nikto.txt", "gobuster.txt", None, "gobuster_dir_wordlist.txt", "ftp.txt")


def scan():
    files = scanner.enumerate_ftp()
    for file in files:
        textf6.insert(tk.INSERT, file)


    # submit.destroy()
    print("scanning started")
    #open ports
    port_list = scanner.get_open_ports()
    strings = [str(port) for port in port_list]
    print(strings)
    for string in strings:
        textf2.insert(tk.INSERT, string + ", ")

    # vuln assessment
    scanner.enumerate_nikto_file_write()
    time.sleep(30)
    with open("nikto.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            textf3.insert(tk.INSERT, stripped_line + "\n")

    scanner.enumerate_gobuster_dir_file_write()
    time.sleep(30)
    with open("gobuster.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            textf5.insert(tk.INSERT, stripped_line + "\n")

    scanner.enumerate_nmap_vulners_file_write()
    time.sleep(30)
    with open("nmap2.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            textf4.insert(tk.INSERT, stripped_line + "\n")

    print(strings)


def click():
    scanner.target = target.get()
    if scanner.target is None:
        print("Invalid")
        return
    # user_scanner.validate_IP_or_domain()
    scan()


# Tkinter Window
window = Tk()
window.title("Auto-Enumerator")
window.minsize(window_width, window_height)
window.maxsize(window_width, window_height)

# Tabs
my_notebook = ttk.Notebook(window)
my_notebook.pack(pady=15)

frame1 = Frame(my_notebook, width=window_width, height=window_height)
frame2 = Frame(my_notebook, width=window_width, height=window_height)
frame3 = Frame(my_notebook, width=window_width, height=window_height)
frame4 = Frame(my_notebook, width=window_width, height=window_height)
frame5 = Frame(my_notebook, width=window_width, height=window_height)
frame6 = Frame(my_notebook, width=window_width, height=window_height)

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)
frame6.pack(fill="both", expand=1)

my_notebook.add(frame1, text="Main")
my_notebook.add(frame2, text="Open Ports")
my_notebook.add(frame3, text="Vulnerability Analysis")
my_notebook.add(frame4, text="CVE")
my_notebook.add(frame5, text="Directory Scan")
my_notebook.add(frame6, text="FTP Files")

scroll_frame2 = Scrollbar(frame2)
scroll_frame2.pack(side=RIGHT, fill=Y)

scroll_frame3 = Scrollbar(frame3)
scroll_frame3.pack(side=RIGHT, fill=Y)

scroll_frame4 = Scrollbar(frame4)
scroll_frame4.pack(side=RIGHT, fill=Y)

scroll_frame5 = Scrollbar(frame5)
scroll_frame5.pack(side=RIGHT, fill=Y)

scroll_frame6 = Scrollbar(frame6)
scroll_frame6.pack(side=RIGHT, fill=Y)


text_frame2 = Text(frame2, width=window_width, height=window_height, Wrap=None, yscrollcommand=scroll_frame2.set)
text_frame3 = Text(frame3, width=window_width, height=window_height, Wrap=None, yscrollcommand=scroll_frame3.set)
text_frame4 = Text(frame4, width=window_width, height=window_height, Wrap=None, yscrollcommand=scroll_frame4.set)
text_frame5 = Text(frame5, width=window_width, height=window_height, Wrap=None, yscrollcommand=scroll_frame5.set)
text_frame6 = Text(frame6, width=window_width, height=window_height, Wrap=None, yscrollcommand=scroll_frame6.set)


textf2 = tk.Text(frame2, width=window_width, height=window_height)
textf2.insert(tk.INSERT, "")
textf2.pack()

textf3 = tk.Text(frame3, width=window_width, height=window_height)
textf3.insert(tk.INSERT, "")
textf3.pack()

textf4 = tk.Text(frame4, width=window_width, height=window_height)
textf4.insert(tk.INSERT, "")
textf4.pack()

textf5 = tk.Text(frame5, width=window_width, height=window_height)
textf5.insert(tk.INSERT, "")
textf5.pack()

textf6 = tk.Text(frame6, width=window_width, height=window_height)
textf6.insert(tk.INSERT, "")
textf6.pack()

# create textbox
target = Entry(frame1, width=20, bg="black", fg="white")
target.place(x=190, y=200)

scanner.target = target.get()
print(scanner.target)

# submit button:
submit = Button(frame1, text="Scan", width=12, height=1, command=click)
submit.place(x=210, y=250)

window.mainloop()
