from anki_connection import AnkiChessConnection
import argparse
import os.path
import chess
import chess.svg
import chess.pgn
import berserk
import io
import re

parser = argparse.ArgumentParser()
parser.add_argument("pgn", help="PGN file (*.pgn) or lichess study id (8 alphanumeric characters, following 'https://lichess.org/study/')")
parser.add_argument("-d", "--deckname", help="Deck name", default="Chess openings")
parser.add_argument("-b", "--black", help="Play from blacks perspective", action="store_true")
parser.add_argument("-s", "--size", help="Size of output", type=int, default=300)
parser.add_argument("-o", "--output", help="Output file (.apkg)", default="chess.apkg")
args = parser.parse_args()

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

def next_move(study: chess.pgn.GameNode, anki, url):
    board = study.board()
    if study.turn() == ORIENTATION and len(study.variations) > 0:
        move = study.variations[0].move
        last_move = None
        if board.fullmove_number > 1 or board.turn == chess.BLACK:
            last_move = board.peek()
        svg1 = game2svg(board, last_move)
        board.push(move)
        svg2 = game2svg(board, move)
        anki.addCard(svg1, svg2, " ".join([m.uci() for m in board.move_stack]), url)

    for variation in study.variations:
        next_move(variation, anki, url)

def read_pgn(anki, study):
    title = study.headers['Event']
    url = study.headers['Site']

    anki.setTitle(title)

    next_move(study, anki, url)
    anki.savePackage(args.output)

if __name__ == "__main__":
    anki = AnkiChessConnection(args.deckname, avoid_duplicates=True)

    # check if args.pgn is file or lichess study id
    if re.match(r'.*\.pgn', args.pgn):
        # is file
        if(not os.path.exists(args.pgn)):
            print("Provided file does not exist: " + args.pgn)
            exit()

        pgn_file = open(args.pgn)
        study = chess.pgn.read_game(pgn_file)
        read_pgn(anki, study)
    elif re.match(r'[A-Za-z0-9]{8}', args.pgn):
        # is lichess study id
        client = berserk.Client()
        try:
            study = list(client.studies.export(args.pgn))
        except:
            print("Cannot open lichess study with provided id: " + args.pgn)
            exit()
        else:
            for chapter in study:
                pgn = io.StringIO(chapter)
                study = chess.pgn.read_game(pgn)
                read_pgn(anki, study)
    else:
        print("Cannot find provided file (*.pgn) or open lichess study (8 alphanumeric characters): " + args.pgn)
        exit()