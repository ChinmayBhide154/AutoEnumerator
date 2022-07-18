import time
from Scanner import Scanner
from tkinter import *
from tkinter import ttk
import tkinter as tk
from threading import Thread
import os

window_width = 1000
window_height = 500

scanner = Scanner(None, "w", "nmap2.txt", "nikto.txt", "gobuster.txt", None, "gobuster_dir_wordlist.txt",
                  "ftp.txt", False, False, False, False, False)



def init_scan_choices():
    port_scan_choice = var1.get()
    vuln_scan_choice = var2.get()
    cve_scan_choice = var3.get()
    web_dir_bf_choice = var4.get()
    ftp_files_view_choice = var5.get()

    if port_scan_choice == 1:
        scanner.nmap_is_on = True

    if vuln_scan_choice == 1:
        scanner.nikto_is_on = True

    if cve_scan_choice == 1:
        if scanner.nmap_is_on:
            cve_scan_choice = True

    if web_dir_bf_choice == 1:
        if scanner.nmap_is_on:
            web_dir_bf_choice = True

    if ftp_files_view_choice == 1:
        if scanner.nmap_is_on:
            ftp_files_view_choice = True

def scan():
    init_scan_choices()

    print("scanning started")

    if scanner.ftp_is_on:
        files = scanner.enumerate_ftp()
        for file in files:
            textf6.insert(tk.INSERT, file)

    else:
        textf6.insert(tk.INSERT, "Results are unavailable because port 21 is not open")

    # open ports
    if scanner.nmap_is_on:
        port_list = scanner.get_open_ports()
        strings = [str(port) for port in port_list]
        print(strings)
        for string in strings:
            textf2.insert(tk.INSERT, string + ", ")

    else:
        textf2.insert(tk.INSERT, "Results are unavailable because port scanning is not enabled")

    # vulnerability assessment
    if scanner.nikto_is_on:
        scanner.enumerate_nikto_file_write()
        time.sleep(30)
        with open("nikto.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                textf3.insert(tk.INSERT, stripped_line + "\n")

    else:
        textf3.insert(tk.INSERT, "Results are unavailable because port scanning is not enabled")

    if scanner.gobuster_dir_is_on:
        scanner.enumerate_gobuster_dir_file_write()
        time.sleep(30)
        with open("gobuster.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                textf5.insert(tk.INSERT, stripped_line + "\n")

    else:
        textf5.insert(tk.INSERT, "Results are unavailable because port scanning is not enabled")

    if scanner.vulners_is_on:
        scanner.enumerate_nmap_vulners_file_write()
        time.sleep(30)
        with open("nmap2.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                textf4.insert(tk.INSERT, stripped_line + "\n")

    else:
        textf4.insert(tk.INSERT, "Results are unavailable because port scanning is not enabled")

    print("Scanning ended")

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
target = Entry(frame1, width=15, bg="black", fg="white")
target.place(x=window_width / 2 - 150, y=window_height / 2 - 80)

# Checkbox options
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()


c1 = tk.Checkbutton(frame1, text='Enable Port Scanning', variable=var1, onvalue=1, offvalue=0)
c1.pack()
c1.place(x=window_width / 2, y=window_height / 2 - 120)

c2 = tk.Checkbutton(frame1, text='Enable General Vulnerability Assessment', variable=var2, onvalue=1, offvalue=0)
c2.pack()
c2.place(x=window_width / 2, y=window_height / 2 - 90)

c3 = tk.Checkbutton(frame1, text='Enable CVE Findings', variable=var3, onvalue=1, offvalue=0)
c3.pack()
c3.place(x=window_width / 2, y=window_height / 2 - 60)

c4 = tk.Checkbutton(frame1, text='Enable Web Directory Brute Forcing', variable=var4, onvalue=1, offvalue=0)
c4.pack()
c4.place(x=window_width / 2, y=window_height / 2 - 30)

c5 = tk.Checkbutton(frame1, text='Enable FTP File Download', variable=var5, onvalue=1, offvalue=0)
c5.pack()
c5.place(x=window_width / 2, y=window_height / 2)


scanner.target = target.get()
print(scanner.target)

# submit button:
submit = Button(frame1, text="Scan", width=12, height=1, command=click)
submit.place(x=window_width / 2 - 150, y=window_height / 2 - 40)

window.mainloop()
