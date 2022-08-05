import pygame as pg
import chess

class Game:
    def __init__(self, color:chess.Color, pieces, width=400, height=400):
        pg.init()
        self.__surface = pg.display.set_mode((width, height))
        self.__pieces = pieces
        self.white = (230, 230, 230)
        self.black = (50, 50, 50)
        self.graphics:dict = {}
        self.__setup_graphics()
        self.__draw_board(color)
        self.__draw_pieces(color)

    def __setup_graphics(self):
        for color in ['black', 'white']:
            for piece in ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']:
                self.graphics[f"{color}_{piece}"] = \
                    pg.transform.scale(pg.image.load(f"graphics/{color}_{piece}.png"), \
                        (self.__surface.get_width()//8, self.__surface.get_height()//8))
    
    def __draw_board(self, player_color:chess.Color):
        tile_width = self.__surface.get_width()//8
        tile_height = self.__surface.get_height()//8
        color = chess.Color.WHITE
        for j in range(8):
            for i in range(8):
                pg.draw.rect(self.__surface, self.white if color == chess.Color.WHITE else self.black, pg.Rect(i*tile_width, j*tile_height, tile_width, tile_height))
                color = chess.Color.BLACK if color == chess.Color.WHITE else chess.Color.WHITE
            color = chess.Color.BLACK if color == chess.Color.WHITE else chess.Color.WHITE

        pg.display.flip()

    def __draw_pieces(self, player_color:chess.Color):
        tile_width = self.__surface.get_width()//8
        tile_height = self.__surface.get_height()//8
        for i in range(8):
            for j in range(8):
                for piece in self.__pieces:
                    if piece.position == chess.Position(j, i):
                        mp_x = (7-i) if player_color == chess.Color.WHITE else i
                        mp_y = j if player_color == chess.Color.WHITE else (7-j)
                        self.__surface.blit(self.graphics[str(piece)], (mp_y*tile_width, mp_x*tile_height))
           
        pg.display.update()
                

    def update(self):
        pass
        


