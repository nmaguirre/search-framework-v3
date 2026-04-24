from typing import List, Optional, Set, Tuple
from core.search_algorithm import SearchAlgorithm
from core.search_problem import SearchProblem
from core.search_state import SearchState

class BestFirstSearch(SearchAlgorithm):
    """
    Best-First Search implementation of the SearchAlgorithm interface.
    It uses a priority queue of opened nodes to explore, and maintains a set of visited states to avoid cycles.
    """

    def __init__(self, problem: SearchProblem):
        super().__init__(problem)

    def solve(self, verbose: bool = True) -> Optional[List[Tuple[SearchState, str]]]:
        opened_states = [(self.problem.get_initial_state(), [], self.problem.heuristic(self.problem.get_initial_state()))]
        visited = set()
        while opened_states:
            opened_states.sort(key=lambda x: x[2])
            current_state, path, _ = opened_states.pop(0)
            if not current_state in visited:
                visited.add(current_state)
                if self.problem.is_goal(current_state):
                    return path + [(current_state, "Goal state")]
                else:
                    for next_state, action in self.problem.get_successors(current_state):
                        if next_state not in visited:
                            opened_states.append((next_state, path + [(current_state, action)], self.problem.heuristic(next_state)))
        # priority queue is empty and no solution found
        return None



