import unittest
from src.hardening.policy_support import load_policy, validate_policy

class TestPolicySupport(unittest.TestCase):

    def test_load_policy_valid(self):
        policy = load_policy('config/default_policies.yaml')
        self.assertIsNotNone(policy)
        self.assertIn('rules', policy)

    def test_load_policy_invalid(self):
        with self.assertRaises(FileNotFoundError):
            load_policy('config/non_existent_policy.yaml')

    def test_validate_policy_success(self):
        policy = {
            'rules': [
                {'name': 'Disable guest account', 'enabled': True},
                {'name': 'Require strong passwords', 'enabled': True}
            ]
        }
        self.assertTrue(validate_policy(policy))

    def test_validate_policy_failure(self):
        policy = {
            'rules': [
                {'name': 'Disable guest account', 'enabled': True},
                {'name': 'Require strong passwords', 'enabled': False}
            ]
        }
        self.assertFalse(validate_policy(policy))

if __name__ == '__main__':
    unittest.main()