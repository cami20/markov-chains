"""Generate markov text from text files."""


from random import choice
import sys


def open_and_read_file(file_path, file_path2):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path).read()
    text_file2 = open(file_path2).read()

    full_text_file = text_file + " " + text_file2

    return full_text_files


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

    chains = {}

    # your code goes here
    words = text_string.split()
    word_pair = ()

    for i in range(len(words) - 2):
        word_pair = words[i], words[i + 1]
        if word_pair not in chains:
            chains[word_pair] = [words[i + 2]]
        else:
            chains[word_pair].append(words[i + 2])

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []
    new_value = ""
    # your code goes here
    key = choice(chains.keys())

    # print key
    # print key[0].istitle()

    while not key[0].istitle():
        key = choice(chains.keys())

    words.append(" ".join((key)))

    while key in chains:
            new_value = choice(chains[key])
            words.append(new_value)
            key = (key[1], new_value)


    return " ".join(words)


input_path = sys.argv[1]
input_path2 = sys.argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
