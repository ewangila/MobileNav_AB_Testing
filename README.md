# Mobile App Navigation A/B/n Test Analysis

Statistical analysis evaluating four mobile navigation layouts to find the fastest design for users starting a workout.

## Business Objective
The UX team designed four different navigation layouts. The goal is to **minimize the time-to-start** for users initiating a new workout and identify the optimal layout for the next production release.

## Designs Tested
| Design        | Description                          | Simulated Mean Time |
|---------------|--------------------------------------|---------------------|
| Traditional   | Classic top navigation               | ~16.0 s             |
| TabBar        | Bottom tab bar                       | ~12.5 s             |
| Hamburger     | Hamburger menu                       | ~19.5 s             |
| Gesture       | Gesture-based navigation             | ~16.5 s             |

**Sample size:** 1,000 users (250 per design)

## Methods
1. **Data Simulation** – Generate a realistic synthetic dataset based on preliminary UX testing distributions
2. **Exploratory Data Analysis** – Violin plots to visualize distributions, medians, and density
3. **One-way ANOVA** – Test for overall statistical significance across the four designs
4. **Effect Size (Eta-squared)** – Measure the practical magnitude of the design impact
5. **Tukey HSD Post-hoc Test** – Identify which specific designs differ from each other

## Key Results
- ANOVA shows a **statistically significant** difference between navigation designs
- **TabBar** consistently produces the lowest time-to-start
- Effect size (Eta-squared) indicates a **large practical impact**
- Tukey HSD confirms TabBar significantly outperforms the other three designs

**Recommendation:** Ship the **TabBar** navigation layout.

## Project Structure
```
├── app_analysis.ipynb      # Full analysis notebook (recommended starting point)
├── app_analysis.py         # Same analysis as a plain Python script
├── requirements.txt
├── .gitignore
└── LICENSE
```
## Requirements

- Python 3.8+
- numpy, pandas, seaborn, matplotlib, scipy, statsmodels
- jupyter / ipykernel (for the notebook)

## License

This project is licensed under the [MIT License](LICENSE).
