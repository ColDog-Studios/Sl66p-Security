import unittest
from src.hardening.app_hardening import harden_application, check_application_security

class TestAppHardening(unittest.TestCase):

    def test_harden_application_success(self):
        app_name = "example_app"
        result = harden_application(app_name)
        self.assertTrue(result)
    
    def test_harden_application_failure(self):
        app_name = "non_existent_app"
        result = harden_application(app_name)
        self.assertFalse(result)

    def test_check_application_security_secure(self):
        app_name = "secure_app"
        result = check_application_security(app_name)
        self.assertTrue(result)

    def test_check_application_security_insecure(self):
        app_name = "insecure_app"
        result = check_application_security(app_name)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()