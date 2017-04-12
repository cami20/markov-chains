"""Generate markov text from text files."""


from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path).read()

    return text_file


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    n = raw_input("How many words would you like in your n-gram? ")
    n = int(n)
    counter = 1
    chains = {}

    # your code goes here
    words = text_string.split()
    word_pair = []

    for i in range(len(words) - n):
        word_pair.append(words[i])
        while counter < n:
            word_pair.append(words[i + counter])
            counter = counter + 1

        word_pair = tuple(word_pair)

        if word_pair not in chains:
            chains[word_pair] = [words[i + n]]
        else:
            chains[word_pair].append(words[i + n])

    print chains


def make_text(chains):
    """Returns text from chains."""

    words = []
    new_value = ""
    # your code goes here
    key = choice(chains.keys())

    while not key[0].istitle():
        key = choice(chains.keys())

    words.append(" ".join((key)))

    while key in chains:
            new_value = choice(chains[key])
            words.append(new_value)
            #key = (key[1:], new_value)
            key = list(key)
            key = key[1:]
            key.append(new_value)
            key = tuple(key)

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
