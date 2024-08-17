from window import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0,0), Point(600, 800)))
    win.draw_line(Line(Point(50, 50), Point(100, 50)))
    win.wait_for_close()

main()