#! /bin/python3

import sys
import socket
from datetime import datetime

#define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid number of elements.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

#just pretty ok
print("-" * 30)
print(f"scanning {target}")
print(f"Start: {(datetime.now().time().replace(microsecond=0))}")
print("-" * 30)

try:
    flag = True
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) #return an error indicator
        if result == 0:
            print("Port {} is open".format(port))
            flag = False
        s.close
    if flag:
        print("No ports are open")
    print(f"Stop: {(datetime.now().time().replace(microsecond=0))}")

except KeyboardInterrupt:
	print("\nClosing program.")
	sys.exit()
	
except socket.gaierror:
	print("\nHostname was not found.")
	sys.exit()

except socket.error:
	print("\nIt was not possible to connect to the server.")
	sys.exit()
