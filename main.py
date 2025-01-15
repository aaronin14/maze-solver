from graphics import Window
from maze import Maze


def main():

    screen_width = 800
    screen_height = 600
    num_rows = 10
    num_cols = 10
    margin = 50
    cell_size_x = (screen_width - margin * 2) / num_cols
    cell_size_y = (screen_height - margin * 2) / num_rows

    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)


    win.wait_for_close()


main()
