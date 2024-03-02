from pathlib import Path
from tfTeams.generate_comps import display_best_comps, find_best_compositions
from .path_config import PathInitializer


def main(champion_dataset_path: Path, synergies_dataset_path: Path):
    PathInitializer().initialize(synergies_dataset_path, champion_dataset_path)
    best_comps = find_best_compositions(length_compositon=8)
    display_best_comps(best_comps=best_comps)
