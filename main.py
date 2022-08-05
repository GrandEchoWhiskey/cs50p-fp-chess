import pygame as pg
import chess
import chessgame as game
from pygame.locals import *

def main():

    board = chess.Board() #chess.Color.WHITE
    g = game.Game(chess.Color.WHITE, board.pieces) #full board
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                return

if __name__ == "__main__":
    main()