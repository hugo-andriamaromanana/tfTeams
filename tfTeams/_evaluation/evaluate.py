from typing import Dict, List

from dataclasses import dataclass, field

from tfTeams._factories.create_synergies import ALL_SYNERGIES

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

def count_synergies(comp: list[StandardChampion]) -> Dict[Synergy, int]:
    all_synergies_as_dict = {synergy: 0 for synergy in ALL_SYNERGIES.get_synergies()}
    for champion in comp:
        for synergy in champion.synergies:
            all_synergies_as_dict[synergy] += 1
    return all_synergies_as_dict


class Comp:

    def __init__(self, champions: List[StandardChampion]) -> None:
        self.champions = champions
        self.all_synergies_count = count_synergies(self.champions)
        self.score = self.evaluate()

    def evaluate(self) -> float:
        score = 0
        for synergy in self.all_synergies_count:
            current_evaluation = self.evaluate_composition(headliner=synergy)
            if current_evaluation > score:
                 score = current_evaluation
                 self.headliner = synergy
        return score
    
    def all_medals_from_comp(self, headliner:Synergy) -> List[Medal]:
        medals = []
        for synergy, count in self.all_synergies_count.items():
            if synergy == headliner:
                count+=1
            medal = synergy.get_medal_for_rank(count)
            if not(medal is None):
                medals.append(medal)
        return medals

    def evaluate_composition(self, headliner: Synergy) -> float:
        all_medals = self.all_medals_from_comp(headliner)
        champions_score = calculate_champions_score(self.champions)
        medals_score = calculate_medals_score(all_medals)
        return champions_score + medals_score
            
    
    