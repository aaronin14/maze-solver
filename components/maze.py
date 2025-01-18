import time
import random
from components.cell import Cell


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            maze_graphic=None,
            seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._maze_graphic = maze_graphic
        self._generating_speed = 0.01
        self._solving_speed = 0.07
        if seed:
            random.seed(seed)

    def generate_maze(self):
        self._create_cells()
        self._mark_entrance_and_exit()
        # Break walls randomly to create the maze
        break_wall_x = random.randrange(0,self._num_cols)
        break_wall_y = random.randrange(0,self._num_rows)
        self._break_walls_r(break_wall_x, break_wall_y)
        # Reset visited property to reuse
        self._reset_cells_visited()


    def _create_cells(self):
        # Create cells matrix
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._maze_graphic))
            self._cells.append(col_cells)
        # Draw cells
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._maze_graphic is None:
            return
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(self._generating_speed)

    def _animate(self, speed):
        if self._maze_graphic is None:
            return
        self._maze_graphic.redraw()
        time.sleep(speed)

    def _mark_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].fill_cell("red")
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].fill_cell("blue")
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Adjacent Left
            if i != 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            # Adjacent Right
            if i != self._num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            # Adjacent Top
            if j != 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            # Adjacent Bottom
            if j != self._num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))

            # Return if there is no Adjacent cells left to visit
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            # Choose the next cell
            next_cell_index = random.choice(to_visit)
            x = next_cell_index[0]
            y = next_cell_index[1]

            # Find the correct wall to break
            # The position of the next cell
            # right
            if i < x:
                self._cells[i][j].has_right_wall = False
                self._cells[x][y].has_left_wall = False
            # left
            if i > x:
                self._cells[i][j].has_left_wall = False
                self._cells[x][y].has_right_wall = False
            # bottom
            if j < y:
                self._cells[i][j].has_bottom_wall = False
                self._cells[x][y].has_top_wall = False
            # top
            if j > y:
                self._cells[i][j].has_top_wall = False
                self._cells[x][y].has_bottom_wall = False

            # Recursively visit the next cell
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    # Depth-first Search
    def _solve_r(self, i, j):
        self._animate(self._solving_speed)

        # Visit the current cell
        self._cells[i][j].visited = True

        # if the current cell is the end cell
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True

        # Check directions
        # left
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], True)

        # right
        if (
            i < self._num_cols-1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # top
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # bottom
        if (
            j < self._num_rows-1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], True)

        # Wrong direction
        return False

