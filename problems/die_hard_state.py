from typing import List, Tuple
from math import gcd

from core.search_state import SearchState

class WaterJugState(SearchState):
    """State for the water jug problem."""
    
    def __init__(self, jug1: int, jug2: int, jug1_cap: int, jug2_cap: int):
        self.jug1 = jug1
        self.jug2 = jug2
        self.jug1_cap = jug1_cap
        self.jug2_cap = jug2_cap
        
        assert 0 <= jug1 <= jug1_cap
        assert 0 <= jug2 <= jug2_cap
    
    def __hash__(self) -> int:
        return hash((self.jug1, self.jug2))
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, WaterJugState):
            return False
        return self.jug1 == other.jug1 and self.jug2 == other.jug2
    
    def __str__(self) -> str:
        return f"({self.jug1}, {self.jug2})"
    
    def __repr__(self) -> str:
        return f"WaterJugState({self.jug1}, {self.jug2})"


