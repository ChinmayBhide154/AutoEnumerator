import os
import subprocess
from DataParser import DataParser


class Scanner(DataParser):

    def __init__(self, ip_address, hostname, data_parser):
        self.ip_address = ip_address
        self.hostname = hostname
        self.file_name = data_parser.file_name
        self.permissions = data_parser.permissions
        self.nmap_file_name = data_parser.nmap_file_name
        self.nikto_file_name = data_parser.nikto_file_name
        self.gobuster_dir_file_name = data_parser.gobuster_dir_file_name

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
        os.system("nmap " + self.ip_address + " > nmap.txt")
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
    def enumerate_all(self):
        file_nmap = open("nmap2.txt", "w")
        command = "nmap --script vulners -sV " + self.ip_address
        subprocess.Popen(command, stdout=file_nmap, shell=True)
        file_nmap.close()

    def enumerate_p80_p443(self):
        if Scanner.find_port(self, 80):
            # execute gobuster dir
            self.file_name = self.gobuster_dir_file_name
            self.write_to_file("gobuster dir -u http://" + self.ip_address + " -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

            # execute nikto
            self.file_name = self.nikto_file_name
            self.write_to_file("nikto -h " + self.ip_address)

        if Scanner.find_port(self, 443):
            self.file_name = self.gobuster_dir_file_name
            self.write_to_file("gobuster dir -u https://" + self.ip_address + " -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

            # execute nikto
            self.file_name = self.nikto_file_name
            self.write_to_file("nikto -h " + self.ip_address)


