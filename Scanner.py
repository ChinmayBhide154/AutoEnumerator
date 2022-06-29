import os
import subprocess

class Scanner:

    def __init__(self, ip_address, hostname):
        self.ip_address = ip_address
        self.hostname = hostname

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

        with open("text1.txt", "r") as file:
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
            # execute dirb and save in dirb.txt
            file_dirb = open("gobuster.txt", "w")
            command = "gobuster dir -u http://" + self.ip_address + " -w usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
            subprocess.Popen(command, cwd="/", stdout=file_dirb, shell=True)
            file_dirb.close()


            # execute nikto and save to nikto.txt
            file_nikto = open("nikto.txt", "w")
            command = "nikto -h " + self.ip_address
            subprocess.Popen(command, stdout=file_nikto, shell=True)
            file_nikto.close()

        if Scanner.find_port(self, 443):
            # execute dirb and save in dirb.txt
            # file_dirb = open("dirb.txt", "w")
            # command = "dirb https://" + self.ip_address + "/"
            # subprocess.Popen(command, stdout=file_dirb, shell=True)
            # file_dirb.close()

            # execute nikto and save to nikto.txt
            file_nikto = open("nikto.txt", "w")
            command = "nikto -h " + self.ip_address
            subprocess.Popen(command, stdout=file_nikto, shell=True)
            file_nikto.close()