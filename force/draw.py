import turtle
from collections.abc import Sequence
from functools import reduce
from math import dist
from turtle import goto as _goto, seth, forward, left, backward, right, penup, pendown, pencolor, \
    pos, exitonclick, hideturtle, colormode

from .color import FORCE, CALC, RES, RESRES
from .force import Force
from .utils import all_equal, get_angle


def par(forces: Sequence[Force]) -> Force:
    assert all_equal(force.poe for force in forces)
    poe = forces[0].poe
    draw_forces(forces)
    goto(*poe)
    force = reduce(single_par, forces)
    pencolor(RESRES)
    goto(*poe)
    draw_force(force)
    return force


def single_par(a: Force, b: Force) -> Force:
    pencolor(CALC)
    goto(*a.poe)
    goto_force(a)
    draw_force(b)
    goto(*b.poe)
    goto_force(b)
    draw_force(a)
    return poe_pos(a.poe)


def htt(forces: Sequence[Force]) -> Force:
    assert all_equal(force.poe for force in forces)
    poe = forces[0].poe
    draw_forces(forces)

    pencolor(CALC)
    goto(*poe)
    for force in forces:
        draw_force(force)

    return poe_pos(poe, RESRES)


def poe_pos(poe, color=RES) -> Force:
    distance = dist(poe, pos())
    angle = get_angle(poe, pos())
    force = Force(distance, angle)
    goto(*poe)
    pencolor(color)
    draw_force(force)
    return force


def draw_forces(forces: Sequence[Force]) -> None:
    pencolor(FORCE)
    for force in forces:
        goto(*force.poe)
        draw_force(force)


def draw_force(force: Force) -> None:
    seth(force.direction)
    forward(force.size)
    draw_arrowh()


def draw_arrowh(size: float = 20, angle: float = 45) -> None:
    left(angle)
    backward(size)
    forward(size)
    right(angle * 2)
    backward(size)
    forward(size)


def goto_force(force: Force) -> None:
    penup()
    draw_force(force)
    pendown()


def goto(x: float, y: float) -> None:
    penup()
    _goto(x, y)
    pendown()


def setup(speed: float, gpp: bool, gpp_size: float) -> None:
    colormode(255)
    turtle.speed(0)
    if gpp:
        draw_gpp(gpp_size)
    turtle.speed(speed)


def shutdown() -> None:
    hideturtle()
    exitonclick()


def draw_gpp(size: float, end: float = 300) -> None:
    goto(-end, end)
    single_gpp(size, end)
    goto(-end, -end)
    seth(90)
    single_gpp(size, end)


def single_gpp(size: float, end: float) -> None:
    for i in range(int(end // size)):
        forward(end * 2)
        right(90)
        forward(size)
        right(90)
        forward(end * 2)
        left(90)
        forward(size)
        left(90)
