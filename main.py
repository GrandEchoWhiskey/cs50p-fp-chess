import pygame as pg
import chess
import chessgame as game
from pygame.locals import *
import sys

def main():

    if len(sys.argv) > 1:
        raise NotImplementedError

    g = game.Game()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                g.select(pg.mouse.get_pos())
        g.update()

if __name__ == "__main__":
    main()