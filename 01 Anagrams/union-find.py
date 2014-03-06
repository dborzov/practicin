"""
Using Weighted Union-Find algorithm to classify stuff
"""

import collections
import sys

def anagram(string1, string2):
    if not len(string1)==len(string2):
        return False
    def create_counter(from_string):
        counter = collections.Counter()
        for symbol in from_string:
            counter[symbol] +=1
        return counter
    counter1 = create_counter(string1)
    counter2 = create_counter(string2)
    mentioned_symbols = set(counter1.keys()+counter2.keys())

    for symbol in mentioned_symbols:
        if not counter1[symbol]==counter2[symbol]:
            return False
    return True



words = [line.rstrip() for line in sys.stdin]

union_links = [i for i in xrange(len(words))] # array to store the union links
def union(i,j):
    union_links[i]=j

for i in xrange(0,len(words)):
    for j in xrange(i,len(words)):
        if anagram(words[i],words[j]):
            print 'Anagram found: ', words[i], words[j]
            union(i,j)