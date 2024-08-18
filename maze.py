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
