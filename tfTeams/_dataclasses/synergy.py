from dataclasses import dataclass
from typing import Dict

from .rank import Medal, Rank

@dataclass
class Synergy:
    name: str
    stades: Dict[Rank, Medal]

    def get_medal_for_rank(self, current_count: int) -> Medal:
        """Given a synergy and a count, return the current Medal for it"""
        rank_values = [rank.value[0] for rank in Rank]
        closest_rank_value = min(rank_values, key=lambda x: abs(x - current_count))
        closest_rank = next(rank for rank in Rank if rank.value == closest_rank_value)
        return self.stades[closest_rank]