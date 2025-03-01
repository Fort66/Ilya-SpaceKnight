import pygame as pg

from config.create_Objects import (
    screen,
)
from classes.class_CheckEvents import CheckEvents

class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.check_events = CheckEvents(self)

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)
            self.check_events.check_events()


            pg.display.update()
