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
for word1 in words:
    for word2 in words:
        if not word1==word2:
            if anagram(word1,word2):
                print 'Anagram: ', word1, ' -- ', word2

