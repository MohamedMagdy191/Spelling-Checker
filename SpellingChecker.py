
import os
import regex as re
from fuzzywuzzy import fuzz


# spellcheck main class
class SpellingChecker:

    # initialization method
    def __init__(self, path):
        # open the dictionary file
        self.file = open(path, 'r', errors='replace')

        # load the file data in a variable
        data = self.file.read()

        # store all the words in a list
        data = data.split("\n")

        # change all the words to lowercase
        data = [i.lower() for i in data]

        # remove all the duplicates in the list
        data = set(data)

        # store all the words into a class variable dictionary
        self.dictionary = list(data)

        # sort the dictionary in lexicographic order
        self.dictionary = sorted(self.dictionary)

        # function returns list of the nearst 4 word from the target word

    def nearest_words(self, key):
        keys = []
        for word in self.dictionary:
            x = re.search(key,
                          word)  # Matches the first instance of key in the (word), and returns it as a re match object.
            if x and (x.span()[0] == 0):
                keys.append(word)
        return keys

    def nearest_four_words(self, key):

        keys = []  # list of the nearest words to the key
        nearest4 = []  # the target list which will contain the nearst 4 words to the key
        key = key.lower()
        if len(key) > 4:
            KEY = key[0:4]
            keys = self.nearest_words(KEY)
        else:
            KEY = key
            keys = self.nearest_words(KEY)

        neighbours = {}
        for word in keys:
            score = fuzz.ratio(word, key)
            neighbours[word] = int(score)
        if neighbours:
            nearest_word = max(neighbours, key=neighbours.get)
            target_idx = self.dictionary.index(nearest_word)
            nearest4 = self.dictionary[target_idx:target_idx + 4]
        else:
            nearest4 = print("Edit the word please")
        return nearest4

    # function that appends input word to the dictionary
    def add_word(self, word):
        if word in self.dictionary:
            print("the word ({}) is allready in the dictionary!".format(word))
        else:
            self.dictionary.append(word)
            self.dictionary = sorted(self.dictionary)
            print("the word ({}) was added seccessfully".format(word))
            
    def export_dictionary(self,out_path): # the out path in form of '/---/----/file_name.txt'
        with open(out_path, 'w') as output:
            for row in self.dictionary:
                output.write(str(row) + '\n')
        print("Done")
