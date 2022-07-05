import os
import subprocess
from IPy import IP
import re

class Scanner:
    def __init__(self, file_name, permissions, nmap_file_name, nikto_file_name, gobuster_dir_file_name, target):
        self.file_name = file_name
        self.permissions = permissions
        self.nmap_file_name = nmap_file_name
        self.nikto_file_name = nikto_file_name
        self.gobuster_dir_file_name = gobuster_dir_file_name
        self.target = target

    def validate_IP_or_domain(self):
        response = self.ping_target()
        if response != 0:
            if self.is_IP() or self.is_domain():
                return "The target " + self.target + "is not up."
            else:
                return "The target " + self.target + "you specified is not valid syntactically. Please double check " \
                                                     "that the domain or ip address was entered correctly "

        else:
            return "Starting the scan"

    def ping_target(self):
        response = os.system("ping -c 1 " + self.target)
        return response

    def is_IP(self):
        try:
            IP(self.target)
            self.is_domain()
        except ValueError:
            return False
        return True

    def is_domain(self):
        # from https://www.geeksforgeeks.org/how-to-validate-a-domain-name-using-regular-expression/
        regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
        p = re.compile(regex)
        if self.target is None:
            return False
        if re.search(p, str):
            return True
        else:
            return False

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

    def enumerate_nmap_vulners(self):
        file_nmap = open(self.nmap_file_name, self.permissions)
        command = "nmap --script vulners -sV " + self.ip_address
        subprocess.Popen(command, stdout=file_nmap, shell=True)
        file_nmap.close()

    def enumerate_p80_p443(self):
        if Scanner.find_port(self, 80):
            # execute gobuster dir
            self.file_name = self.gobuster_dir_file_name
            self.write_to_file("gobuster dir -u http://" + self.target + " -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

            # execute nikto
            self.file_name = self.nikto_file_name
            self.write_to_file("nikto -h " + self.target)

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


