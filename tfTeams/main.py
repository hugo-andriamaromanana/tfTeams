from pathlib import Path
from tfTeams._factories.create_synergies import CreateAllSynergies
from tfTeams.generate_comps import display_best_comps, find_best_comps, generate_all_champions_combinations
from icecream import ic


def main(champion_dataset_path:Path, synergies_dataset_path:Path):
    ALL_SYNERGIES = CreateAllSynergies().update_config(syn_dataset_path=synergies_dataset_path)
    print(ALL_SYNERGIES)
    all_combinations = generate_all_champions_combinations(champions_dataset_path=champion_dataset_path, length_comp=8)
    print("All combinations done")
    best_comps = find_best_comps(all_champion_combinations=all_combinations)
    display_best_comps(best_comps=best_comps)



