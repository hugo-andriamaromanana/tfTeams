from dataclasses import dataclass, field
from enum import Enum
from typing import List, Any
from abc import ABC, abstractmethod
from .synergy import Synergy

class ChampionCost(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

@dataclass
class ChampionType(ABC):
    name: str

    @abstractmethod
    def get_current_synergy(self) -> Any:
        pass


class StandardChampion(ChampionType):
    synergies: List[Synergy]
    
    def get_current_synergy(self) -> List[Synergy]:
        return self.synergies