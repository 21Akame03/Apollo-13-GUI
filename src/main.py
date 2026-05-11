import sys

import pygame

import lm_draw
import terminal

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("LM-7 VECTOR DISPLAY")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Menlo", 18)
CW, CH = font.size("A")


def fit_169(w, h):
    if w * 9 > h * 16:
        w = h * 16 // 9
    else:
        h = w * 9 // 16
    return w, h


def layout():
    cols = WIDTH // CW
    rows = HEIGHT // CH
    ox = (WIDTH - cols * CW) // 2
    oy = (HEIGHT - rows * CH) // 2
    return cols, rows, ox, oy


COLS, ROWS, OX, OY = layout()
content = [
    "APOLLO 13  ──  LM AQUARIUS",
    "━" * 46,
    "SYSTEMS STATUS             [MISSION DAY 3]",
    "",
    "  CABIN PRESSURE  ...........  4.7  PSI  ",
    "  O2 REMAINING   ...........  12.4   %  ",
    "  CO2 LEVEL      ...........   8.2 MMHG  ",
    "  BATTERY A      ...........  38.0  AMP  ",
    "  BATTERY B      ...........  11.2  AMP  ",
    "  WATER SUPPLY   ...........  82.0   %  ",
    "",
    "",
]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = fit_169(event.w, event.h)
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            COLS, ROWS, OX, OY = layout()

    cx, cy = int(WIDTH * 0.7), HEIGHT // 2

    # Draw Cabin

    screen.fill((0, 0, 0))
    terminal.draw_border(screen, font, OX, OY, cols=COLS, rows=ROWS, title="LM-13")
    terminal.draw_content(screen, font, OX, OY, cols=COLS, lines=content)
    lm_draw.draw_lm(screen, cx, cy)

    pygame.display.flip()
    clock.tick(60)
