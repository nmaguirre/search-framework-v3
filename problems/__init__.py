# Import key classes so users can do:
# from problems import WaterJugProblem
from problems.die_hard_state import WaterJugState
from problems.die_hard_problem import DieHardProblem
from problems.maze_state import MazeState
from problems.maze_problem import MazeProblem
from problems.n_queens_state import NQueensState
from problems.n_queens_problem import NQueensProblem

__all__ = ['DieHardProblem', 'WaterJugState', 'MazeState', 'MazeProblem', 'NQueensState', 'NQueensProblem']
