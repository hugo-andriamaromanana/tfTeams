from pandas import read_csv, DataFrame
from pathlib import Path

def parse_csv_champions(champ_dataset: Path) -> DataFrame: 
    dataframe = read_csv(champ_dataset)
    dataframe["synergies"] = dataframe["synergies"].str.split()
    return dataframe

def parse_csv_synergies(syn_dataset: Path) -> DataFrame: 
    dataframe = read_csv(syn_dataset)
    dataframe["stades"] = dataframe["stades"].str.split()
    return dataframe