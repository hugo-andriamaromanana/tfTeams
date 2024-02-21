from enum import Enum, auto


class Rank(Enum):
    One = (1,)
    Two = (2,)
    Three = (3,)
    Four = (4,)
    Five = (5,)
    Six = (6,)
    Seven = (7,)
    Eight = (8,)
    Nine = (9,)


class Medal(Enum):
    Bronze = auto()
    Silver = auto()
    Gold = auto()
    Platinum = auto()
