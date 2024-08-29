import time
from random import randint, seed as randseed
from window import Line, Point

class Cell:
    def __init__(self, point_a, point_b, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.point_a = point_a
        self.point_b = point_b
        self.win = window
        self.visited = None

    def draw_left_wall(self, fill_color="black"):
        self.win.draw_line(
            Line(
                Point(
                    self.point_a.x,
                    self.point_a.y
                ),
                Point(
                    self.point_a.x,
                    self.point_b.y
                )
            ),
            fill_color
        )

    def draw_top_wall(self, fill_color="black"):
        self.win.draw_line(
            Line(
                Point(
                    self.point_a.x,
                    self.point_a.y
                ),
                Point(
                    self.point_b.x,
                    self.point_a.y
                )
            ),
            fill_color
        )

    def draw_right_wall(self, fill_color="black"):
        self.win.draw_line(
            Line(
                Point(
                    self.point_b.x,
                    self.point_a.y
                ),
                Point(
                    self.point_b.x,
                    self.point_b.y
                )
            ),
            fill_color
        )

    def draw_bottom_wall(self, fill_color="black"):
        self.win.draw_line(
            Line(
                Point(
                    self.point_a.x,
                    self.point_b.y
                ),
                Point(
                    self.point_b.x,
                    self.point_b.y
                )
            ),
            fill_color
        )

    def draw(self):
        def invisible_line(has_wall):
            if has_wall is False:
                return "white"

        self.draw_left_wall(invisible_line(self.has_left_wall))
        self.draw_top_wall(invisible_line(self.has_top_wall))
        self.draw_right_wall(invisible_line(self.has_right_wall))
        self.draw_bottom_wall(invisible_line(self.has_bottom_wall))

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"

        self.win.draw_line(
            Line(
                Point(
                    (self.point_a.x + self.point_b.x) / 2,
                    (self.point_a.y + self.point_b.y) / 2
                ),
                Point(
                    (to_cell.point_a.x + to_cell.point_b.x) / 2,
                    (to_cell.point_a.y + to_cell.point_b.y) / 2
                )
            ),
            line_color
        )

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

        if seed:
            randseed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)

    def create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(self.build_cell(i,j))
            self.cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i,j)

    def draw_cell(self, i, j):
        if self.win is None:
            return
        self.cells[i][j].draw()
        self.animate()

    def build_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = Cell(
            Point(x1,y1),
            Point(x2,y2),
            self.win
        )
        # print(cell.point_a.x, cell.point_a.y, cell.point_b.x, cell.point_b.y)
        return cell

    def break_entrance_and_exit(self):
        def break_cell(i,j, exit = False):
            row = self.cells[i]
            cell = row[j]
            if exit:
                cell.has_bottom_wall = False
            else:
                cell.has_top_wall = False

            self.draw_cell(i,j)

        def break_cell_rand(self):
            # 1 means left or right walls
            # 2 means top or bottom wall
            if randint(1,2) == 1:
                if exit:
                    cell.has_right_wall = False
                else:    
                    cell.has_left_wall = False
            else:
                if exit:
                    cell.has_bottom_wall = False
                else:
                    cell.has_top_wall = False
            self.draw_cell(i,j)

        break_cell(0,0)
        break_cell(-1,-1, True)

    def break_walls_r(self, i, j):

        def is_visited(i, j):
            return self.cells[i][j].visited

        def break_wall(tar_i, tar_j):
            # left
            if tar_i == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[tar_i][j].has_right_wall = False
            # right
            if tar_i == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[tar_i][j].has_left_wall = False
            # top
            if tar_j == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][tar_j].has_bottom_wall = False
            # bottom
            if tar_j == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][tar_j].has_top_wall = False
                    
        self.cells[i][j].visited = True
        while True:
            remaining = []
            # check adjacent
            # left
            if i > 0 and not is_visited(i-1, j):
                remaining.append([i-1, j])
            # right
            if i + 1 < self.num_cols and not is_visited(i+1, j):
                remaining.append([i+1, j])
            # top
            if j > 0 and not is_visited(i, j-1):
                remaining.append([i, j-1])
            # bottom
            if j + 1 < self.num_rows and not is_visited(i, j+1):
                remaining.append([i, j+1])
            
            if len(remaining) == 0:
                self.draw_cell(i, j)
                return

            rand_dir = randint(0, len(remaining) - 1)
            next_index = remaining[rand_dir]
            break_wall(next_index[0], next_index[1])
            self.break_walls_r(next_index[0], next_index[1])

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
