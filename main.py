from Scanner import Scanner
from tkinter import *
from tkinter import ttk

window_width = 1000
window_height = 500

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

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)

my_notebook.add(frame1, text="Main")
my_notebook.add(frame2, text="Open Ports")
my_notebook.add(frame3, text="Vulnerability Analysis")
my_notebook.add(frame4, text="CVE")
my_notebook.add(frame5, text="Directory Scan")

# create textbox
target = Entry(frame1, width=20, bg="black", fg="white")
target.place(x=190, y=200)

user_scanner.target = target.get()
print(user_scanner.target)

# submit button:
submit = Button(frame1, text="Scan", width=12, height=1, command=click)
submit.place(x=210, y=250)




window.mainloop()
