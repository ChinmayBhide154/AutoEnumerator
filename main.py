from nmap import scanner

user_scanner = scanner("192.168.1.78", None)

port_list = user_scanner.get_open_ports()
user_scanner.enumerate_p80_p443()
