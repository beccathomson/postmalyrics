from datamuse import datamuse

api = datamuse.Datamuse()
api.words(rel_rhy='ninth', max=5)  # words that rhyme with "ninth"
[]
api.words(rel_rhy='orange', max=5)  # words that rhyme with "orange"
[{'word': 'door hinge', 'score': 74, 'numSyllables': 2}]
api.words(rel_jja='yellow', max=5)  # things often described as "yellow"
[{'word': 'fever', 'score': 1001}, {'word': 'color', 'score': 1000}, {'word': 'flowers', 'score': 999}, {'word': 'light', 'score': 998}, {'word': 'colour', 'score': 997}]
api.suggest(s='foo', max_results=10)  # completion suggestions for "foo"
[{'word': 'food', 'score': 3888}, {'word': 'foot', 'score': 3041}, {'word': 'fool', 'score': 1836}, {'word': 'football', 'score': 1424}, {'word': 'footage', 'score': 1328}, {'word': 'footprint', 'score': 1082}, {'word': 'foolish', 'score': 967}, {'word': 'foof', 'score': 930}, {'word': 'footing', 'score': 786}, {'word': 'foolproof', 'score': 697}]