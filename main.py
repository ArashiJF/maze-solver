from window import Window, Line, Point
from maze import Maze, Cell

def test_cell_draw():
    win = Window(400, 400)
    cell_1 = Cell(
        Point(
            1,
            1
        ),
        Point(
            100,
            100
        ),
        win
    )
    cell_2 = Cell(
        Point(
            100,
            100
        ),
        Point(
            200,
            200
        ),
        win
    )
    cell_3 = Cell(
        Point(
            200,
            200
        ),
        Point(
            300,
            300
        ),
        win
    )
    cell_4 = Cell(
        Point(
            300,
            300
        ),
        Point(
            400,
            400
        ),
        win
    )
    cell_1.draw()
    cell_2.draw()
    cell_3.draw()
    cell_4.draw()

    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3)
    cell_3.draw_move(cell_4)
    win.wait_for_close()

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()

main()