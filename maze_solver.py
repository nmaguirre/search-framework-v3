from problems import MazeProblem, MazeState
from algorithms import DepthFirstSearch, BestFirstSearch

# Create the problem
problem = MazeProblem('problems/large_maze.txt')
dfs = DepthFirstSearch(problem)

path = dfs.solve()
if path:
    print("Path length is " + str(len(path)))
    for i, (state, action) in enumerate(path):
        print(f"Step {i:3}: {action:45} → {state}")

best_first = BestFirstSearch(problem)

path = best_first.solve()
if path:
    print("Path length is " + str(len(path)))
    for i, (state, action) in enumerate(path):
        print(f"Step {i:3}: {action:45} → {state}")
