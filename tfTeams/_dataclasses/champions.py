from dataclasses import dataclass
from typing import List

from .synergy import Synergy
from .champion_type import ChampionType

@dataclass
class StandardChampion(ChampionType):
    synergies: List[Synergy]
    
    def get_current_synergy(self) -> List[Synergy]:
        return self.synergies