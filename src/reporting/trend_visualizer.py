# trend_visualizer.py

import matplotlib.pyplot as plt
import numpy as np

class TrendVisualizer:
    def __init__(self):
        self.data = {}

    def add_data(self, category, value):
        if category not in self.data:
            self.data[category] = []
        self.data[category].append(value)

    def visualize_trends(self):
        plt.figure(figsize=(10, 6))
        for category, values in self.data.items():
            plt.plot(values, label=category)
        plt.title('Configuration Risk Trends')
        plt.xlabel('Time')
        plt.ylabel('Risk Level')
        plt.legend()
        plt.grid()
        plt.show()

    def save_trend(self, filename):
        plt.savefig(filename)

    def clear_data(self):
        self.data.clear()