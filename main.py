from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    l1 = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l1, "black")
    win.wait_for_close()


main()
