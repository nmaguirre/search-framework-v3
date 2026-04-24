from problems import MazeProblem, MazeState

# Create the problem
problem = MazeProblem('problems/large_maze.txt')
    
print("=" * 70)
print("MAZE PROBLEM")
problem.print_maze()

# Get initial state
initial_state = problem.get_initial_state()
print(f"\nStarting from: {initial_state}")
print("Searching with DFS...")
print("-" * 70)
    
# Stack stores (state, path)
# path is list of (state, action) pairs
stack = [(initial_state, [])]
    
# Track visited states to avoid cycles
visited = set()
found = False    
while not found and stack:
    # Pop from stack (LIFO - Depth First!)
    current_state, path = stack.pop()
        
    # Check if we found the goal
    if problem.is_goal(current_state):
        print(f"SOLUTION FOUND!")
        print(f"Total steps: {len(path)}")
        print("\nSolution sequence:")
            
        # Print initial state
        step = 0
        no_action = "Initial state"
        print(f"Step {step:3}: {no_action:45} → {initial_state}")
        # Print each action and resulting state
        for i, (state, action) in enumerate(path, 1):
            print(f"Step {i:3}: {action:45} → {state}")
        print("-" * 70)
        problem.print_maze(path)
        found = True
    else:
        if not (current_state in visited):
            # Mark as visited
            visited.add(current_state)
            # Add successors to stack 
            successors = problem.get_successors(current_state)
            for next_state, action in successors:
                if next_state not in visited:
                    stack.append((next_state, path + [(next_state, action)])) 
if not found:    
    print("Search space exhausted and no solution found.")

