CYAN = (0, 170, 170)
BLACK = (0, 0, 0)


def text(surf, font, x, y, s, fg=CYAN, bg=None):
    surf.blit(font.render(s, True, fg, bg), (x, y))


def draw_border(surf, font, x, y, cols, rows, title=""):
    cw, ch = font.size("A")
    header = f"  LM-7 VECTOR DISPLAY{title.center(cols - 32)}Modified  "
    text(surf, font, x, y, header[:cols].ljust(cols), BLACK, CYAN)

    inner = cols - 2
    label = f"╡ {title} ╞"
    pad = (inner - len(label)) // 2
    text(surf, font, x, y + ch, "╔" + "═" * pad + label + "═" * (inner - len(label) - pad) + "╗")
    for r in range(2, rows - 1):
        text(surf, font, x, y + r * ch, "║" + " " * inner + "║")
    text(surf, font, x, y + (rows - 1) * ch, "╚" + "═" * inner + "╝")


def draw_content(surf, font, x, y, cols, lines):
    cw, ch = font.size("A")
    for i, line in enumerate(lines):
        text(surf, font, x + 2 * cw, y + (i + 2) * ch, line[: cols - 4])
