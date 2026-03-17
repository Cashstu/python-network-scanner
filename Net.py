import socket
import ipaddress

# Help determine if the IP is online by attempting to resolve its address.
def is_active(ip):
    #attempt to resolve the IP address
    try:
        socket.gethostbyaddr(ip)
        return True
    except socket.herror:
        return False

# scan_network taken an IP range and returns a list of active IPs
def scan_network(network):
    active_ips = []
    for ip in ipaddress.IPv4Network(network):
        if is_active(str(ip)):
            active_ips.append((str(ip)))
    return active_ips

# Try to connect each port in the list for given IP Address.
# If successful, it will be added to open_ports list
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    network = input("Enter the network to scan (e.g., 192.168.1.0/24): ")
    active_ips = scan_network(network)
    print(f"Active IPs: {active_ips}")

    ports = [22, 80, 443, 8080] # Example ports to scan
    for ip in active_ips:
        print(f"Scanning {ip}...")
        open_ports = scan_ports(ip, ports)
        if open_ports:
            print(f"Open ports on {ip}: {open_ports}")
        else:
            print(f"No open ports found on {ip}")

if __name__ == "__main__":
    main()
