from asciimatics.effects import Mirage, Wipe, Matrix
from asciimatics.particles import DropScreen
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

def credits(screen):
    effects = [
        Matrix(screen, stop_frame=200),
        Mirage(
            screen,
            FigletText("cdxppr"),
            screen.height // 2 - 3,
            Screen.COLOUR_WHITE,
            start_frame=100,
            stop_frame=250),
    ]

    screen.play([Scene(effects,250)], stop_on_resize=True, repeat=False)

    print()

def main():
    try:
        Screen.wrapper(credits)
    except ResizeScreenError:
        Screen.wrapper(credits)