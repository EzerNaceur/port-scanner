# Port Scanner

A simple port scanner implementation in Python.

## Usage

```sh
python port-scan.py [-h] [-p PORT] [-pr pmin pmax] [-t THREADS] [-e] destination
```

# Description

This script allows you to scan open ports on a specified IP address. You can scan a specific port, a range of ports, and control the number of threads used for the scan. Additionally, you can save the list of open ports to a file.

## Positional Arguments

- **destination**: The IP address of the device to port-scan.

## Options

\t  -h, --help: Show the help message and exit.
  
\t  -p PORT, --port PORT: Scan a specific port.
  
\t  -pr pmin pmax, --portrange pmin pmax: Accepts a range of ports to scan (<pmin pmax>).
  
\t  -t THREADS, --threads THREADS: Specify the number of threads to be used (default=100).
  
\t  -e, --echo: Print the open ports to the open_ports.txt file.

## Examples

- Scan a Specific Port

```sh
python port-scan.py -p 80 192.168.1.1
```

- Scan a Range of Ports

```sh
python port-scan.py -pr 20 80 192.168.1.1
```

- Specify the Number of Threads

```sh
python port-scan.py -t 200 192.168.1.1
```

- Save Open Ports to a File

```sh
python port-scan.py -e 192.168.1.1
```

## Disclaimer

This script is for educational purposes only. Unauthorized use of this script to attack a system is illegal and unethical. Always obtain proper authorization before testing or attacking any system.
