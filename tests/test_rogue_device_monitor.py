import unittest
from src.scanning.rogue_device_monitor import RogueDeviceMonitor

class TestRogueDeviceMonitor(unittest.TestCase):

    def setUp(self):
        self.monitor = RogueDeviceMonitor()

    def test_detect_rogue_device(self):
        # Simulate a network with a rogue device
        network_devices = ['192.168.1.1', '192.168.1.100']  # Example IPs
        rogue_device = '192.168.1.100'
        self.monitor.scan_network(network_devices)
        self.monitor.detect_rogue_device(rogue_device)
        self.assertIn(rogue_device, self.monitor.rogue_devices)

    def test_no_rogue_device(self):
        # Simulate a network without rogue devices
        network_devices = ['192.168.1.1', '192.168.1.2']
        rogue_device = '192.168.1.100'
        self.monitor.scan_network(network_devices)
        self.monitor.detect_rogue_device(rogue_device)
        self.assertNotIn(rogue_device, self.monitor.rogue_devices)

    def test_alert_on_rogue_device(self):
        # Test alerting mechanism for rogue devices
        rogue_device = '192.168.1.100'
        self.monitor.alert_on_rogue_device(rogue_device)
        self.assertTrue(self.monitor.alert_triggered)

if __name__ == '__main__':
    unittest.main()