import subprocess
import os
from Scanner import Scanner

class DataParser:

    def __init__(self, file_name, permissions, nmap_file_name, nikto_file_name, gobuster_dir_file_name):
        self.file_name = file_name
        self.permissions = permissions
        self.nmap_file_name = nmap_file_name
        self.nikto_file_name = nikto_file_name
        self.gobuster_dir_file_name = gobuster_dir_file_name

    def write_to_file(self, command):
        file_ = open(self.file_name, "w")
        subprocess.Popen(command, cwd="/", stdout=file_, shell=True)
        file_.close()

    #Write to tkinter gui
    def write_to_gui(self):
        print("Written to gui")

    def get_bf_web_directories(self):
        with open(self.gobuster_dir_file_name, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line[0] == '/':
                    self.write_to_gui()

    def get_cves(self):
        with open(self.gobuster_dir_file_name, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if 'CVE' in stripped_line:
                    self.write_to_gui()

    def get_vulnerability_alerts(self):
        with open(self.nikto_file_name, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if 'CVE' in stripped_line:
                    self.write_to_gui()