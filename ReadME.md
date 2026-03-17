# Python Network Scanner

A lightweight command-line network scanning tool built in Python that identifies active hosts and open ports on a given network range.

## Features

- Scans a specified IPv4 network range for active hosts
- Checks common ports for open connections on discovered hosts
- Clean modular design with separated network and port scanning functions
- Input validation and configurable timeout handling

## Usage

Run the script from the terminal:
```bash
python Net.py
```

When prompted, enter a network range in CIDR notation:
```
Enter the network to scan (e.g., 192.168.1.0/24):
```

The scanner will output active hosts and any open ports found.

## Default Ports Scanned

- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)
- 8080 (HTTP Alternate)

## Requirements

- Python 3.x
- No external dependencies — uses built-in `socket` and `ipaddress` modules

## What I Learned

Built this project to deepen my understanding of how network scanning tools work at the socket level. Focused on modular design, input handling, and understanding TCP connection behavior across a range of hosts and ports.