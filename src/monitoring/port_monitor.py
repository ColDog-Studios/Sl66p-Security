# Contents of /SleepSecurity/SleepSecurity/src/monitoring/port_monitor.py

import socket
import logging

class PortMonitor:
    def __init__(self, ip_range):
        self.ip_range = ip_range
        self.open_ports = {}

    def scan_ports(self, ip, ports):
        open_ports = []
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        return open_ports

    def monitor(self):
        for ip in self.ip_range:
            ports = range(1, 1025)  # Scanning the first 1024 ports
            open_ports = self.scan_ports(ip, ports)
            if open_ports:
                self.open_ports[ip] = open_ports
                logging.info(f"Open ports on {ip}: {open_ports}")

    def get_open_ports(self):
        return self.open_ports

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ip_range = ["192.168.1.1", "192.168.1.2"]  # Example IPs
    port_monitor = PortMonitor(ip_range)
    port_monitor.monitor()
    print(port_monitor.get_open_ports())