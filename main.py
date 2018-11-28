# Coded by Stephanie Callejas
# Last Edit: 12 Nov 2018
# CS2302 Lab 4 B Project
# Instructors: Diego Aguirre and Saha, Manoj Pravakar
# Goal: Determine if a given anagram is a valid word in the english language using hash tables
from chaininghashtable import ChainingHashTable

# f is used to populate the tree with the words

f = open("words.txt")
word_list = f.readlines()

for i in range(len(word_list)):
    word_list[i] = word_list[i][:-2]  # -2 to get rid of the enter space
counter = 0


# The method print_anagrams shown below prints all the anagrams of a given word.
# To do this, it generates all permutations of the letters in the word and, for each permutation,
# it checks if it is a valid word in the English language.
# if you call print_anagrams("spot"),the method should print the following words: spot, stop, post, pots, opts, and tops

def print_anagrams(word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in word_list:
            print(prefix + word)

    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            #if cur not in before:  # Check if permutations of cur have not been generated.
            print_anagrams(prefix + cur, before + after, word_list)


# Main program to test HashTable classes
keys = [35, 0, 22, 94, 220, 110, 4]
chaining = ChainingHashTable()

for key in keys:
    chaining.insert(key)


# Show tables after inserts.
print ("Chaining: initial table:")
print (chaining)
print()


# Show tables after removing item 0
print ("=======================================")
chaining.remove(0)


print ("Chaining: after removing 0:")
print(chaining)
print()

