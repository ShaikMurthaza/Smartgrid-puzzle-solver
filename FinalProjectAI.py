import random
import time
import matplotlib.pyplot as plt
import sys
from copy import deepcopy

class SudokuCSP:
    def __init__(self, n):
        self.n = n
        self.subgrid_size = int(n ** 0.5)
        self.variables = [(i, j) for i in range(n) for j in range(n)]
        self.domains = {variable: set(range(1, n + 1)) for variable in self.variables}
        self.constraints = self._get_constraints()

    def _get_constraints(self):
        constraints = []
        for i in range(self.n):
            for j in range(self.n):
                for k in range(j + 1, self.n):
                    constraints.append(((i, j), (i, k)))
                    constraints.append(((j, i), (k, i)))

        for i in range(0, self.n, self.subgrid_size):
            for j in range(0, self.n, self.subgrid_size):
                subgrid = [(i + r, j + c) for r in range(self.subgrid_size) for c in range(self.subgrid_size)]
                for u in subgrid:
                    for v in subgrid:
                        if u != v:
                            constraints.append((u, v))

        return constraints

    def solve(self, puzzle):
        assignments = {(i, j): puzzle[i][j] for i in range(self.n) for j in range(self.n) if puzzle[i][j] != 0}
        return self._backtracking_search(assignments)

    def _backtracking_search(self, assignments):
        if self._is_complete(assignments):
            return assignments

        var = self._select_unassigned_variable(assignments)
        for value in self._order_domain_values(var, assignments):
            if self._is_consistent(var, value, assignments):
                assignments[var] = value
                result = self._backtracking_search(assignments)
                if result is not None:
                    return result
                del assignments[var]
        return None

    def _is_complete(self, assignments):
        return all(assignments.get(var) is not None for var in self.variables)

    def _select_unassigned_variable(self, assignments):
        unassigned = [var for var in self.variables if var not in assignments]
        return min(unassigned, key=lambda var: len(self.domains[var]))

    def _order_domain_values(self, var, assignments):
        return sorted(self.domains[var], key=lambda value: self._count_conflicts(var, value, assignments))

    def _count_conflicts(self, var, value, assignments):
        count = 0
        for neighbor in self.variables:
            if neighbor != var and neighbor in assignments and assignments[neighbor] == value:
                count += 1
        return count

    def _is_consistent(self, var, value, assignments):
        for neighbor in self.variables:
            if neighbor != var and neighbor in assignments and assignments[neighbor] == value:
                return False
        return True

def choose_difficulty():
    print("Select the difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        try:
            choice = int(input("Enter the number corresponding to the desired difficulty level (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_sudoku_puzzle_with_difficulty(n, difficulty_level):
    puzzle = SudokuCSP(n)
    solved = puzzle.solve([[0] * n for _ in range(n)])
    remove_count = 0
    if difficulty_level == 1:
        remove_count = int(0.4 * n * n)
    elif difficulty_level == 2:
        remove_count = int(0.5 * n * n)
    elif difficulty_level == 3:
        remove_count = int(0.7 * n * n)

    for _ in range(remove_count):
        while True:
            row = random.randint(0, n - 1)
            col = random.randint(0, n - 1)
            if solved[(row, col)] != 0:
                solved[(row, col)] = 0
                break

    return [[solved[(i, j)] for j in range(n)] for i in range(n)]

def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def visualize_metrics(metrics_backtracking, solver_name):
    labels = ['Recursive Calls', 'Backtracks', 'Max Depth']
    sizes_backtracking = [metrics_backtracking['recursive_calls'], metrics_backtracking['backtracks'], metrics_backtracking['max_depth']]
    fig, ax = plt.subplots()
    ax.pie(sizes_backtracking, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(f'{solver_name} - Metrics Distribution')
    plt.show()

def solve_and_measure_time(grid, n, solver_name):
    start_time = time.time()
    puzzle = SudokuCSP(n)
    solved = puzzle.solve(grid)
    end_time = time.time()

    print(f"\n{solver_name} - Solved Sudoku Puzzle:")
    print_sudoku([[solved[(i, j)] for j in range(n)] for i in range(n)])
    print(f"\nTime taken to solve: {end_time - start_time:.4f} seconds")
    print(f"Number of Recursive Calls: {puzzle._recursive_calls}")
    print(f"Number of Backtracks: {puzzle._backtracks}")
    print(f"Max Depth: {puzzle._max_depth}")

    return {'recursive_calls': puzzle._recursive_calls, 'backtracks': puzzle._backtracks, 'max_depth': puzzle._max_depth}

if __name__ == "__main__":
    solver_name = 'Constraint Satisfaction Problem (CSP)'

    try:
        n = int(input("Enter the size of the Sudoku grid (e.g., 4 for 4x4, 9 for 9x9): "))
        if n <= 0 or (int(n**0.5))**2 != n:
            print("Please enter a positive square number.")
            sys.exit()

        difficulty_level = choose_difficulty()

        puzzle = generate_sudoku_puzzle_with_difficulty(n, difficulty_level)

        print("\nGenerated Sudoku Puzzle:")
        print_sudoku(puzzle)

        metrics_csp = solve_and_measure_time(puzzle, n, solver_name)

        # Visualize metrics
        visualize_metrics(metrics_csp, solver_name)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
