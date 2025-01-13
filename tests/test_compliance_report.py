import unittest
from src.reporting.compliance_report import ComplianceReport

class TestComplianceReport(unittest.TestCase):

    def setUp(self):
        self.report = ComplianceReport()

    def test_generate_report(self):
        # Assuming generate_report returns a dictionary
        result = self.report.generate_report()
        self.assertIsInstance(result, dict)

    def test_compliance_gaps(self):
        # Assuming check_compliance_gaps returns a list of gaps
        gaps = self.report.check_compliance_gaps()
        self.assertIsInstance(gaps, list)

    def test_report_format(self):
        # Assuming generate_report has a specific format
        result = self.report.generate_report()
        self.assertIn('compliance_status', result)
        self.assertIn('gaps', result)

if __name__ == '__main__':
    unittest.main()