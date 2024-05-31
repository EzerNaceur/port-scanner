# Warning: Use with discretion and when explicitly permitted.
import ipaddress
import socket
import argparse
import threading
from queue import Queue

# Initial object definition
ports = Queue()
open_ports = []
thread_list = []


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
parser.add_argument('destination', type=str, help='[+] The IP address of the device to port-scan.')
parser.add_argument('-p', '--port', type=int, help='[+] Scan a specific port.')
parser.add_argument('-pr', '--portrange', type=int, nargs=2, metavar=('pmin', 'pmax'),help='[+] Accepts a <pmin pmax> of a specific port range.')
parser.add_argument('-t', '--threads', type=int, default=100,  help='[+] Specify the number of threads to be used(default=100).')
parser.add_argument('-e', '--echo', action='store_true', help='[+] Print the open port to the open_ports.txt file.')
# Parse the arguments
args = parser.parse_args()
target = args.destination
port = args.port
port_range = args.portrange
threads = args.threads
echo = args.echo


def scan_port(pt):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, pt))
        return True
    except:
        return False


def fill_queue(port_list):
    for p in port_list:
        ports.put(p)


def worker():
    while not ports.empty():
        cport = ports.get()
        if scan_port(cport):
            print(f"[+] Port {cport} is open.")
            open_ports.append(cport)


if port_range:
    listp = range(port_range[0], port_range[1])
    fill_queue(listp)
elif port:
    fill_queue(port)
else:
    listp = range(1, 1024)
    fill_queue(listp)

for t in range(threads):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

if len(open_ports) == 0:
    print("No open ports detected.")
else:
    if echo:
        with open('open_ports.txt', 'w') as file:
            for oprt in open_ports:
                file.write(oprt)


