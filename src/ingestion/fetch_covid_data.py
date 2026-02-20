import requests
from pathlib import Path

OWID_COVID_DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

def fetch_covid_data():
    response = requests.get(OWID_COVID_DATA_URL)
    response.raise_for_status()

    file_path = RAW_DATA_DIR / "owid-covid-data.csv"
    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"COVID-19 data downloaded to {file_path}")

if __name__ == "__main__":
    fetch_covid_data()