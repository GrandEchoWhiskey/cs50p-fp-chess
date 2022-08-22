import chess
from stockfish import Stockfish, StockfishException
import pygame as pg

def main():

    board = chess.Board()
    sf = Stockfish(
        depth=20,
        parameters={
            "Threads": 2,
            "Minimum Thinking Time": 30
        }
    )

    sf.update_engine_parameters({
        "Hash": 2048,
        "UCI_Chess960": "true"
    })

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