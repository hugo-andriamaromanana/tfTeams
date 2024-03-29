from pathlib import Path
from typing import List

from tfTeams._dataclasses.synergy import Synergy

from tfTeams._dataclasses.champions import StandardChampion, ChampionCost
from tfTeams._factories.create_synergies import ALL_SYNERGIES
from tfTeams._parsers.dataset_parsers import parse_csv_champions

from icecream import ic

def create_synergy_by_name(synergy_name: str) -> Synergy:
    for synergy in ALL_SYNERGIES.get_synergies():
        if synergy.name == synergy_name:
            return synergy
    print(synergy_name)
    print(ALL_SYNERGIES.get_synergies())
    raise ValueError("Synergy was not found by name")

def create_all_champions(champ_dataset_path: Path) -> List[StandardChampion]:
    champions_dataframe = parse_csv_champions(champ_dataset=champ_dataset_path)
    all_champions = []
    for _, champion_row in champions_dataframe.iterrows():
        champion_synergies = [create_synergy_by_name(synergy_name=synergy_name) for synergy_name in champion_row["synergies"]]
        all_champions.append(StandardChampion(name=champion_row["name"], cost=ChampionCost(champion_row["cost"]), synergies=champion_synergies))
    return all_champions


class CreateAllChampions:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def initialize(self, champ_dataset_path: Path):
        if champ_dataset_path != Path(""):
            self.all_champions = create_all_champions(champ_dataset_path=champ_dataset_path) 
        else:
            self.all_champions = []
            
    def update_config(self, champ_dataset_path:Path):
        return self.initialize(champ_dataset_path=champ_dataset_path)
    
    def get_synergies(self):
        return self.all_champions

    


ALL_CHAMPIONS = CreateAllChampions()
ALL_CHAMPIONS.initialize(champ_dataset_path=Path(""))
