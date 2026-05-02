import pandas as pd

def add_lags(df, lags=3):
    for col in ["GDP_Growth", "R&D_Expenditure", "Inflation"]:
        for l in range(1, lags+1):
            df[f"{col}_lag{l}"] = df[col].shift(l)
    return df.dropna()