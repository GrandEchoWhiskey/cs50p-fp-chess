from chess import Board
from stockfish import Stockfish
import pygame as pg

def draw_pieces(surface, board):
    pass

def main():

    pg.init()

    board = Board()
    
    surface = pg.display.set_mode((400, 400))
    white = (230, 230, 230)
    black = (50, 50, 50)

    graphics:dict = {}
    for color in ['white', 'black']:
        for piece in ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']:
            key = f"{color}_{piece}"
            graphics[key] = pg.transform.scale(
                pg.image.load(f"graphics/{key}.png"), \
                    (surface.get_width()//8, surface.get_height()//8)
            )

    tile_width = surface.get_width()//8
    tile_height = surface.get_height()//8
    color = 0
    for j in range(8):
        for i in range(8):
            pg.draw.rect(surface, white if not color else black, pg.Rect(i*tile_width, j*tile_height, tile_width, tile_height))
            color = 0 if color else 1
        color = 0 if color else 1

    

    sf = Stockfish(
        depth=50,
        parameters={
            "Threads": 2,
            "Minimum Thinking Time": 30,
            "Hash": 2048,
            "UCI_Chess960": "true"
        }
    )

    sf.set_fen_position(board.fen())

    while not board.is_game_over():
        print(board)
        move = sf.get_best_move()
        sf.make_moves_from_current_position([move])
        board.push_san(move)

    print(board)

    return

if __name__ == "__main__":
    main()