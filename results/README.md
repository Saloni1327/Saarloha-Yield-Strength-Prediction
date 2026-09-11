# Model Performance Results

This folder contains the performance results for the machine learning models used to predict steel yield strength.

## Evaluation Metrics

- **MAE:** Mean Absolute Error
- **R²:** Coefficient of Determination

The models were evaluated separately for:

- Chromium content greater than 5%
- Chromium content less than 5%

## Results

The `model_performance.csv` file contains the MAE and R² values for all evaluated models.

The Python script `model_performance_plot.py` can be used to generate comparison plots for both metrics.

## Best-Performing Models

- **Cr > 5%:** Random Forest achieved the lowest MAE of 26.57.
- **Cr < 5%:** Gradient Boosting achieved the lowest MAE of 51.34.
