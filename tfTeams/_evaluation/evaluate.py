from typing import Dict, List

from tfTeams._factories.create_synergies import ALL_SYNERGIES
from .._dataclasses.synergy import Synergy
from .._dataclasses.rank import Medal
from .._dataclasses.champions import StandardChampion

def calculate_medals_score(medals: List[Medal]) -> float:
    score = 0
    for medal in medals:
        score += medal.value
    return score

def calculate_champions_score(champions: List[StandardChampion]) -> float:
    score = 0
    for champion in champions:
        score += champion.cost.value
    return score

def count_synergies(comp: list[StandardChampion]) -> Dict[Synergy, int]:
    all_synergies_as_dict = {synergy: 0 for synergy in ALL_SYNERGIES}
    for champion in comp:
        for synergy in champion.synergies:
            all_synergies_as_dict[synergy] += 1
    return all_synergies_as_dict


class Comp:
    def __init__(self, champions: List[StandardChampion]):
        self.champions = champions
        self.all_synergies_count = count_synergies(self.champions)
        self.score = self.evaluate()

    def _evaluate(self) -> float:
        score = 0
        for synergy in self.all_synergies_count:
            current_evaluation = self._evaluate_composition(synergy)
            score = max(score, current_evaluation)
            self.headliner = synergy if current_evaluation > score else self.headliner
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

    def _evaluate_composition(self, headliner) -> float:
        all_medals = self._all_medals_from_comp(headliner)
        champions_score = self._calculate_champions_score()
        medals_score = self._calculate_medals_score(all_medals)
        return champions_score + medals_score
