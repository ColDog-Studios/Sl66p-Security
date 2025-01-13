# network_mapper.py

import socket
import nmap

def scan_network(network_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-sn')
    return nm.all_hosts()

def get_device_info(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = None
    return {
        'ip': ip,
        'hostname': hostname
    }

def map_network_devices(network_range):
    devices = []
    hosts = scan_network(network_range)
    for host in hosts:
        device_info = get_device_info(host)
        devices.append(device_info)
    return devices

def main():
    network_range = '192.168.1.0/24'  # Example network range
    devices = map_network_devices(network_range)
    for device in devices:
        print(f"IP: {device['ip']}, Hostname: {device['hostname']}")

if __name__ == "__main__":
    main()