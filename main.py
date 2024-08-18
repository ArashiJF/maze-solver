from window import Window, Line, Point
from maze import Cell

def main():
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
    win.wait_for_close()

main()