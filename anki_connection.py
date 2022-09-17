import genanki

class AnkiChessNote(genanki.Note):
    @property
    def guid(self):
        # use move history
        return genanki.guid_for(self.fields[3])

class AnkiChessConnection:
    # Unique for this model
    MODEL_GUID = 1238229309
    DECK_GUID = 2104873761

    def __init__(self, deck_name, title):
        self.deck_name = deck_name
        self.title = title
        self.deck = genanki.Deck(AnkiChessConnection.DECK_GUID, deck_name)
        self.model = genanki.Model(
            AnkiChessConnection.MODEL_GUID,
            'Simple Model',
            fields=[
                {'name': 'Title'},
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'Move history'},
                {'name': 'URL'}
            ],
            templates=[
                {
                'name': 'Card 1',
                'qfmt': '{{Title}} </br> {{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ]
        )

    def addCard(self, front_svg, back_svg, move_history, url=""):
        note = AnkiChessNote(
            model=self.model,
            fields=[
                self.title,
                front_svg,
                back_svg,
                move_history,
                url
            ])
        self.deck.add_note(note)

    def savePackage(self, output):
        genanki.Package(self.deck).write_to_file(output)

anki = AnkiChessConnection("Chess opening", "Vienna Gambit")

with open("studyMove3.svg", "r") as f:
    svg1 = f.read()
with open("chessboard.svg", "r") as f:
    svg2 = f.read()

anki.addCard(svg1, svg2, "e4 e5 Nf3", "www.com")

anki.savePackage("output.apkg")