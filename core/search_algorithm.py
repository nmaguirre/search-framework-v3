"""
Abstract base class for all search algorithms.
"""

from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Dict, Any
from core.search_problem import SearchProblem
from core.search_state import SearchState


class SearchAlgorithm(ABC):
    """
    Abstract base class for search algorithms.
    All search algorithms should inherit from this class.
    """

    def __init__(self, problem: SearchProblem):
        """
        Initialize search algorithm with a problem.

        Args:
            problem: The search problem to solve
        """
        self.problem = problem

    @abstractmethod
    def solve(self, verbose: bool = True) -> Optional[List[Tuple[SearchState, str]]]:
        """
        Solve the problem using the specific search algorithm.

        Args:
            verbose: Whether to print progress information

        Returns:
            List of (state, action) pairs representing the solution path,
            or None if no solution found
        """
        pass
