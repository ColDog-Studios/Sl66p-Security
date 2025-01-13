import unittest
from src.monitoring.port_monitor import check_open_ports

class TestPortMonitor(unittest.TestCase):

    def test_check_open_ports(self):
        # Assuming check_open_ports returns a list of open ports
        open_ports = check_open_ports('192.168.1.1')  # Replace with a test IP
        self.assertIsInstance(open_ports, list)
        # Further assertions can be added based on expected behavior

if __name__ == '__main__':
    unittest.main()