import tkinter as tk
from tkinter import messagebox

# Backtracking algorithm to solve Sudoku
def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0  # Backtrack if no solution
                return False
    return True

def is_safe(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# GUI for Sudoku Solver
class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        
        # Create a 9x9 grid for the Sudoku board
        self.grid = [[tk.Entry(root, width=5, font=('Arial', 18), borderwidth=2, relief="solid") for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.grid[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.solve_button = tk.Button(root, text="Solve", font=('Arial', 14), command=self.solve)
        self.solve_button.grid(row=9, column=4, columnspan=2)

    def solve(self):
        board = [[0] * 9 for _ in range(9)]
        # Get values from the grid and fill the board
        for i in range(9):
            for j in range(9):
                val = self.grid[i][j].get()
                if val.isdigit():
                    board[i][j] = int(val)
                else:
                    board[i][j] = 0

        # Solve the Sudoku
        if solve_sudoku(board):
            # If solution is found, display it on the grid
            for i in range(9):
                for j in range(9):
                    self.grid[i][j].delete(0, tk.END)
                    self.grid[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showinfo("No Solution", "This Sudoku puzzle has no solution!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()