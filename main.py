from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    #c.has_left_wall = False
    #c.has_right_wall = False
    #c.has_top_wall = False
    #c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)

    win.wait_for_close()


main()
