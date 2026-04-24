from core.search_problem import SearchProblem
from core.search_state import SearchState
from problems.die_hard_state import WaterJugState

from typing import List, Tuple


class DieHardProblem(SearchProblem):
    """Water jug problem: Measure exactly target gallons (for Die Hard case, use 5 and 3 as capacities,
    and 4 as target."""

    def __init__(self, jug1_capacity: int, jug2_capacity: int, target: int):
        self.jug1_cap = jug1_capacity
        self.jug2_cap = jug2_capacity
        self.target = target

    def get_initial_state(self) -> WaterJugState:
        return WaterJugState(0, 0, self.jug1_cap, self.jug2_cap)

    def is_goal(self, state: WaterJugState) -> bool:
        return state.jug1 == self.target or state.jug2 == self.target

    def get_successors(self, state: WaterJugState) -> List[Tuple[WaterJugState, str]]:
        """
        Generate all possible next states with their action descriptions.
        """
        successors = []
        jug1, jug2 = state.jug1, state.jug2

        # Move 1: Fill jug1
        if jug1 < self.jug1_cap:
            new_state = WaterJugState(self.jug1_cap, jug2, self.jug1_cap, self.jug2_cap)
            successors.append((new_state, f"Fill jug1 ({self.jug1_cap} gallons)"))

        # Move 2: Fill jug2
        if jug2 < self.jug2_cap:
            new_state = WaterJugState(jug1, self.jug2_cap, self.jug1_cap, self.jug2_cap)
            successors.append((new_state, f"Fill jug2 ({self.jug2_cap} gallons)"))

        # Move 3: Empty jug1
        if jug1 > 0:
            new_state = WaterJugState(0, jug2, self.jug1_cap, self.jug2_cap)
            successors.append((new_state, "Empty jug1"))

        # Move 4: Empty jug2
        if jug2 > 0:
            new_state = WaterJugState(jug1, 0, self.jug1_cap, self.jug2_cap)
            successors.append((new_state, "Empty jug2"))

        # Move 5: pour from jug1 to jug2
        if jug1 > 0 and jug2 < self.jug2_cap:
            init1 = jug1
            init2 = jug2
            while init1 > 0 and init2 < self.jug2_cap:
                init1 = init1 - 1
                init2 = init2 + 1
            new_state = WaterJugState(init1, init2, self.jug1_cap, self.jug2_cap)
            successors.append((new_state, f"Pour from jug1 into jug2 ({init2 - jug2} gallons)"))

        # Move 6: pour from jug2 to jug1
        if jug2 > 0 and jug1 < self.jug1_cap:
            init1 = jug1
            init2 = jug2
            while init2 > 0 and init1 < self.jug1_cap:
                init1 = init1 + 1
                init2 = init2 - 1
            new_state = WaterJugState(init1, init2, self.jug1_cap, self.jug2_cap)
            successors.append((new_state, f"Pour from jug2 into jug1 ({init1 - jug1} gallons)"))

        return successors

    def heuristic(self, state: WaterJugState) -> float:
        """
        Heuristic: minimum of the absolute difference between each jug and the target.
        """
        return min(abs(state.jug1 - self.target), abs(state.jug2 - self.target))
