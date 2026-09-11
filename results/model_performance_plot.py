import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("model_performance.csv")

for metric in ["MAE", "R2"]:
    pivot = df.pivot(
        index="Model",
        columns="Chromium Dataset",
        values=metric
    )

    ax = pivot.plot(kind="bar", figsize=(10, 6))
    ax.set_title(f"{metric} Comparison by Chromium Dataset")
    ax.set_xlabel("Machine Learning Model")
    ax.set_ylabel(metric)
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.savefig(f"{metric.lower()}_comparison.png", dpi=300)
    plt.close()
