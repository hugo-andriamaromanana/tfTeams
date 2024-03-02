from dataclasses import dataclass
from pathlib import Path

EMPTY_PATH = Path("")


@dataclass
class ConfigPaths:
    synergies_path: Path
    champions_path: Path


class PathInitializer:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(self, syn_dataset_path: Path, champions_dataset_path: Path):
        if syn_dataset_path != EMPTY_PATH:
            self.config_paths = ConfigPaths(syn_dataset_path, champions_dataset_path)
        else:
            self.config_paths = ConfigPaths(EMPTY_PATH, EMPTY_PATH)

    def update_config(self, syn_dataset_path: Path, champions_dataset_path: Path):
        return self.initialize(syn_dataset_path, champions_dataset_path)

    def get_config_paths(self):
        return self.config_paths



CONFIG_PATHS = PathInitializer()
CONFIG_PATHS.initialize(EMPTY_PATH,EMPTY_PATH)
