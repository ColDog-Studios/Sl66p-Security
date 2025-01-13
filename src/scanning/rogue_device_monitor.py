# Contents of /SleepSecurity/SleepSecurity/src/scanning/rogue_device_monitor.py

import socket
import threading
import time

class RogueDeviceMonitor:
    def __init__(self, network_range):
        self.network_range = network_range
        self.rogue_devices = set()
        self.lock = threading.Lock()

    def scan_network(self):
        for ip in self.network_range:
            threading.Thread(target=self.check_device, args=(ip,)).start()

    def check_device(self, ip):
        try:
            socket.gethostbyaddr(ip)
        except socket.herror:
            with self.lock:
                self.rogue_devices.add(ip)

    def alert_rogue_devices(self):
        while True:
            time.sleep(60)  # Check every minute
            if self.rogue_devices:
                self.send_alert()

    def send_alert(self):
        print("Alert! Rogue devices detected:")
        for device in self.rogue_devices:
            print(f" - {device}")

    def start_monitoring(self):
        self.scan_network()
        self.alert_rogue_devices()

# Example usage
if __name__ == "__main__":
    network_range = ["192.168.1." + str(i) for i in range(1, 255)]
    monitor = RogueDeviceMonitor(network_range)
    monitor.start_monitoring()