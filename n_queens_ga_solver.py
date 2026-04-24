from problems import NQueensProblem, NQueensState
from algorithms import DepthFirstSearch, BestFirstSearch
import time
import random


def crossover(state1: NQueensState, state2: NQueensState):
    """
    Generates successors by combining two states, taking the first half of the queens from state1
    and the second half from state2
    """
    assert isinstance(state1, NQueensState)
    assert isinstance(state2, NQueensState)
    assert state1.board_size == state2.board_size
    board_size = state1.board_size
    mid = board_size // 2
    new_queens = list(state1.queens[:mid]) + list(state2.queens[mid:])
    return NQueensState(board_size, tuple(new_queens))

def mutate(state: NQueensState):
    """
    Generates successors by randomly moving one queen to a different row in the same column
    """
    assert isinstance(state, NQueensState)
    board_size = state.board_size
    col = random.randint(0, board_size - 1)
    current_row = state.queens[col]
    new_row = random.randint(0, board_size - 1)
    while new_row == current_row:
        new_row = random.randint(0, board_size - 1)
    new_queens = list(state.queens)
    new_queens[col] = new_row
    return NQueensState(board_size, tuple(new_queens))


# Create the problem
problem = NQueensProblem(8)
# Create the initial population
population_size = 1000
population = [NQueensProblem.random_state(8) for _ in range(population_size)]
curr_time = time.time()
max_generations = 10000
for generation in range(max_generations):
    # Evaluate fitness of the population
    fitness = [problem.heuristic(state) for state in population]
    if 0 in fitness:
        solution_index = fitness.index(0)
        print(f"Solution found in generation {generation}")
        print(population[solution_index])
        break
    # Select random parents
    size_of_selection = len(population) // 2
    selected_indices = random.sample(range(len(population)), size_of_selection)
    selected_population = [population[i] for i in selected_indices]
    # Create the next generation through crossover and mutation
    next_generation = []
    for i in range(0, len(selected_population) - 1, 2):
        parent1 = selected_population[i]
        parent2 = selected_population[i + 1]
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)
    population = next_generation



