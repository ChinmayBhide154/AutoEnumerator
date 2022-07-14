import os
import subprocess
# from IPy import IP
import re
from ftplib import FTP

class Scanner:
    def __init__(self, file_name, permissions, nmap_file_name, nikto_file_name, gobuster_dir_file_name, target, gobuster_dir_wordlist, ftp_file_name):
        self.file_name = file_name
        self.permissions = permissions
        self.nmap_file_name = nmap_file_name
        self.nikto_file_name = nikto_file_name
        self.gobuster_dir_file_name = gobuster_dir_file_name
        self.target = target
        self.gobuster_dir_wordlist = gobuster_dir_wordlist
        self.ftp_file_name = ftp_file_name

    def find_port(self, port_number):
        port_list = self.get_open_ports()
        for port in port_list:
            if port_number == port:
                return True

        return False


    def find_index_of_port(self, port_number):
        port_list = self.get_open_ports()
        index = -1
        for port in port_list:
            index += 1
            if port_number == port:
                return index


    def get_open_ports(self):
        ports = []
        os.system("nmap " + self.target + " > nmap.txt")
        os.system("grep tcp nmap.txt > nmap1.txt")

        with open("nmap1.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                curr_number = ""
                for index in range(10):
                    curr_number = curr_number + stripped_line[index]

                    if stripped_line[index] == '/':
                        curr_number = curr_number[:-1]
                        ports.append(int(curr_number))
                        break

        return ports

    # Writing contents to file
    def enumerate_nmap_vulners_file_write(self):
        self.file_name = self.nmap_file_name
        self.write_to_file("nmap --script vulners -sV " + self.target)

    def enumerate_gobuster_dir_file_write(self):
        self.file_name = self.gobuster_dir_file_name
        if self.find_port(80):
                os.system("gobuster dir -u http://192.168.1.65 -w gobuster_dir_wordlist.txt > gobuster.txt")
        if self.find_port(443):
            self.write_to_file(
                "gobuster dir -u https://" + self.target + " -w " + self.gobuster_dir_wordlist)

    def enumerate_nikto_file_write(self):
        if self.find_port(80) or self.find_port(443):
            self.file_name = self.nikto_file_name
            self.write_to_file("nikto -h " + self.target)

    def enumerate_ftp(self):
        if self.find_port(21):
            ftp = FTP(self.target)
            ftp.login()

        return ftp.nlst()


    def write_to_file(self, command):
        file_ = open(self.file_name, "w")
        subprocess.Popen(command, cwd="/", stdout=file_, shell=True)
        file_.close()

    # These functions do not write to a file

    def enumerate_nmap_vulners(self):
        os.system("nmap --script vulners -sV " + self.target)

    def enumerate_gobuster_dir(self):
        if self.find_port(80):
            os.system(
                "gobuster dir -u http://" + self.target + " -w " + self.gobuster_dir_wordlist)

        if self.find_port(443):
            os.system(
                "gobuster dir -u https://" + self.target + " -w " + self.gobuster_dir_wordlist)

    def enumerate_nikto(self):
        if self.find_port(80) or self.find_port(443):
            os.system("nikto -h " + self.target)






'''
    def enumerate_nmap_vulners(self):
        self.file_name = self.nmap_file_name
        self.write_to_file("nmap --script vulners -sV " + self.target)

    def enumerate_p80_p443(self):
        if Scanner.find_port(self, 80):
            # execute gobuster dir
            self.file_name = self.gobuster_dir_file_name
            self.write_to_file("gobuster dir -u http://" + self.target + " -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

            # execute nikto
            self.file_name = self.nikto_file_name
            self.write_to_file("nikto -h " + self.target)

            self.file_name = self.nmap_file_name
            self.write_to_file("nmap --script vulners -sV " + self.target)

        if Scanner.find_port(self, 443):
            self.file_name = self.gobuster_dir_file_name
            self.write_to_file("gobuster dir -u https://" + self.target + " -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

            # execute nikto
            self.file_name = self.nikto_file_name
            self.write_to_file("nikto -h " + self.target)

    def write_to_file(self, command):
        file_ = open(self.file_name, "w")
        subprocess.Popen(command, cwd="/", stdout=file_, shell=True)
        file_.close()

'''


