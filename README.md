# Port-scanner Description
This is a simple Python script for scanning ports on a target machine. It uses the socket library to check for open ports within a specified range.

## Usage

Ensure you have Python 3 installed. Run the script from the command line with the target IP address as the argument.

## Example
python3 port_scanner.py (example.com or ip address)

## Features
Scans for open ports on a target machine.
Displays a timestamp for when the scan was started.
Provides information on open ports.

## How It Works
The script takes the target IP address as a command-line argument, translates the hostname to its IPv4 address, and then proceeds to scan ports within a specified range (whatever you replace in the 21st line in the code). For each port, it attempts to establish a TCP connection. If successful, it prints a message indicating that the port is open.

## Disclaimer
This tool is intended for educational purposes (ethical hacking) and should only be used on systems that you have explicit permission to scan.

## Author
Kartik Sharda