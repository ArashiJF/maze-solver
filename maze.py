import time

from window import Line, Point

class Cell:
    def __init__(self, point_a, point_b, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.point_a = point_a
        self.point_b = point_b
        self.win = window

    def draw_left_wall(self):
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
            )
        )

    def draw_top_wall(self):
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
            )
        )

    def draw_right_wall(self):
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
            )
        )

    def draw_bottom_wall(self):
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
            )
        )

    def draw(self):
        if self.has_left_wall: self.draw_left_wall()
        if self.has_top_wall: self.draw_top_wall()
        if self.has_right_wall: self.draw_right_wall()
        if self.has_bottom_wall: self.draw_bottom_wall()

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_clor = "gray"

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
        win
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()

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

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
