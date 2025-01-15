import unittest
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()
