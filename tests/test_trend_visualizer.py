import unittest
from src.reporting.trend_visualizer import TrendVisualizer

class TestTrendVisualizer(unittest.TestCase):

    def setUp(self):
        self.visualizer = TrendVisualizer()

    def test_initialize(self):
        self.assertIsNotNone(self.visualizer)

    def test_add_data(self):
        self.visualizer.add_data('2023-01-01', {'risk': 5})
        self.assertIn('2023-01-01', self.visualizer.data)

    def test_visualize_trends(self):
        self.visualizer.add_data('2023-01-01', {'risk': 5})
        self.visualizer.add_data('2023-01-02', {'risk': 3})
        trends = self.visualizer.visualize_trends()
        self.assertIn('2023-01-01', trends)
        self.assertIn('2023-01-02', trends)

    def test_highlight_risks(self):
        self.visualizer.add_data('2023-01-01', {'risk': 8})
        highlighted = self.visualizer.highlight_risks()
        self.assertTrue(highlighted)

if __name__ == '__main__':
    unittest.main()