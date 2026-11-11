#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

# Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip-address>")
    sys.exit()

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan common ports (Ports 1 to 1024)
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Returns 0 if the port is open
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()