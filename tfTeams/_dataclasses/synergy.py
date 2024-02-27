from dataclasses import dataclass
from typing import Dict, Optional

from .rank import Medal
@dataclass(eq= True)
class Synergy:
    name: str
    stades: Dict[int, Medal]

    def get_medal_for_rank(self, current_count: int) -> Optional[Medal]:
        """Given a synergy and a count, return the current Medal for it"""
        for count in reversed(range(current_count+1)):
            medal = self.stades.get(count) 
            if not (medal is None):
                return medal
        return None
            
    def __hash__(self):
        return hash(self)