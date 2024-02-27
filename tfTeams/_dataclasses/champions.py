from dataclasses import dataclass
from typing import List, Any
from abc import ABC, abstractmethod
from .synergy import Synergy

@dataclass
class ChampionType(ABC):
    name: str
    cost: int
    @abstractmethod
    def get_current_synergy(self) -> Any:
        pass

@dataclass
class StandardChampion(ChampionType):
    synergies: List[Synergy]
    
    def get_current_synergy(self) -> List[Synergy]:
        return self.synergies