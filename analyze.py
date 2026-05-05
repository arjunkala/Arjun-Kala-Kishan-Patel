#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

INPUT = "data/processed/merged_crime_unemployment.csv"
RESULTS_DIR = "results"
FIGURES_DIR = "results/figures"

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

df = pd.read_csv(INPUT)

key_cols = [
    "violent_crime_rate",
    "property_crime_rate",
    "Unemployment_rate",
    "population"
]

desc = df[key_cols].describe().round(3)
desc.to_csv(f"{RESULTS_DIR}/descriptive_statistics.csv")

print("\nDescriptive statistics:")
print(desc)


correlation_pairs = [
    ("Unemployment_rate", "violent_crime_rate"),
    ("Unemployment_rate", "property_crime_rate"),
    ("violent_crime_rate", "property_crime_rate")
]

corr_results = []

for x, y in correlation_pairs:
    r, p = stats.pearsonr(df[x], df[y])
    corr_results.append({
        "variable_1": x,
        "variable_2": y,
        "pearson_r": round(r, 4),
        "p_value": round(p, 6)
    })

corr_df = pd.DataFrame(corr_results)
corr_df.to_csv(f"{RESULTS_DIR}/correlation_results.csv", index=False)

print("\nCorrelation results:")
print(corr_df)


def run_regression(outcome):
    X = df[["Unemployment_rate", "population"]].copy()
    X["population"] = X["population"].apply(lambda x: pd.NA if x <= 0 else x)
    X["log_population"] = X["population"].apply(lambda x: None if pd.isna(x) else __import__("math").log(x))

    X = X[["Unemployment_rate", "log_population"]]
    X = sm.add_constant(X)

    y = df[outcome]

    model = sm.OLS(y, X, missing="drop").fit()

    results = pd.DataFrame({
        "term": model.params.index,
        "coefficient": model.params.values,
        "p_value": model.pvalues.values
    })

    results["outcome"] = outcome
    results["r_squared"] = model.rsquared

    return results.round(5)

violent_model = run_regression("violent_crime_rate")
property_model = run_regression("property_crime_rate")

regression_results = pd.concat([violent_model, property_model], ignore_index=True)
regression_results.to_csv(f"{RESULTS_DIR}/regression_results.csv", index=False)

print("\nRegression results:")
print(regression_results)


# Figure 1: Unemployment vs violent crime
plt.figure(figsize=(8, 5))
plt.scatter(df["Unemployment_rate"], df["violent_crime_rate"], alpha=0.4)

slope, intercept, r, p, se = stats.linregress(
    df["Unemployment_rate"],
    df["violent_crime_rate"]
)

x_vals = sorted(df["Unemployment_rate"])
y_vals = [slope * x + intercept for x in x_vals]

plt.plot(x_vals, y_vals)
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Violent Crime Rate per 100,000")
plt.title("Unemployment Rate vs. Violent Crime Rate, 2000–2019")
plt.tight_layout()
plt.savefig(f"{FIGURES_DIR}/violent_crime_scatter.png", dpi=150)
plt.close()


# Figure 2: Unemployment vs property crime
plt.figure(figsize=(8, 5))
plt.scatter(df["Unemployment_rate"], df["property_crime_rate"], alpha=0.4)

slope, intercept, r, p, se = stats.linregress(
    df["Unemployment_rate"],
    df["property_crime_rate"]
)

x_vals = sorted(df["Unemployment_rate"])
y_vals = [slope * x + intercept for x in x_vals]

plt.plot(x_vals, y_vals)
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Property Crime Rate per 100,000")
plt.title("Unemployment Rate vs. Property Crime Rate, 2000–2019")
plt.tight_layout()
plt.savefig(f"{FIGURES_DIR}/property_crime_scatter.png", dpi=150)
plt.close()


# Figure 3: Average trends over time
yearly = df.groupby("Year").agg({
    "violent_crime_rate": "mean",
    "property_crime_rate": "mean",
    "Unemployment_rate": "mean"
}).reset_index()

plt.figure(figsize=(9, 5))
plt.plot(yearly["Year"], yearly["violent_crime_rate"], marker="o", label="Violent crime rate")
plt.plot(yearly["Year"], yearly["property_crime_rate"], marker="o", label="Property crime rate")
plt.plot(yearly["Year"], yearly["Unemployment_rate"] * 100, marker="o", label="Unemployment rate × 100")

plt.xlabel("Year")
plt.ylabel("Average Value")
plt.title("Average Crime and Unemployment Trends, 2000–2019")
plt.legend()
plt.tight_layout()
plt.savefig(f"{FIGURES_DIR}/yearly_trends.png", dpi=150)
plt.close()


# Figure 4: Average violent crime by state
state_avg = (
    df.groupby("State")["violent_crime_rate"]
    .mean()
    .sort_values(ascending=False)
)

top_bottom = pd.concat([state_avg.head(10), state_avg.tail(10)])
top_bottom.to_csv(f"{RESULTS_DIR}/state_violent_crime_rankings.csv")

plt.figure(figsize=(9, 7))
top_bottom.sort_values().plot(kind="barh")
plt.xlabel("Average Violent Crime Rate per 100,000")
plt.title("Top and Bottom 10 States by Average Violent Crime Rate")
plt.tight_layout()
plt.savefig(f"{FIGURES_DIR}/state_violent_crime_rankings.png", dpi=150)
plt.close()

print("\nAnalysis complete.")
print(f"Results saved in: {RESULTS_DIR}/")
print(f"Figures saved in: {FIGURES_DIR}/")