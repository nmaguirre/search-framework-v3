from typing import Tuple
from core.search_state import SearchState
"""
N-Queens state for N-Queens problem.
Represents a state of the board, where each queen is placed in a specific column of a specific row. 
"""
class NQueensState(SearchState):

    def __init__(self, board_size: int, queens: Tuple[int, ...]):
        """
        Initialize N-Queens state.

        Args:
            queens: A tuple where the index represents the row and the value represents the column of the queen in that
            row.
        """
        assert len(queens) == board_size, "Number of queens must match board size"
        for q in queens:
            assert 0 <= q < board_size, "Queen positions must be within board size"
        self.board_size = board_size
        self.queens = queens

    def __hash__(self) -> int:
        """Hash based on queen positions."""
        return hash(self.queens)

    def __eq__(self, other: object) -> bool:
        """Equality based on queen positions."""
        if not isinstance(other, NQueensState):
            return False
        return self.queens == other.queens

    def __str__(self) -> str:
        """String representation of the board."""
        board = []
        for row in range(self.board_size):
            line = ""
            for col in range(self.board_size):
                if self.queens[col] == row:
                    line += "Q "
                else:
                    line += ". "
            board.append(line.strip())
        return "\n".join(board)

    def __repr__(self) -> str:
        return f"NQueensState({self.queens})"