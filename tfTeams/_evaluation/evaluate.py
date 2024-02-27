from typing import Dict, List

from dataclasses import dataclass, field

from .._dataclasses.synergy import Synergy

from .._dataclasses.rank import Medal

from .._dataclasses.champions import StandardChampion

def calculate_medals_score(medals: List[Medal]) -> float:
    score = 0
    #Magie: bronze_medal * bronze coef ect....
    for medal in medals:
        score += medal.value
    return score

def calculate_champions_score(champions: List[StandardChampion]) -> float:
    score = 0
    for champion in champions:
        score += champion.cost.value
    return score

def count_synergies(comp: list[StandardChampion], all_synergies: list[Synergy]) -> Dict[Synergy, int]:
    all_synergies_as_dict = {synergy: 0 for synergy in all_synergies}
    for champion in comp:
        for synergy in champion.synergies:
            all_synergies_as_dict[synergy] += 1
    return all_synergies_as_dict

ALL_SYNERGIES = []

@dataclass
class Comp:
    champions: List[StandardChampion] = field(default_factory=list)
    
    @property
    def medals(self) -> List[Medal]:
        all_synergies_count = count_synergies(self.champions,ALL_SYNERGIES)
        medals = []
        for count,synergy in enumerate(all_synergies_count):
            medal = synergy.get_medal_for_rank(count)
            if not(medal is None):
                medals.append(medal)
        return medals
    
    @property
    def evaluation(self) -> float:
        champions_score = calculate_champions_score(self.champions)
        medals_score = calculate_medals_score(self.medals)
        return champions_score + medals_score
    
    