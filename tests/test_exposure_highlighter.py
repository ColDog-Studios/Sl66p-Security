import unittest
from src.monitoring.exposure_highlighter import highlight_exposures

class TestExposureHighlighter(unittest.TestCase):

    def setUp(self):
        self.device_data = {
            'device1': {'status': 'active', 'config': {'insecure_setting': True}},
            'device2': {'status': 'inactive', 'config': {'insecure_setting': False}},
            'device3': {'status': 'active', 'config': {'insecure_setting': True}},
        }

    def test_highlight_exposures(self):
        exposures = highlight_exposures(self.device_data)
        expected_exposures = ['device1', 'device3']
        self.assertEqual(exposures, expected_exposures)

    def test_no_exposures(self):
        self.device_data['device1']['config']['insecure_setting'] = False
        exposures = highlight_exposures(self.device_data)
        self.assertEqual(exposures, [])

if __name__ == '__main__':
    unittest.main()