import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_dimensions(self):
        num_cols = 10
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        first_row = maze.cells[0]
        first_cell = first_row[0]

        self.assertEqual(
            first_cell.point_a.x,
            0
        )
        self.assertEqual(
            first_cell.point_a.y,
            0
        )
        self.assertEqual(
            first_cell.point_b.x,
            10
        )
        self.assertEqual(
            first_cell.point_b.y,
            10
        )

        last_row = maze.cells[9]
        last_cell = last_row[-1]

        self.assertEqual(
            last_cell.point_a.x,
            90
        )
        self.assertEqual(
            last_cell.point_a.y,
            90
        )
        self.assertEqual(
            last_cell.point_b.x,
            100
        )
        self.assertEqual(
            last_cell.point_b.y,
            100
        )

if __name__ == "__main__":
    unittest.main()
