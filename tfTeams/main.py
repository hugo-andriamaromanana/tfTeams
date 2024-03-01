from pathlib import Path
from tfTeams._factories.create_champions import CreateAllChampions
from tfTeams._factories.create_synergies import CreateAllSynergies
from tfTeams.generate_comps import display_best_comps, find_best_compositions


def main(champion_dataset_path:Path, synergies_dataset_path:Path):
    CreateAllSynergies().update_config(syn_dataset_path=synergies_dataset_path)
    CreateAllChampions().update_config(champ_dataset_path=champion_dataset_path)
    best_comps = find_best_compositions(length_compositon=8)
    display_best_comps(best_comps=best_comps)



