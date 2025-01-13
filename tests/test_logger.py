import unittest
from src.utils.logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def test_logging_info(self):
        with self.assertLogs('SleepSecurity', level='INFO') as log:
            self.logger.info('Test info message')
            self.assertIn('Test info message', log.output[0])

    def test_logging_warning(self):
        with self.assertLogs('SleepSecurity', level='WARNING') as log:
            self.logger.warning('Test warning message')
            self.assertIn('Test warning message', log.output[0])

    def test_logging_error(self):
        with self.assertLogs('SleepSecurity', level='ERROR') as log:
            self.logger.error('Test error message')
            self.assertIn('Test error message', log.output[0])

    def test_logging_critical(self):
        with self.assertLogs('SleepSecurity', level='CRITICAL') as log:
            self.logger.critical('Test critical message')
            self.assertIn('Test critical message', log.output[0])

if __name__ == '__main__':
    unittest.main()