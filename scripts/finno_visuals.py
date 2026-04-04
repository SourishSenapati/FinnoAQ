"""
Visualization module for FINNO projects.
Handles generation of matplotlib charts for cost analysis and process optimization.
"""

import os
import matplotlib.pyplot as plt
import numpy as np


class FinnoVisualizer:
    """
    Manages the creation and saving of scientific visualizations.
    """

    def __init__(self, output_dir="visualizations"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def plot_cost_distribution(self, machine_name, diy_costs, market_prices):
        """Generates a probability density plot for Make vs Buy cost analysis."""
        plt.figure(figsize=(10, 6))

        # Convert tensors to numpy if needed
        if hasattr(diy_costs, 'cpu'):
            diy_costs = diy_costs.cpu().numpy()
        if hasattr(market_prices, 'cpu'):
            market_prices = market_prices.cpu().numpy()

        # Optimization: Sample only 100k points for plotting speed even if 100M exist
        sample_size = min(len(diy_costs), 100000)
        diy_sample = np.random.choice(diy_costs, sample_size, replace=False)
        market_sample = np.random.choice(
            market_prices, sample_size, replace=False)

        plt.hist(market_sample, bins=50, alpha=0.5,
                 label='Market Price (Buy)', color='red')
        plt.hist(diy_sample, bins=50, alpha=0.5,
                 label='Fabrication Cost (Make)', color='green')

        plt.title(
            f"Make vs Buy Analysis: {machine_name} (n={sample_size} Monte Carlo Samples)")
        plt.xlabel("Cost (INR)")
        plt.ylabel("Probability Density")
        plt.legend()
        plt.grid(True, alpha=0.3)

        filename = os.path.join(
            self.output_dir, f"{machine_name.replace(' ', '_')}_cost_analysis.png")
        plt.savefig(filename)
        plt.close()
        print(f"   [VIZ] Generated Cost Analysis Plot: {filename}")

    def plot_process_physics(self, process_name, time_axis, temp_profile, optimal_temp):
        """Generates a process control chart showing temperature vs time."""
        plt.figure(figsize=(10, 6))

        plt.plot(time_axis, temp_profile,
                 label='Process Temperature Profile', color='blue')
        plt.axhline(optimal_temp, color='green', linestyle='--',
                    label=f'Optimal Setpoint ({optimal_temp}°C)')

        plt.title(f"Thermodynamic Process Control: {process_name}")
        plt.xlabel("Time (minutes)")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.grid(True)

        filename = os.path.join(
            self.output_dir, f"{process_name.replace(' ', '_')}_thermodynamics.png")
        plt.savefig(filename)
        plt.close()
        print(f"   [VIZ] Generated Physics Plot: {filename}")

    def plot_optimization_curve(self, x_data, y_data, x_label, y_label, title, optimal_x=None):
        """Generates an optimization curve (e.g., Temp vs Cook Time)."""
        plt.figure(figsize=(10, 6))

        if hasattr(x_data, 'cpu'):
            x_data = x_data.cpu().numpy()
        if hasattr(y_data, 'cpu'):
            y_data = y_data.cpu().numpy()

        plt.plot(x_data, y_data, linewidth=2, color='purple')

        if optimal_x is not None:
            plt.axvline(optimal_x, color='orange', linestyle='--',
                        label=f'Optimal: {optimal_x:.1f}')

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True)

        filename = os.path.join(
            self.output_dir, f"{title.replace(' ', '_')}.png")
        plt.savefig(filename)
        plt.close()
        print(f"   [VIZ] Generated Optimization Plot: {filename}")
