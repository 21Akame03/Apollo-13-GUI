import math

import pygame

GREEN = (51, 255, 102)
DIM = (26, 136, 170)
FAINT = (13, 64, 26)
CYAN = (0, 170, 170)


def line(surf, x1, y1, x2, y2, color=CYAN, w=1):
    pygame.draw.line(surf, color, (x1, y1), (x2, y2), w)


def draw_probe(surf, cx, cy):
    line(surf, cx, cy - 198, cx, cy - 168)
    line(surf, cx - 5, cy - 198, cx + 5, cy - 198)
    line(surf, cx - 3, cy - 180, cx + 3, cy - 180, DIM)


def draw_dome(surf, cx, cy):
    line(surf, cx - 14, cy - 168, cx + 14, cy - 168)
    line(surf, cx - 14, cy - 168, cx - 35, cy - 152)
    line(surf, cx + 14, cy - 168, cx + 35, cy - 152)


def draw_cabin(surf, cx, cy):
    line(surf, cx - 35, cy - 152, cx + 35, cy - 152)
    line(surf, cx - 35, cy - 152, cx - 35, cy - 80)
    line(surf, cx + 35, cy - 152, cx + 35, cy - 80)
    line(surf, cx - 35, cy - 80, cx + 35, cy - 80)
    line(surf, cx - 10, cy - 80, cx + 10, cy - 80, DIM)  # hatch hint
    line(surf, cx - 35, cy - 136, cx - 46, cy - 136, DIM)  # rear bay
    line(surf, cx - 35, cy - 112, cx - 46, cy - 112, DIM)
    line(surf, cx - 46, cy - 136, cx - 46, cy - 112, DIM)


def draw_window(surf, cx, cy):
    line(surf, cx - 18, cy - 144, cx + 18, cy - 144)
    line(surf, cx - 18, cy - 112, cx + 18, cy - 112)
    line(surf, cx - 18, cy - 144, cx - 18, cy - 112)
    line(surf, cx + 18, cy - 144, cx + 18, cy - 112)
    line(surf, cx, cy - 144, cx, cy - 112, DIM)


def draw_descent_stage(surf, cx, cy):
    line(surf, cx - 125, cy - 80, cx + 125, cy - 80)
    line(surf, cx - 125, cy - 80, cx - 125, cy + 70)
    line(surf, cx + 125, cy - 80, cx + 125, cy + 70)
    line(surf, cx - 125, cy + 70, cx + 125, cy + 70)
    line(surf, cx - 42, cy - 80, cx - 42, cy + 70, DIM)
    line(surf, cx + 42, cy - 80, cx + 42, cy + 70, DIM)
    line(surf, cx - 125, cy - 5, cx + 125, cy - 5, DIM)


def draw_ladder(surf, cx, cy):
    line(surf, cx - 8, cy + 70, cx - 8, cy + 180)
    line(surf, cx + 8, cy + 70, cx + 8, cy + 180)
    for i in range(8):
        ry = cy + 84 + i * 14
        line(surf, cx - 8, ry, cx + 8, ry, DIM)


def draw_engine(surf, cx, cy):
    line(surf, cx - 22, cy + 70, cx + 22, cy + 70)
    line(surf, cx - 22, cy + 70, cx - 40, cy + 138)
    line(surf, cx + 22, cy + 70, cx + 40, cy + 138)
    line(surf, cx - 40, cy + 138, cx + 40, cy + 138)
    line(surf, cx - 12, cy + 70, cx - 12, cy + 88, DIM)
    line(surf, cx + 12, cy + 70, cx + 12, cy + 88, DIM)
    line(surf, cx - 12, cy + 88, cx + 12, cy + 88, DIM)


def draw_legs(surf, cx, cy):
    jy = cy - 5  # joint at mid-height of descent stage

    pygame.draw.circle(surf, CYAN, (cx - 125, jy), 4)
    line(surf, cx - 125, jy, cx - 210, cy + 154)  # primary strut
    line(surf, cx - 125, jy, cx - 162, cy + 154)  # secondary strut
    line(surf, cx - 125, cy - 80, cx - 151, cy + 40, DIM)  # diagonal brace
    line(surf, cx - 228, cy + 154, cx - 144, cy + 154)  # footpad
    pygame.draw.circle(surf, CYAN, (cx - 228, cy + 154), 3)
    pygame.draw.circle(surf, CYAN, (cx - 144, cy + 154), 3)

    pygame.draw.circle(surf, CYAN, (cx + 125, jy), 4)
    line(surf, cx + 125, jy, cx + 210, cy + 154)
    line(surf, cx + 125, jy, cx + 162, cy + 154)
    line(surf, cx + 125, cy - 80, cx + 151, cy + 40, DIM)
    line(surf, cx + 144, cy + 154, cx + 228, cy + 154)
    pygame.draw.circle(surf, CYAN, (cx + 144, cy + 154), 3)
    pygame.draw.circle(surf, CYAN, (cx + 228, cy + 154), 3)


def draw_antenna(surf, cx, cy):
    line(surf, cx + 35, cy - 138, cx + 62, cy - 156)  # arm
    line(surf, cx + 62, cy - 156, cx + 55, cy - 168)  # dish left
    line(surf, cx + 62, cy - 156, cx + 69, cy - 167)  # dish right
    line(surf, cx + 55, cy - 168, cx + 69, cy - 167)  # dish rim
    line(surf, cx - 20, cy - 152, cx - 28, cy - 168, DIM)  # VHF stub left
    line(surf, cx + 20, cy - 152, cx + 28, cy - 168, DIM)  # VHF stub right


def draw_plume(surf, cx, cy):
    line(surf, cx, cy + 138, cx, cy + 175, FAINT)
    line(surf, cx, cy + 138, cx - 16, cy + 170, FAINT)
    line(surf, cx, cy + 138, cx + 16, cy + 170, FAINT)
    line(surf, cx, cy + 138, cx - 28, cy + 163, FAINT)
    line(surf, cx, cy + 138, cx + 28, cy + 163, FAINT)


def draw_lm(surf, cx, cy):
    draw_legs(surf, cx, cy)
    draw_engine(surf, cx, cy)
    draw_descent_stage(surf, cx, cy)
    draw_cabin(surf, cx, cy)
    draw_window(surf, cx, cy)
    draw_dome(surf, cx, cy)
    draw_probe(surf, cx, cy)
    draw_antenna(surf, cx, cy)
