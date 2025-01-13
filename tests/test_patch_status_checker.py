import unittest
from src.monitoring.patch_status_checker import check_patch_status

class TestPatchStatusChecker(unittest.TestCase):

    def test_check_patch_status_success(self):
        # Mock a device with up-to-date patches
        device = {'name': 'Device1', 'patch_status': 'up-to-date'}
        result = check_patch_status(device)
        self.assertTrue(result['status'])
        self.assertEqual(result['message'], 'All patches are up to date.')

    def test_check_patch_status_failure(self):
        # Mock a device with out-of-date patches
        device = {'name': 'Device2', 'patch_status': 'out-of-date'}
        result = check_patch_status(device)
        self.assertFalse(result['status'])
        self.assertEqual(result['message'], 'Patches are out of date.')

    def test_check_patch_status_invalid_device(self):
        # Mock an invalid device
        device = None
        result = check_patch_status(device)
        self.assertFalse(result['status'])
        self.assertEqual(result['message'], 'Invalid device.')

if __name__ == '__main__':
    unittest.main()