from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width):
        self.root = Tk()
        self.root.title("Maze solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_color,
            width=2
        )

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0,0), Point(600, 800)))
    win.draw_line(Line(Point(50, 50), Point(100, 50)))
    win.wait_for_close()

main()