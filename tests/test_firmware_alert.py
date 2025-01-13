import unittest
from src.monitoring.firmware_alert import check_firmware_status, alert_outdated_firmware

class TestFirmwareAlert(unittest.TestCase):

    def setUp(self):
        self.device = {
            'name': 'Device1',
            'firmware_version': '1.0.0',
            'latest_firmware_version': '1.0.1'
        }

    def test_check_firmware_status_outdated(self):
        result = check_firmware_status(self.device)
        self.assertTrue(result['outdated'])

    def test_check_firmware_status_up_to_date(self):
        self.device['firmware_version'] = '1.0.1'
        result = check_firmware_status(self.device)
        self.assertFalse(result['outdated'])

    def test_alert_outdated_firmware(self):
        with self.assertLogs('firmware_alert', level='warning') as log:
            alert_outdated_firmware(self.device)
            self.assertIn('WARNING:firmware_alert:Device1 has outdated firmware: 1.0.0', log.output)

if __name__ == '__main__':
    unittest.main()