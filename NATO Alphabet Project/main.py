#TODO 1. Create a dictionary in this format:
import pandas as pd
alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

mapping = {row.letter: row.code for (index, row) in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    passed = input(">>>")
    try:
        passed_elements = [mapping[elements.upper()] for elements in passed]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(passed_elements)


generate_phonetic()

