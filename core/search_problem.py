from abc import ABC, abstractmethod
from typing import List, Tuple
from core.search_state import SearchState

class SearchProblem(ABC):
    """
    Abstract base class for any search problem.
    Defines the interface that all search problems must implement.
    """
    
    @abstractmethod
    def get_initial_state(self) -> SearchState:
        """Return the initial state of the problem"""
        pass
    
    @abstractmethod
    def is_goal(self, state: SearchState) -> bool:
        """Check if a state is a goal state"""
        pass
    
    @abstractmethod
    def get_successors(self, state: SearchState) -> List[Tuple[SearchState, str]]:
        """
        Return all possible successor states from current state.
        Each successor is a tuple (next_state, action_description)
        """
        pass

    def get_cost(self, state: SearchState, action: str) -> float:
        """Return the cost of taking an action from a state"""
        # Default implementation: all actions have the same cost: unit
        return 1

    def heuristic(self, state: SearchState) -> float:
        """
        Heuristic function for informed search.
        Estimates the cost/distance from current state to goal.

        """
        # Default implementation for uninformed search
        # Override this method in subclasses for informed search
        return 0