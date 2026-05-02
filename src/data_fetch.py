import pandas as pd

import requests

COUNTRIES = {

    "CHN": "China",

    "DEU": "Germany",

}

INDICATORS = {

    "NY.GDP.MKTP.KD.ZG": "GDP_Growth",

    "GB.XPD.RSDV.GD.ZS": "R&D_Expenditure",

    "FP.CPI.TOTL.ZG": "Inflation",

    "SL.UEM.TOTL.ZS": "Unemployment",

}

def fetch_world_bank_indicator(country_code, indicator_code, start_year=2000, end_year=2024):

    url = (

        f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"

        f"?format=json&per_page=20000&date={start_year}:{end_year}"

    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    payload = response.json()

    if len(payload) < 2 or payload[1] is None:

        return pd.DataFrame(columns=["Year", "Value"])

    rows = []

    for item in payload[1]:

        rows.append({

            "Year": int(item["date"]),

            "Value": item["value"],

        })

    return pd.DataFrame(rows)

def load_data(start_year=2000, end_year=2024):

    country_frames = []

    for country_code, country_name in COUNTRIES.items():

        merged = None

        for indicator_code, variable_name in INDICATORS.items():

            df = fetch_world_bank_indicator(

                country_code=country_code,

                indicator_code=indicator_code,

                start_year=start_year,

                end_year=end_year,

            )

            df = df.rename(columns={"Value": variable_name})

            if merged is None:

                merged = df

            else:

                merged = merged.merge(df, on="Year", how="outer")

        merged["Country"] = country_name

        country_frames.append(merged)

    final = pd.concat(country_frames, ignore_index=True)

    final = final.sort_values(["Country", "Year"]).reset_index(drop=True)

    numeric_cols = [

        "GDP_Growth",

        "R&D_Expenditure",

        "Inflation",

        "Unemployment",

    ]

    for col in numeric_cols:

        final[col] = pd.to_numeric(final[col], errors="coerce")

    final = final.groupby("Country", group_keys=False).apply(

        lambda x: x.sort_values("Year").interpolate(limit_direction="both")

    )

    return final.reset_index(drop=True)