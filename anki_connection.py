import genanki

# Unique for this model
MODEL_GUID = 1238229309

my_model = genanki.Model(
    MODEL_GUID,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ]
)

my_note = genanki.Note(
    model=my_model,
    fields=['Capital of Argentina', 'Buenos Aires']
)

my_deck = genanki.Deck(
  2104873761,
  'Country Capitals')

my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('output.apkg')