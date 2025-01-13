import unittest
from src.hardening.os_hardening import apply_os_hardening, check_hardening_status

class TestOSHardening(unittest.TestCase):

    def test_apply_os_hardening(self):
        result = apply_os_hardening()
        self.assertTrue(result, "OS hardening should be applied successfully.")

    def test_check_hardening_status(self):
        status = check_hardening_status()
        self.assertIsInstance(status, dict, "Status should be a dictionary.")
        self.assertIn('hardened', status, "Status should contain 'hardened' key.")
        self.assertIn('issues', status, "Status should contain 'issues' key.")

if __name__ == '__main__':
    unittest.main()