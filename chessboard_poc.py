import chess
import chess.svg

board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")

svg_image = chess.svg.board(
    board,
    fill=dict.fromkeys(board.attacks(chess.E4), "#cc0000cc") | {chess.E4: "#00cc00cc"},
    arrows=[chess.svg.Arrow(chess.E4, chess.F6, color="#0000cccc")],
    size=350,
)

with open("./chessboard.svg", "w") as f:
    f.write(svg_image)