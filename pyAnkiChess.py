from anki_connection import AnkiChessConnection
import argparse
import os.path
import chess
import chess.svg
import chess.pgn

parser = argparse.ArgumentParser()
parser.add_argument("pgn", help="PGN file")
parser.add_argument("-d", "--deckname", help="Deck name", default="Chess openings")
parser.add_argument("-b", "--black", help="Play from blacks perspective", action="store_true")
parser.add_argument("-s", "--size", help="Size of output", type=int, default=300)
parser.add_argument("-o", "--output", help="Output file (.apkg)", default="chess.apkg")
args = parser.parse_args()

if(not os.path.exists(args.pgn)):
    print("Cannot find provided file: " + args.pgn)
    exit()

ORIENTATION = chess.WHITE
if args.black:
    ORIENTATION = chess.BLACK

def game2svg(board, move):
    return chess.svg.board(
        board,
        orientation=ORIENTATION,
        lastmove=move,
        size=args.size
    )

pgn_file = open(args.pgn)
study = chess.pgn.read_game(pgn_file)
title = study.headers['Event']
url = study.headers['Site']

anki = AnkiChessConnection(args.deckname, title)

def next_move(study: chess.pgn.GameNode):
    board = study.board()
    if study.turn() == ORIENTATION:
        move = study.variations[0].move
        svg1 = game2svg(board, board.peek())
        board.push(move)
        svg2 = game2svg(board, move)
        anki.addCard(svg1, svg2, " ".join([m.uci() for m in board.move_stack]), url)

    for variation in study.variations:
        next_move(variation)

next_move(study)
anki.savePackage(args.output)