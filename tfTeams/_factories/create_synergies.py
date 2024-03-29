from dataclasses import dataclass
from importlib.machinery import all_suffixes
from pathlib import Path
import re
from typing import List, Dict, Tuple

from tfTeams._dataclasses.champions import Synergy
from tfTeams._dataclasses.rank import Medal
from tfTeams._parsers.dataset_parsers import parse_csv_synergies

def split_stade_parsed(string_to_split: str) -> Tuple[int, str]:
    match_string = re.match(r'(\d+)([a-zA-Z])', string_to_split)
    if match_string is None:
        raise ValueError("Splitting error, couldn't split the string into a tuple of int & string")
    return (int(match_string.group(1)), match_string.group(2))


def get_medal_from_initial(initial: str) -> Medal:
    match initial:
        case "b":
            return Medal.Bronze
        case "s":
            return Medal.Silver
        case "g":
            return Medal.Gold
        case "p":
            return Medal.Platinum
        case _:
            raise ValueError("Initial error, no medal was found")
        

def get_stades(stades_parsed: List[str]) -> Dict[int, Medal]:
    synergy_medal_by_rank = {}
    for stade in stades_parsed:
        rank, medal_initial = split_stade_parsed(string_to_split=stade)
        synergy_medal_by_rank[rank] = get_medal_from_initial(initial=medal_initial)
    return synergy_medal_by_rank


def create_all_synergies(syn_dataset_path: Path) -> List[Synergy]:
    synergies_dataframe = parse_csv_synergies(syn_dataset=syn_dataset_path)
    all_synergies = []
    for _, synergy_row in synergies_dataframe.iterrows():
        medals_stade = get_stades(synergy_row["stades"])
        all_synergies.append(Synergy(name=synergy_row["name"], stades=medals_stade))
    return all_synergies


class CreateAllSynergies:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def initialize(self, syn_dataset_path: Path):
        if syn_dataset_path != Path(""):
            self.all_synergies = create_all_synergies(syn_dataset_path=syn_dataset_path) 
        else:
            self.all_synergies = []
            
    def update_config(self, syn_dataset_path:Path):
        return self.initialize(syn_dataset_path=syn_dataset_path)
    
    def get_synergies(self):
        return self.all_synergies

    


ALL_SYNERGIES = CreateAllSynergies()
ALL_SYNERGIES.initialize(syn_dataset_path=Path(""))


