# Spelling-Checker
A Spell Checker Python Class

### Summary
This class takes (dictionary.txt) as an input
  `spell = SpellingChecker(path)`

The class has five main operations:
1. It stores this dictionary in a python list in lexicographic order.
2. It takes an input word and returns the nearest 4 words if this word is not in the dictionary and returns the word and the nearest 3 words to it if this word is allready in the dictionary.
   `spell.nearest_four_words(word)`
3. It takes an input word and returns the nearest words (it's not a certain number of words)
  `spell.nearest_words(word)`
4. It takes an input word and add this word to the dictionary if it is not allready in the dictionary.
  `spell.add_word(word)`
5. It takes a path of (file.txt) and exports the edited dictionary if any updates are done.
    `spell.export_dictionary(word)`

### Requirements:
* regex
* fuzzywuzzy
* python-Levenshtein
