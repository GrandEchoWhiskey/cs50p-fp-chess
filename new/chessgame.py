import chess
from stockfish import Stockfish, StockfishException
from gui import Game
import pygame as pg
from pygame.locals import *
import sys

board = chess.Board()

game = Game(board)

while not game.board.is_game_over():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.K_q:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            game.select(pg.mouse.get_pos())
    game.update()