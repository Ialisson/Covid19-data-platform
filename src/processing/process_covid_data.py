import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/owid-covid-data.csv")
PROCESSED_DATA_DIR = Path("data/processed")
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

def process_covid_data():
    df = pd.read_csv(RAW_DATA_PATH)

    # Seleciona colunas relevantes
    columns = [
        "location",
        "date",
        "total_cases",
        "new_cases",
        "total_deaths",
        "new_deaths",
        "people_vaccinated",
        "people_fully_vaccinated"
    ]

    df = df[columns]

    # Converter data
    df["date"] = pd.to_datetime(df["date"])

    # Evitar divisão por zero
    df["case_fatality_rate"] = (
        df["total_deaths"] / df["total_cases"]
    )

    # Média móvel de 7 dias (por país)
    df["new_cases_7d_avg"] = (
        df.groupby("location")["new_cases"]
        .rolling(window=7)
        .mean()
        .reset_index(level=0, drop=True)
    )

    output_path = PROCESSED_DATA_DIR / "covid_metrics.csv"
    df.to_csv(output_path, index=False)

    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    process_covid_data()