# Warning: Use with discretion and when explicitly permitted.

import ipaddress
import socket
import argparse

# Verify IP address
def is_valid_ip(ip):
    try:
        # Try to create an IPv4 or IPv6 address object
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        print('[-] Invalid IP address.')


# Argument parser to define flags
parser = argparse.ArgumentParser(description='Simple port scanner implementation in python')
# Add the arguments to parse
parser.add_argument('-d', '--destination', required=True, type=str, help='[+] The IP address of the device to port-scan.')
parser.add_argument('-dp', '--port', type=int, help='[+] Scan a specific port.')
# Parse the arguments
args = parser.parse_args()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.destination ,port))
        return True
    except ValueError:
        print('[-] Error while scanning.')


if