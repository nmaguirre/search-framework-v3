"""
Maze state for maze solving problem.
"""

from typing import List, Tuple, Optional
from core.search_state import SearchState

class MazeState(SearchState):
    """
    State for maze navigation.
    Represents current position (row, column) in the maze.
    """

    def __init__(self, row: int, col: int):
        """
        Initialize maze state.

        Args:
            row: Row coordinate
            col: Column coordinate
        """
        self.row = row
        self.col = col

    def __hash__(self) -> int:
        """Hash based on coordinates."""
        return hash((self.row, self.col))

    def __eq__(self, other: object) -> bool:
        """Equality based on coordinates."""
        if not isinstance(other, MazeState):
            return False
        return self.row == other.row and self.col == other.col

    def __str__(self) -> str:
        return f"({self.row}, {self.col})"

    def __repr__(self) -> str:
        return f"MazeState({self.row}, {self.col})"

    def get_coordinates(self) -> Tuple[int, int]:
        """Return (row, col) tuple."""
        return (self.row, self.col)
