from pandas import read_csv, DataFrame
from pathlib import Path

def parse_csv_synergies(syn_dataset: Path) -> DataFrame: 
    dataframe = read_csv(syn_dataset)
    dataframe["stades"] = dataframe["stades"].str.split()
    return dataframe


df = parse_csv_synergies(syn_dataset="./assets/synergies.csv")
print(df.iloc[0]["stades"][0])