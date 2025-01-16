from graphics import Window
from maze import Maze


def main():

    screen_width = 600
    screen_height = 600
    num_rows = 18
    num_cols = 18
    margin = 30
    cell_size_x = (screen_width - margin * 2) / num_cols
    cell_size_y = (screen_height - margin * 2) / num_rows

    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 1)


    win.wait_for_close()


main()
