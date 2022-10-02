import berserk
import io
import chess
import chess.pgn

client = berserk.Client()

study_id = "El9igr12"

study = list(client.studies.export(study_id))

for chapter in study:
    pgn = io.StringIO(chapter)
    game = chess.pgn.read_game(pgn)
    for i in range(3):
        game = game.next()
    print(game.board())
