from queue import PriorityQueue
import random
import time
from components.cell import Cell


class Maze:
    def __init__(
            self,
            width=800,
            height=800,
            margin=25,
            rows=15,
            cols=15,
            maze_graphic=None,
            seed=None,
    ):
        self._cells = []
        self._path = {}
        self._width = width
        self._height = height
        self._margin = margin
        self._rows = rows
        self._cols = cols
        self._cell_width = (width - margin * 2) / cols
        self._cell_height = (height - margin * 2) / rows
        self._maze_graphic = maze_graphic
        self._speed = 1/(51)
        self._generated = False
        self._solved = False
        if seed:
            random.seed(seed)

    def generate_maze(self):
        if not self._generated:
            self._create_cells()
            self._mark_entrance_and_exit()
            # Break walls randomly to create the maze
            break_wall_x = random.randrange(0,self._cols)
            break_wall_y = random.randrange(0,self._rows)
            self._break_walls_r(break_wall_x, break_wall_y)
            # Reset visited property to reuse
            self._generated = True
            self._reset_cells_visited()

    def set_rows(self, rows):
        self._rows = rows
        self._cell_height = (self._width - self._margin * 2) / rows

    def set_cols(self, cols):
        self._cols = cols
        self._cell_width = (self._height - self._margin * 2) / cols

    def set_speed(self, speed):
        self._speed = speed

    def solve(self, algorithm="DFS"):
        if not self._solved:
            self._solved = True
            if algorithm == "BFS":
                return self._bfs()
            elif algorithm == "A*":
                return self._a_star()
            else:
                return self._dfs_r(0, 0)

    def clear(self):
        self._generated = False
        self._solved = False
        self._maze_graphic.clear_canvas()
        self._cells = []
        self._margin = 25
        self._rows = 15
        self._cols = 15
        self._cell_width = (self._width - self._margin * 2) / self._cols
        self._cell_height = (self._height - self._margin * 2) / self._rows

    def reset(self):
        self._solved = False
        self._cells = []
        # TODO: remove draw_move() only

    def _create_cells(self):
        # Create cells matrix
        for i in range(self._cols):
            col_cells = []
            for j in range(self._rows):
                col_cells.append(Cell(self._maze_graphic))
            self._cells.append(col_cells)
        # Draw cells
        for i in range(self._cols):
            for j in range(self._rows):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._maze_graphic is None:
            return
        x1 = self._margin + self._cell_width * i
        y1 = self._margin + self._cell_height * j
        x2 = x1 + self._cell_width
        y2 = y1 + self._cell_height
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(self._speed)

    def _animate(self, speed):
        if self._maze_graphic is None:
            return
        self._maze_graphic.redraw()
        time.sleep(speed)

    def _mark_entrance_and_exit(self):
        self._cells[0][0].fill_cell("red")
        self._draw_cell(0, 0)
        self._cells[self._cols - 1][self._rows - 1].fill_cell("blue")
        self._draw_cell(self._cols - 1, self._rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Adjacent Left
            if i != 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            # Adjacent Right
            if i != self._cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            # Adjacent Top
            if j != 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            # Adjacent Bottom
            if j != self._rows-1 and not self._cells[i][j+1].visited:
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

    # Depth-first Search
    def _dfs_r(self, i, j):
        self._animate(self._speed)
        # Visit the current cell
        self._cells[i][j].visited = True
        # Check if the current cell is the end cell
        if i == self._cols-1 and j == self._rows-1:
            return True
        # Check for next available cell
        # left
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._dfs_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], "green")

        # right
        if (
            i < self._cols-1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._dfs_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], "green")

        # top
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._dfs_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], "green")

        # bottom
        if (
            j < self._rows-1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._dfs_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], "green")

        # Wrong direction
        return False

    # Breadth-First Search
    def _bfs(self):
        to_visit = []
        return self._bfs_r(0, 0, to_visit)

    def _bfs_r(self, i, j, to_visit):
        self._animate(self._speed)
        # Visit the current cell
        self._cells[i][j].visited = True
        # Check if the current cell is the end cell
        if i == self._cols-1 and j == self._rows-1:
            return True
        # Check for next available cell
        # left
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            to_visit.append((i-1,j))
        # right
        if (
            i < self._cols-1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            to_visit.append((i+1,j))
        # top
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            to_visit.append((i,j-1))
        # bottom
        if (
            j < self._rows-1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            to_visit.append((i,j+1))

        next_cell = to_visit.pop(0)
        next_i = next_cell[0]
        next_j = next_cell[1]
        self._bfs_r(next_i, next_j, to_visit)

        # Wrong direction
        if not to_visit:
            return False

    # A* Search Algorithm
    # Manhattan distance Heuristic
    def _heuristic(self, x1, y1):
        x2 = self._cols-1
        y2 = self._rows-1
        return abs(x1-x2) + abs(y1-y2)

    def _a_star(self):
        g_scores = {}
        f_scores = {}
        for i in range(self._cols):
            for j in range(self._rows):
                g_scores[(i,j)] = float('inf')
                f_scores[(i,j)] = float('inf')
                g_scores[0,0] = 0
                f_scores[0,0] = self._heuristic(0,0)

        fringe = PriorityQueue()
        fringe.put((f_scores[0,0],  self._heuristic(0,0), (0, 0)))

        while not fringe.empty():
            self._animate(self._speed)
            current = fringe.get()[2]
            i, j = current
            # Visit the current cell
            self._cells[i][j].visited = True
            # Check if the current cell is the end cell
            if i == self._cols-1 and j == self._rows-1:
                self._back_track()
                return True
            # Check for next available cell
            # left
            if (
                i > 0
                and not self._cells[i][j].has_left_wall
                and not self._cells[i-1][j].visited
            ):
                self._a_star_helper(i, j, i-1, j, fringe, g_scores, f_scores)

            # right
            if (
                i < self._cols-1
                and not self._cells[i][j].has_right_wall
                and not self._cells[i+1][j].visited
            ):
                self._a_star_helper(i, j, i+1, j, fringe, g_scores, f_scores)

            # top
            if (
                j > 0
                and not self._cells[i][j].has_top_wall
                and not self._cells[i][j-1].visited
            ):
                self._a_star_helper(i, j, i, j-1, fringe, g_scores, f_scores)

            # bottom
            if (
                j < self._rows-1
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[i][j+1].visited
            ):
                self._a_star_helper(i, j, i, j+1, fringe, g_scores, f_scores)

        # Wrong direction
        return False

    def _a_star_helper(self, i, j, ci, cj, fringe, g_scores, f_scores):
        self._cells[ci][cj].visited = True
        temp_g_score = g_scores[(i,j)] + 1
        temp_h_score = self._heuristic(ci, cj)
        temp_f_score = temp_g_score + temp_h_score

        if temp_f_score < g_scores[(ci,cj)]:
            g_scores[(ci,cj)] = temp_g_score
            f_scores[(ci,cj)] = temp_f_score
            fringe.put((temp_f_score, temp_h_score, (ci, cj)))
            self._cells[i][j].draw_move(self._cells[ci][cj])
            self._path[(ci,cj)] = (i,j)

    def _back_track(self):
        x1 = self._cols-1
        y1 = self._rows-1
        while self._path[(x1, y1)] is not None:
            self._animate(self._speed)
            x2 , y2 = self._path[(x1, y1)]
            self._cells[x1][y1].draw_move(self._cells[x2][y2], "green")
            x1 = x2
            y1 = y2
