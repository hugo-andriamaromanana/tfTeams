from itertools import combinations
from pathlib import Path
from typing import List, Tuple
from tfTeams._dataclasses.champions import StandardChampion
from tfTeams._dataclasses.synergy import Synergy
from tfTeams._evaluation.evaluate import Comp
from tfTeams._factories.create_champions import create_all_champions


def generate_all_champions_combinations(champions_dataset_path: Path, length_comp: int) -> combinations[Tuple[StandardChampion, ...]]:
    all_champions = create_all_champions(champ_dataset_path=champions_dataset_path)
    all_combinations = combinations(all_champions, length_comp)
    return all_combinations

def find_best_comps(all_champion_combinations: combinations[Tuple[StandardChampion, ...]]) -> List[Comp]:
    """
    With all possible combinations , we are looking for THE BEST compositions by their evaluation. 
    Iterate through all combinations, transforms the current combination into a composition.
    If the evaluation is better than the evaluation of the previous best compositions, our composition replace previous best compositions. 
    If the evaluation is equals to the evaluation of the previous best compositions, our composition is appened into the best compositions.
    """
    best_compositions = []
    best_score = 0
    for champion_combination in all_champion_combinations:
        actual_composition = Comp([champion for champion in champion_combination])
        actual_score = actual_composition.score
        if actual_score > best_score:
            best_compositions = [actual_composition]
            best_score = actual_score
        elif actual_score == best_score:
            best_compositions.append(actual_composition)
    return best_compositions