import chess
import pygame as pg
from itertools import product

class Game:

    __white = (230, 230, 230)
    __black = (50, 50, 50)

    def __init__(self, board:chess.Board, display_color=0, width=400, height=400):
        pg.init()
        self.__surface = pg.display.set_mode((width, height))
        self.__display = display_color
        self.__board = board
        self.__graphics = self.load_graphics(width, height)
        self.__draw_board()
        self.__draw_pieces()
        self.__selected = None

    @property
    def __tile_w(self):
        return self.__surface.get_width()//8

    @property
    def __tile_h(self):
        return self.__surface.get_height()//8

    @staticmethod
    def load_graphics(width, height):
        graphics = {}
        color = ['black', 'white']
        piece = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
        for c, p in product(color, piece):
            name = f"{c}_{p}"
            image = pg.image.load(f"graphics/{name}.png")
            graphics[name] = pg.transform.scale(image, (width//8, height//8))
        return graphics

    def __draw_board(self):
        color = 0
        for x in range(8):
            for y in range(8):
                c = self.__black if color else self.__white
                r = pg.Rect(x*self.__tile_w, y*self.__tile_h, self.__tile_w, self.__tile_h)
                pg.draw.rect(self.__surface, c, r)
                color = ~color
            color = ~color

    def __draw_pieces(self):
        for x in range(8):
            for y in range(8):
                tx = x if self.__display else (7-x)
                ty = y if self.__display else (7-y)
                piece = self.__board.piece_at(chess.square(tx, 7-ty))
                if not piece:
                    continue
                name = chess.piece_name(piece.piece_type).lower()
                color = 'white' if piece.color else 'black'
                pos = (tx*self.__tile_w, ty*self.__tile_h)
                self.__surface.blit(self.__graphics[f"{color}_{name}"], pos)

        pg.display.update()

    def update(self):
        self.__draw_pieces()

    def select(self, pos:tuple):
        x = pos[0] // self.__tile_w
        y = pos[1] // self.__tile_h
        pos = (x, (7-y) if not self.__display else y)
        if self.__selected:
            try:
                move = chess.Move(chess.square(*self.__selected), chess.square(*pos))
                self.__board.push_uci(str(move))
                self.__draw_board()
            finally:
                self.__selected = None
                return
        self.__selected = pos
        return

    @property
    def board(self):
        return self.__board
