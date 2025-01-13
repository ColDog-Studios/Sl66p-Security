import unittest
from src.api.cli import main

class TestCLI(unittest.TestCase):

    def test_cli_help(self):
        """Test if the CLI help command works."""
        result = main(['--help'])
        self.assertIn('usage:', result)

    def test_cli_version(self):
        """Test if the CLI version command works."""
        result = main(['--version'])
        self.assertIn('Sleep Security', result)

    def test_cli_invalid_command(self):
        """Test if the CLI handles invalid commands gracefully."""
        result = main(['invalid_command'])
        self.assertIn('Error:', result)

if __name__ == '__main__':
    unittest.main()