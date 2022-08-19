"""Count repeated character"""
from collections import Counter


def countChar(string, char):
    count = Counter(string)
    return count[char]


string = "elaf ghassan jameel"
char = 'e'
print(countChar(string, char))
