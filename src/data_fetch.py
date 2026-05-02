import pandas as pd
import numpy as np

def generate_placeholder_data(country):
    years = list(range(2000, 2025))
    data = pd.DataFrame({
        "Year": years,
        "GDP_Growth": np.random.normal(3, 2, len(years)),
        "R&D_Expenditure": np.random.uniform(0.5, 3, len(years)),
        "Inflation": np.random.uniform(1, 6, len(years)),
        "Unemployment": np.random.uniform(3, 10, len(years)),
        "Interest_Rate": np.random.uniform(0, 6, len(years)),
    })
    data["Country"] = country
    return data

def load_data():
    china = generate_placeholder_data("China")
    germany = generate_placeholder_data("Germany")
    return pd.concat([china, germany])