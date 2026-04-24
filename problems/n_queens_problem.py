from core.search_problem import SearchProblem
from problems.n_queens_state import NQueensState
import random

"""
N-Queens problem implementation.
The N-Queens problem is a classic combinatorial problem that asks for all arrangements of N queens on an N x N 
chessboard such that no two queens threaten each other. This means that no two queens can be in the same row, column, 
or diagonal.
"""


class NQueensProblem(SearchProblem):

    def __init__(self, board_size: int, initial_state: NQueensState = None):
        """
        Initialize N-Queens problem.

        Args:
            board_size: The size of the chessboard (N)
        """
        assert board_size > 0, "Board size must be a positive integer"
        self.board_size = board_size
        if (initial_state is not None):
            assert len(initial_state.queens) == board_size, "Initial state must have the same number of queens as board size"
            self.initial_state = initial_state

    def get_initial_state(self) -> NQueensState:
        """Return the initial state of the problem.
            Every queen is placed in the first column of its corresponding row.
        """
        if hasattr(self, 'initial_state'):
            return self.initial_state
        else:
            initial_queens = tuple(0 for _ in range(self.board_size))
            return NQueensState(self.board_size, initial_queens)

    def is_goal(self, state: NQueensState) -> bool:
        """Check if the given state is a goal state (valid arrangement of queens)."""
        assert len(state.queens) == self.board_size, "State must have the same number of queens as board size"
        for i in range(self.board_size):
            for j in range(i + 1, self.board_size):
                if state.queens[i] == state.queens[j]:
                    # same column
                    return False
                if abs(state.queens[i] - state.queens[j]) == abs(i - j):
                    # same diagonal
                    return False
        return True

    def get_successors(self, state: NQueensState):
        """Generate successor states by placing every queen in the next row (if possible)."""
        assert len(state.queens) == self.board_size, "State must have the same number of queens as board size"
        successors = []
        for row in range(self.board_size):
            if state.queens[row] < self.board_size - 1:
                # can move the queen in this row to the next column
                new_queens = list(state.queens)
                new_queens[row] += 1
                successors.append((NQueensState(self.board_size, tuple(new_queens)),
                                   "Move queen in row {} to column {}".format(row, new_queens[row])))
        return successors

    def heuristic(self, state: NQueensState) -> float:
        """Heuristic function to estimate the cost to reach the goal state.
            We can use the number of pairs of queens that are attacking each other as a heuristic.
        """
        attacking_pairs = 0
        for i in range(self.board_size):
            for j in range(i + 1, self.board_size):
                if state.queens[i] == state.queens[j]:
                    # same column
                    attacking_pairs += 1
                if abs(state.queens[i] - state.queens[j]) == abs(i - j):
                    # same diagonal
                    attacking_pairs += 1
        return attacking_pairs

    @staticmethod
    def random_state(board_size: int) -> NQueensState:
        """Generate a random state for the N-Queens problem."""
        assert board_size > 0, "Board size must be a positive integer"
        random.seed()
        random_queens = tuple(random.randint(0, board_size - 1) for _ in range(board_size))
        return NQueensState(board_size, random_queens)