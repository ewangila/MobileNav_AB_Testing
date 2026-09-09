import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

class NavigationUXTest:
    def __init__(self, sample_size_per_group=250):
        self.sample_size = sample_size_per_group
        self.df = self._generate_synthetic_data()

    def _generate_synthetic_data(self):
        """Generates a realistic, noisy dataset and returns a tidy DataFrame."""
        np.random.seed(42)
        
        # Simulating realistic normal distributions for task completion times
        data = {
            'Traditional': np.random.normal(loc=16.0, scale=2.5, size=self.sample_size),
            'TabBar': np.random.normal(loc=12.5, scale=1.8, size=self.sample_size),
            'Hamburger': np.random.normal(loc=19.5, scale=3.0, size=self.sample_size),
            'Gesture': np.random.normal(loc=16.5, scale=2.8, size=self.sample_size)
        }
        
        # Convert to a tidy DataFrame structure (ideal for analytics)
        df = pd.DataFrame(data).melt(var_name='Design', value_name='Time_Seconds')
        df['Time_Seconds'] = df['Time_Seconds'].clip(lower=3.0) # Prevent impossible negative times
        return df

    def run_analysis(self):
        """Runs ANOVA, calculates effect size, and performs Tukey HSD."""
        groups = [group['Time_Seconds'].values for _, group in self.df.groupby('Design')]
        f_stat, p_val = stats.f_oneway(*groups)
        
        # Calculate Eta-squared (Effect Size) to see business impact
        ss_between = sum(len(g) * (np.mean(g) - self.df['Time_Seconds'].mean())**2 for g in groups)
        ss_total = sum((self.df['Time_Seconds'] - self.df['Time_Seconds'].mean())**2)
        eta_squared = ss_between / ss_total

        print("A/B/n Test Results")
        print(f"ANOVA F-statistic: {f_stat:.2f}")
        print(f"p-value: {p_val:.4e}")
        print(f"Effect Size (Eta-squared): {eta_squared:.3f} (Values > 0.14 indicate a large effect)\n")

        if p_val < 0.05:
            print("Conclusion: Significant differences found. Running Tukey HSD post-hoc test...\n")
            tukey = pairwise_tukeyhsd(endog=self.df['Time_Seconds'], groups=self.df['Design'], alpha=0.05)
            print(tukey)
        
        return tukey

    def plot_results(self):
        """Generates a professional Violin Plot to show distribution and density."""
        plt.figure(figsize=(10, 6))
        sns.violinplot(x='Design', y='Time_Seconds', data=self.df, palette='viridis', inner="quartile", hue='Design', legend=False)
        plt.title('Time to Start Workout by Navigation Layout (n=1000)', fontsize=14, pad=15)
        plt.ylabel('Time to Start Workout (seconds)')
        plt.xlabel('Navigation Design')
        sns.despine() # Clean up the chart borders
        plt.tight_layout()
        plt.show()

# Execution
if __name__ == "__main__":
    ux_test = NavigationUXTest(sample_size_per_group=250)
    ux_test.plot_results()
    ux_test.run_analysis()