from problems import NQueensProblem
from algorithms import DepthFirstSearch, BestFirstSearch
import time

# Create the problem
problem = NQueensProblem(8)
dfs = DepthFirstSearch(problem)

curr_time = time.time()
path = dfs.solve()
solving_time = time.time() - curr_time
print(f"DFS solving time: {solving_time:.4f} seconds")
if path:
    # I don't care about the path, I just want to see the final state
    print("Path length is " + str(len(path)))
    print("Solution using DFS: ")
    print(path[-1][0])
else:
    print("No solution found with DFS")

bfs = BestFirstSearch(problem)
curr_time = time.time()
path = bfs.solve()
solving_time = time.time() - curr_time
print(f"Best First Search solving time: {solving_time:.4f} seconds")
if path:
    # I don't care about the path, I just want to see the final state
    print("Path length is " + str(len(path)))
    print("Solution using Best First Search: ")
    print(path[-1][0])
else:
    print("No solution found with Best First Search")




