from itertools import combinations
from pathlib import Path
from random import randint, shuffle
from typing import List, Tuple
from tfTeams._dataclasses.champions import StandardChampion
from tfTeams._dataclasses.synergy import Synergy
from tfTeams._evaluation.evaluate import Comp
from tfTeams._factories.create_champions import ALL_CHAMPIONS, create_all_champions
from more_itertools import ilen


def generate_all_champions_combinations(champions_dataset_path: Path, length_comp: int) -> combinations:
    all_champions = create_all_champions(champ_dataset_path=champions_dataset_path)
    all_combinations = combinations(all_champions, length_comp)
    return all_combinations

def find_best_comps(all_champion_combinations: combinations) -> List[Comp]:
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


def generate_random_list_champions(length_compositon) -> List[StandardChampion]:
    list_champions = []
    while len(list_champions) < length_compositon:
        random_champ = ALL_CHAMPIONS.all_champions[randint(0, len(ALL_CHAMPIONS.all_champions) - 1)]
        if random_champ not in list_champions:
            list_champions.append(random_champ)
    return list_champions


def generate_random_single_composition(all_compositions: List[None] | List[Comp], length_compositon: int) -> Comp:
    while True:
        random_composition = Comp(champions=generate_random_list_champions(length_compositon=length_compositon))
        if random_composition not in all_compositions:
                return random_composition


def generate_random_list_compositions(length_compositon: int) -> List[Comp]:
    compositions = []
    for _ in range(1000):
        compositions.append(generate_random_single_composition(all_compositions=compositions, length_compositon= length_compositon))
    return compositions


def new_composition_from_parents(first_parent_composition: Comp, second_parent_composition: Comp) -> Comp:
    composition_lentgh = len(first_parent_composition.champions)
    champions_from_first_parent = first_parent_composition.champions
    champions_from_second_parent = second_parent_composition.champions
    all_champions = list(set(champions_from_first_parent + champions_from_second_parent ))
    shuffle(all_champions)
    return Comp(champions=all_champions[:composition_lentgh])


def genetic_multiplication_composition(parent_composition: List[Comp]) -> List[Comp]:
    for couple_index in range(250):
        new_composition = new_composition_from_parents(first_parent_composition=parent_composition[couple_index], second_parent_composition=parent_composition[250-couple_index])
        if new_composition not in parent_composition:
            parent_composition.append(new_composition)
        else:
            parent_composition.append(generate_random_single_composition(all_compositions=parent_composition, length_compositon=len(parent_composition[0].champions)))
    return parent_composition


def generate_random_champion(composition: Comp) -> StandardChampion:
    while True:
        random_champion = ALL_CHAMPIONS.all_champions[randint(0, len(ALL_CHAMPIONS.all_champions) - 1)]
        if random_champion not in composition.champions:
            return random_champion


def some_composition_mutate(all_compositions: List[Comp]) -> List[Comp]:
    random_composition_index, random_champion_index = randint(0, 59), randint(0, len(all_compositions[0].champions) - 1)
    all_compositions[random_composition_index].champions[random_champion_index] = generate_random_champion(composition=all_compositions[random_composition_index])
    return all_compositions

def no_upgrade_for_while(wave: int) -> bool:
    return wave == 100


def best_comps_from_genetics(compositions: List[Comp]) -> List[Comp]:
    best_comps = []
    best_score = compositions[0].score 
    for composition in compositions:
        if composition.score == best_score:
            best_comps.append(composition)
        else:
            return best_comps
    raise ValueError("No compositions in genetic algorythm")


def best_genetic_composition(initial_compositions: List[Comp]) -> List[Comp]:
    wave_without_upgrade = 0
    actual_compositions = initial_compositions 
    best_evaluation = actual_compositions[0].score
    while True:
        actual_compositions.sort(key=lambda x: x.score, reverse=True)
        if actual_compositions[0].score < best_evaluation:
            best_evaluation = actual_compositions[0].score
        else:
            wave_without_upgrade += 1
        if no_upgrade_for_while(wave=wave_without_upgrade):
            break
        actual_compositions = actual_compositions[:500]
        actual_compositions = genetic_multiplication_composition(parent_composition=actual_compositions)
        if randint(0,5):
            actual_compositions = some_composition_mutate(all_compositions = actual_compositions)
    return best_comps_from_genetics(compositions=actual_compositions)


def find_best_compositions(length_compositon: int) -> List[Comp]:
    # Initiation 
    all_comps = generate_random_list_compositions(length_compositon=length_compositon)
    print("all comps generated")
    return best_genetic_composition(initial_compositions=all_comps)


def display_best_comps(best_comps: List[Comp]) -> None:
    for index, compositon in enumerate(best_comps):
        print(f"Compisition {index}")
        print("Champions : \n")
        for champion in compositon.champions:
            print(champion)
        print(f" Synergies : \n")
        for synergy, count in compositon.all_synergies_count.items():
            print(f"{synergy.name} with {count} champions")
        print(f"With headliner : {compositon.headliner}, we have {compositon.all_medals_from_comp(headliner=compositon.headliner)} medals")
        print(f"Score : {compositon.score}")