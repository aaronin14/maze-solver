import tkinter as tk
from components.ui import UserInterface
from components.graphics import MazeGraphic
from components.maze import Maze


def main():
    # Default Maze Configuration
    maze_w = 800
    maze_h = 800
    margin = 25
    rows = 15
    cols = 15

    root = tk.Tk()
    root.title("Maze Solver")
    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0)
    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1)

    maze_graphic = MazeGraphic(root, left_frame, maze_w, maze_h)
    maze = Maze(maze_w, maze_h, margin, rows, cols, maze_graphic)
    ui = UserInterface(root, right_frame, maze, maze_graphic)
    maze_graphic.wait_for_close()


main()
