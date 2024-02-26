from enum import Enum
from typing import Dict, List

from dataclasses import dataclass, field

from .._dataclasses.synergy import Synergy

from .._dataclasses.rank import Medal

from .._dataclasses.champions import StandardChampion

def calculate_medal_score(comp: List[StandardChampion]) -> float:
    score = 0
    #Magie: bronze_medal * bronze coef ect....
    for champion in comp:
        score+= 
    return 0.1

def evalute_comp(comp: List[StandardChampion]) -> float:
    pass

def count_synergies(comp: list[StandardChampion], all_synergies: list[Synergy]) -> Dict[Synergy, int]:
    all_synergies_as_dict = {synergy: 0 for synergy in all_synergies}
    for champion in comp:
        for synergy in champion.synergies:
            all_synergies_as_dict[synergy] += 1
    return all_synergies_as_dict

@dataclass
class Comp:
    champions: List[StandardChampion] = field(default_factory=list)

    @property
    def medals(self) -> List[Medal]:
        all_synergies_count = count_synergies()
        medals = []
        for champion in self.champions:
            