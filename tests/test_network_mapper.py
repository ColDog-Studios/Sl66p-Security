import unittest
from src.scanning.network_mapper import scan_network

class TestNetworkMapper(unittest.TestCase):

    def test_scan_network(self):
        # Assuming scan_network returns a list of devices
        devices = scan_network()
        self.assertIsInstance(devices, list)
        # Further assertions can be added based on expected output

if __name__ == '__main__':
    unittest.main()