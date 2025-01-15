from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self._win = win
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Left Wall
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        left_color = "black"
        if self.has_left_wall is False:
            left_color = "white"
        self._win.draw_line(left_wall, left_color)

        # Right Wall
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        right_color = "black"
        if self.has_right_wall is False:
            right_color = "white"
        self._win.draw_line(right_wall, right_color)

        # Top Wall
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        top_color = "black"
        if self.has_top_wall is False:
            top_color = "white"
        self._win.draw_line(top_wall, top_color)

        # Bottom Wall
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        bottom_color = "black"
        if self.has_bottom_wall is False:
            bottom_color = "white"
        self._win.draw_line(bottom_wall, bottom_color)

    def drawable(self):
        return not (self._x1 is None or self._x2 is None or self._y1 is None or self._y2 is None)

    def draw_move(self, to_cell, undo=False):
        if not self.drawable() or not to_cell.drawable():
            return

        # Find center points
        p1 = Point((self._x1 + self._x2)/2, (self._y1+self._y2)/2)
        p2 = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)

        # Draw Line
        line = Line(p1, p2)
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)
