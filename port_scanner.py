#!/bin/python3
import sys
import socket
from datetime import datetime
import threading

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])      #Translate hostname to IPv4
else:
    print("Invalid amount of arguments\nSyntax: python3 port_scanner.py <ip>")

# Add ASCII art
print('''
  _____   ____  _____ _______    _____  _____          _   _ _   _ ______ _____   
 |  __ \ / __ \|  __ \__   __|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \  
 | |__) | |  | | |__) | | |    | (___ | |       /  \  |  \| |  \| | |__  | |__) | 
 |  ___/| |  | |  _  /  | |     \___ \| |      / /\ \ | . ` | . ` |  __| |  _  /  
 | |    | |__| | | \ \  | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \  
 |_|     \____/|_|  \_\ |_|    |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\ 
                                                                                  
                                                                                  ''')

print("Target IP:" + target)
print("\n")

# Add a pretty Banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open.")
        s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("Could not connect to the server.")
        sys.exit()

try:
    threads = []

    for port in range(1,65535):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
