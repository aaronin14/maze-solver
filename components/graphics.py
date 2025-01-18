import tkinter as tk


class MazeGraphic:
    def __init__(self, root, frame, maze_w, maze_h):
        self.__root = root
        self.__frame = frame
        self.__canvas = tk.Canvas(self.__frame, width=maze_w, height=maze_h, bg="#18191a")
        self.__canvas.grid(row=0, column=0)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__frame.update_idletasks()
        self.__frame.update()

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def fill_rectangle(self, rec, fill_color="red"):
        rec.fill(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="white"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def fill(self, canvas, fill_color="red"):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=0)
