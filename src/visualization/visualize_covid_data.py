import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/processed/covid_metrics.csv")
OUTPUT_DIR = Path("docs/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def plot_country_trends(country: str):
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])

    country_df = df[df["location"] == country]

    plt.figure(figsize=(12, 6))
    plt.plot(country_df["date"], country_df["new_cases_7d_avg"])
    plt.title(f"New COVID-19 Cases (7-day Avg) — {country}")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.tight_layout()

    output_file = OUTPUT_DIR / f"{country}_new_cases_7d_avg.png"
    plt.savefig(output_file)
    plt.close()

    print(f"Saved plot: {output_file}")

def plot_fatality_rate(country: str):
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])

    country_df = df[df["location"] == country]

    plt.figure(figsize=(12, 6))
    plt.plot(country_df["date"], country_df["case_fatality_rate"])
    plt.title(f"Case Fatality Rate — {country}")
    plt.xlabel("Date")
    plt.ylabel("CFR")
    plt.tight_layout()

    output_file = OUTPUT_DIR / f"{country}_case_fatality_rate.png"
    plt.savefig(output_file)
    plt.close()

    print(f"Saved plot: {output_file}")

if __name__ == "__main__":
    plot_country_trends("Brazil")
    plot_fatality_rate("Brazil")