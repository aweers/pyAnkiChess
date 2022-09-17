import argparse
import os.path
import chess
import chess.pgn
import chess.svg

parser = argparse.ArgumentParser()
parser.add_argument("pgn", help="PGN file")
parser.add_argument("-b", "--black", help="Play from blacks perspective", action="store_true")
args = parser.parse_args()

if(not os.path.exists(args.pgn)):
    print("Cannot find provided file: " + args.pgn)
    exit()

ORIENTATION = chess.WHITE
if args.black:
    ORIENTATION = chess.BLACK

def printBoard(game, output="./studyMove3.svg"):
    svg_image = chess.svg.board(
        game.board(),
        orientation=ORIENTATION,
        lastmove=game.move
    )
    with open(output, "w") as f:
        f.write(svg_image)


pgn_file = open(args.pgn)
study = chess.pgn.read_game(pgn_file)
title = study.headers['Event']
url = study.headers['Site']

print(title)
print(url)

for i in range(3):
    study = study.next()

printBoard(study)