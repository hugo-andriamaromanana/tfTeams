from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class ChampionType(ABC):
    cost: int
    @abstractmethod
    def get_current_synergy(self) -> Any:
        pass