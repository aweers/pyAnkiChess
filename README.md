# pyAnkiChess
Import chess PGN into Anki from a local file or lichess study.

```bash
usage: pyAnkiChess.py [-h] [-d DECKNAME] [-b] [-s SIZE] [-o OUTPUT] pgn

positional arguments:
  pgn                   PGN file (*.pgn) or lichess study id (8 alphanumeric characters, following
                        'https://lichess.org/study/')

options:
  -h, --help            show this help message and exit
  -d DECKNAME, --deckname DECKNAME
                        Deck name
  -b, --black           Play from blacks perspective
  -s SIZE, --size SIZE  Size of output
  -o OUTPUT, --output OUTPUT
                        Output file (.apkg)
```

## Examples:
- Use local PGN file: 
```bash
python pyAnkiChess.py -d "Vienna opening" -o vienna.apkg pgns/vienna_opening.pgn
```
- Use lichess study (URL: https://lichess.org/study/El9igr12). Note that only public studies are supported. 
```bash
python pyAnkiChess.py -d "London system" -o london.apkg El9igr12
```
