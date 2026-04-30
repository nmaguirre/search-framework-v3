from problems import NQueensProblem, NQueensState
from algorithms import DepthFirstSearch, BestFirstSearch
import time


def alternative_successors(state: NQueensState):
    """
    Generates successors by moving each queen to a +2 -2 row in the same column
    """
    assert isinstance(state, NQueensState)
    successors = []
    for col in range(state.board_size):
        current_row = state.queens[col]
        for delta in [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 6, 7]:
            new_row = current_row + delta
            if 0 <= new_row < state.board_size:
                new_queens = list(state.queens)
                new_queens[col] = new_row
                successors.append(
                    (NQueensState(state.board_size, tuple(new_queens)), f"Move queen in column {col} to row {new_row}"))
    return successors


# Create the problem
problem = NQueensProblem(8)
current_state = None
curr_time = time.time()
max_restarts = 100
for restart in range(max_restarts):
    problem = NQueensProblem(8, initial_state=NQueensProblem.random_state(8))
    #problem = NQueensProblem(8)
    current_state = problem.get_initial_state()
    stuck = False
    while not stuck and not problem.is_goal(current_state):
        #successors = problem.get_successors(current_state)
        successors = alternative_successors(current_state)
        if not successors:
            stuck = True
        else:
            # Choose the successor with the lowest heuristic value
            new_state, action = min(successors, key=lambda x: problem.heuristic(x[0]))
            if problem.heuristic(new_state) >= problem.heuristic(current_state):
                stuck = True
            else:
                current_state = new_state
    if problem.is_goal(current_state):
        break
solving_time = time.time() - curr_time
print(f"Hill Climbing solving time: {solving_time:.4f} seconds")
if current_state:
    if problem.is_goal(current_state):
        print("Solution using Hill Climbing: ")
        print(current_state)
    else:
        print("No solution found with Hill Climbing")
        print("Final state: ")
        print(current_state)
else:
    print("No solution found with Hill Climbing")
