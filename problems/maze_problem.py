"""
Maze navigation problem for search framework.
Maze configuration is read from a text file.
"""

from typing import List, Tuple, Optional
from pathlib import Path
import os
from core.search_problem import SearchProblem
from problems.maze_state import MazeState


class MazeProblem(SearchProblem):
    """
    Maze navigation problem.
    Find path from entry (2) to exit (3).
    Maze is read from a text file with markers.
    """

    # Cell type constants
    PATH = 0
    WALL = 1
    ENTRY = 2
    EXIT = 3

    def __init__(self, maze_file: Optional[str] = None):
        """
        Initialize maze problem from file.

        Args:
            maze_file: Path to maze text file. If None, uses default.
        """
        if maze_file is None:
            # Use default maze file
            default_path = Path(__file__).parent.parent / "mazes" / "default_maze.txt"
            maze_file = str(default_path)

        self.maze, self.rows, self.cols, self.entry, self.exit = self._read_maze_from_file(maze_file)

        # Validate maze has entry and exit
        if self.entry is None:
            raise ValueError(f"Maze file {maze_file} has no entry marker (2)")
        if self.exit is None:
            raise ValueError(f"Maze file {maze_file} has no exit marker (3)")

    def _read_maze_from_file(self, filepath: str) -> Tuple[List[List[int]], int, int, Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
        """
        Read maze from text file.

        File format:
            First line: rows cols
            Following lines: rows x cols grid of:
                0 = path
                1 = wall
                2 = entry (exactly one)
                3 = exit (exactly one)

        Returns:
            Tuple of (maze grid, rows, cols, entry_coords, exit_coords)
        """
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()

            # Remove empty lines and strip whitespace
            lines = [line.strip() for line in lines if line.strip()]

            if not lines:
                raise ValueError(f"File {filepath} is empty")

            # First line: dimensions
            first_line = lines[0].split()
            if len(first_line) != 2:
                raise ValueError(f"First line must contain 'rows cols', got: {first_line}")

            rows, cols = map(int, first_line)

            # Read maze grid
            maze = []
            entry = None
            exit_pos = None

            for i in range(1, rows + 1):
                if i >= len(lines):
                    raise ValueError(f"Expected {rows} rows, but only found {i - 1}")

                row_line = lines[i].split()
                if len(row_line) != cols:
                    raise ValueError(f"Row {i} has {len(row_line)} values, expected {cols}")

                row = []
                for j, val_str in enumerate(row_line):
                    val = int(val_str)
                    if val not in [self.PATH, self.WALL, self.ENTRY, self.EXIT]:
                        raise ValueError(f"Row {i}, col {j} has invalid value {val}. Use 0,1,2,3")

                    if val == self.ENTRY:
                        if entry is not None:
                            raise ValueError(
                                f"Multiple entry markers found! First at {entry}, second at ({i - 1}, {j})")
                        entry = (i - 1, j)
                        val = self.PATH  # Convert to path for navigation
                    elif val == self.EXIT:
                        if exit_pos is not None:
                            raise ValueError(
                                f"Multiple exit markers found! First at {exit_pos}, second at ({i - 1}, {j})")
                        exit_pos = (i - 1, j)
                        val = self.PATH  # Convert to path for navigation

                    row.append(val)

                maze.append(row)

            print(f"✅ Loaded maze from {filepath}")
            print(f"   Dimensions: {rows}x{cols}")
            print(f"   Entry: {entry}")
            print(f"   Exit: {exit_pos}")

            # Count cell types for debugging
            path_count = sum(row.count(self.PATH) for row in maze)
            wall_count = sum(row.count(self.WALL) for row in maze)
            print(f"   Path cells: {path_count}, Wall cells: {wall_count}")

            return maze, rows, cols, entry, exit_pos

        except FileNotFoundError:
            print(f"❌ File not found: {filepath}")
            raise
        except Exception as e:
            print(f"❌ Error reading maze file: {e}")
            raise

    def get_initial_state(self) -> MazeState:
        """Return entry position."""
        return MazeState(self.entry[0], self.entry[1])

    def is_goal(self, state: MazeState) -> bool:
        """Check if we've reached the exit."""
        return state.row == self.exit[0] and state.col == self.exit[1]

    def get_successors(self, state: MazeState) -> List[Tuple[MazeState, str]]:
        """
        Generate all possible next states from current position.
        Movements: up, down, left, right (if not a wall).
        """
        successors = []
        row, col = state.row, state.col

        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dr, dc, action in moves:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.maze[new_row][new_col] != self.WALL:  # Not a wall
                    new_state = MazeState(new_row, new_col)
                    successors.append((new_state, action))

        return successors

    def heuristic(self, state: MazeState) -> float:
        """
        Heuristic function: estimates distance by Euclidean distance to exit.
        """
        return ((state.row - self.exit[0]) ** 2 + (state.col - self.exit[1]) ** 2) ** 0.5

    def print_maze(self, path: Optional[List[Tuple[MazeState, str]]] = None):
        """
        Pretty print the maze with optional solution path.
        """
        # Create a copy for display
        display = [row[:] for row in self.maze]

        # Mark the path if provided
        if path:
            for state, _ in path:
                if (state.row, state.col) != self.entry and \
                        (state.row, state.col) != self.exit:
                    display[state.row][state.col] = 4  # Path marker

        # Print the maze
        print("\n" + "=" * (self.cols * 2 + 4))
        print(f"MAZE ({self.rows}x{self.cols})")
        print("=" * (self.cols * 2 + 4))

        for row in range(self.rows):
            line = ""
            for col in range(self.cols):
                if (row, col) == self.entry:
                    line += "E"  # Entry
                elif (row, col) == self.exit:
                    line += "X"  # Exit
                elif display[row][col] == self.WALL:
                    line += "█"  # Wall
                elif display[row][col] == 4:
                    line += "·"  # Path
                elif display[row][col] == self.PATH:
                    line += " "  # Open space
                else:
                    line += "?"  # Unknown
                # line += " "
            print(line)

        print("=" * (self.cols * 2 + 4))
        print("Legend: E=Entry X=Exit █=Wall ·=Path")
