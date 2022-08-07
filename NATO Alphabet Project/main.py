#TODO 1. Create a dictionary in this format:
import pandas as pd
alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

mapping = {row.letter: row.code for (index, row) in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
passed = input(">>>")
try:
    passed_elements = [mapping[elements.upper()] for elements in passed]
    print(passed_elements)
except KeyError:
    print("Sorry, only letters in the alphabet please")




