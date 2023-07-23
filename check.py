from SpellingChecker import SpellingChecker

path = 'dictionary.txt'

spell = SpellingChecker(path)

print(spell.nearest_words("animal"))

print(spell.nearest_four_words("word"))

print(spell.nearest_four_words("animaal"))

print(spell.nearest_four_words("animel"))

print(spell.nearest_four_words("angri"))

spell.add_word("animal")

print(spell.nearest_four_words("animeel"))

spell.add_word("animeel")

print(spell.nearest_four_words("animeel"))

spell.export_dictionary("edited_dictionary.txt")
