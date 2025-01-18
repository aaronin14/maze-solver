import tkinter as tk
from components.ui import Settings
from components.graphics import MazeGraphic
from components.maze import Maze


def main():
    # Maze Configuration
    maze_w = 600
    maze_h = 600
    margin = 30
    num_rows = 20
    num_cols = 20
    cell_size_x = (maze_w - margin * 2) / num_cols
    cell_size_y = (maze_h - margin * 2) / num_rows

    root = tk.Tk()
    root.title("Maze Solver")
    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0)
    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1)

    maze_graphic = MazeGraphic(root, left_frame, maze_w, maze_h)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, maze_graphic)
    settings = Settings(right_frame, maze)
    maze_graphic.wait_for_close()


main()
