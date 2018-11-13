# Coded by Stephanie Callejas
# Last Edit: 12 Nov 2018
# CS2302 Lab 4 B Project
# Instructors: Diego Aguirre and Saha, Manoj Pravakar
# Goal: Determine if a given anagram is a valid word in the english language using hash tables

# f is used to populate the tree with the words
f = open("words.txt")
word_list = f.readlines()

for i in range(len(word_list)):
    word_list[i] = word_list[i][:-2]  # -2 to get rid of the enter space
counter = 0


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)

    # A modulo hash uses the remainder from division of the key by hash table size N.
    def hash_remainder(self,key,N):
        return key % N

    # A binary mid-square hash function extracts the middle R bits,
    # and returns the remainder of the middle bits divided by hash table size N,
    # where R is greater than or equal to ⌈log2N⌉
    def hash_midsquare(self,key,N,R):
        squared_key = key * key

        lowbits_toremove = (32 - R) / 2
        extracted_bits = squared_key >> lowbits_toremove
        extracted_bits = extracted_bits & (0xFFFFFFFF >> (32 - R))

        return extracted_bits % N

    # Load factor calculated
    def load_factor(self):
        count = 0
        for i in range(i < self.table):
            count += self.table
        load_factor = count / self.table
        print("Current Load factor = " + load_factor);