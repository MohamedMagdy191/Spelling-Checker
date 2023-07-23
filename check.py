from SpellingChecker import SpellingChecker

path = 'dictionary.txt'

spell = SpellingChecker(path)

print(spell.neighbours("word"))

print(spell.neighbours("animaal"))

print(spell.neighbours("animel"))

print(spell.neighbours("angri"))

spell.add_word("animal")

print(spell.neighbours("animeel"))

spell.add_word("animeel")

print(spell.neighbours("animeel"))
