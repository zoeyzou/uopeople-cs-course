import turtle
import math

bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, length, n):
    angle = 360 / n
    polyline(t, length, n, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, step_length, n, step_angle)


def circle(t, r):
    arc(t, r, 360)


def petal(t, r, angle):
    """ draws a petal using 2 arcs
    t: Turtle
    r: radius of the arcs
    angle: degree of the arc
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    """ Draws a flower with n petals
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: degree of the arc
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360 / n)


def triangle(t, length, angle):
    """ Draws a triangle with a angle for the tip
    t: Turtle
    length: length of the equal edge
    angle: degree of the top
    """
    edge_length = length * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(length)
    t.lt(90 + angle)
    t.fd(2 * edge_length)
    t.lt(90 + angle)
    t.fd(length)
    t.lt(180 - angle)


def polypie(t, n, r):
    angle = 360 / n
    for i in range(n):
        triangle(t, r, angle / 2)
        t.lt(angle)


def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()


def move(t, length):
    """ Helper to move the turtle and move the pen up when moving
    """
    t.pu()
    t.fd(length)
    t.pd()


flower(bob, 20, 100, 20)

move(bob, 100)
flower(bob, 7, 50, 60)

move(bob, 100)
flower(bob, 10, 50, 80)

bob.lt(180)
move(bob, 200)
bob.lt(90)
move(bob, 200)
bob.lt(90)

draw_pie(bob, 5, 60)

move(bob, 100)
draw_pie(bob, 6, 60)

move(bob, 100)
draw_pie(bob, 7, 60)

turtle.mainloop()
