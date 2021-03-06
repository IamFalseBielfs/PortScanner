import socket
from IPy import IP
from termcolor import colored
color = colored

print(color("     _____           __     _____                                  ", "green"))
print(color("    |  __ \         | |    / ____|                                 ", "white"))
print(color("    | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __  ", "blue"))
print(color("    |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| ", "red"))
print(color("    | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |    ", "yellow"))
print(color("    |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|    ", "white"))  
print("\n")
print("     <<<<<----->= Port Scanner By: IAmFalseBeliefs <=----->>>>>")
print("     <<<<<----->=          Ports Made Easy         <=----->>>>>")
print("<<<<<----->= Use NMAP to find version of service running <=----->>>>>")
print("\n")

def check_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(s):
	return s.recv(1024)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.settimeout(float(speed))
		sock.connect((ipaddress, port))
		try:
			banner = get_banner(sock)
			print("[----] Port " + str(port) + " is open <-----> running " + str(banner.decode().strip("\n")))
		except:
			print("[----] Port " + str(port) + " is open <-----> No Banner Avaliable")
	except:
		pass

targets = input("[----] Enter URL or IP address to scan (Split multiple targets by coma): ")
speed = input("[----] Enter speed (suggested 0.5 for most acuracy): ")
range1 = input("[----] Please put number of begining port (ie. 80): ")
range2 = int(input("[----] Please put number of ending port (ie. 100): "))
range2 += 1

def scan(target):
	converted_ip = check_ip(target)
	print("\n " + "     <<<<<----->= Scanning " + str(target) + " <=----->>>>>")
	for port in range(int(range1), int(range2)):
		scan_port(converted_ip, port)

if "," in targets:
	for ip_add in targets.split(","):
		scan(ip_add.strip(" "))
else:
	scan(targets)