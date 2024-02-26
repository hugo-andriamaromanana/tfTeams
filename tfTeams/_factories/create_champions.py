from pathlib import Path
from typing import List

from tfTeams._dataclasses.synergy import Synergy

from tfTeams._dataclasses.champions import StandardChampion
from tfTeams._factories.create_synergies import create_synergy_by_name
from tfTeams._parsers.dataset_parsers import parse_csv_champions

def create_all_champions(champ_dataset: Path, all_synergies: List[Synergy]) -> List[StandardChampion]:
    champions_dataframe = parse_csv_champions(champ_dataset=champ_dataset)
    all_champions = []
    for _, champion_row in champions_dataframe.iterrows():
        champion_synergies = [create_synergy_by_name(synergy_name=synergy_name, all_synergies=all_synergies) for synergy_name in champion_row["synergies"]]
        all_champions.append(StandardChampion(name=champion_row["name"], cost=champion_row["cost"], synergies=champion_synergies))
    return all_champions