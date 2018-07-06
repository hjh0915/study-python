import turtle
import time

def draw_square():
    t = turtle.Pen()
    t.forward(100)
    t.left(300)
    t.right(300)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

    time.sleep(10)

if __name__ == '__main__':
    draw_square()