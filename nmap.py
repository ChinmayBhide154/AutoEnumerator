import os


class scanner:
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
        os.system("nmap " + self.ip_address + " > text.txt")
        os.system("grep tcp text.txt > text1.txt")

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

    def enumerate_p80_p443(self):
        if scanner.find_port(self, 80):
            port_80 = scanner.find_index_of_port(self, 80)
            os.system("dirb http://" + self.ip_address + "/ >> text1.txt")

        if scanner.find_port(self, 443):
            port_443 = scanner.find_index_of_port(self, 443)
            os.system("dirb https://" + self.ip_address + "/ >> text1.txt")
