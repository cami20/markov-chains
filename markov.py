"""Generate markov text from text files."""


from random import choice


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

    chains = {}

    # your code goes here
    words = text_string.split()
    word_pair = ()

    for i in range(len(words) - 1):
        word_pair = words[i], words[i + 1]
        if words[i] in [words[len(words) - 2], words[len(words) - 3]]:
            break
        elif word_pair not in chains:
            chains[word_pair] = [words[i + 2]]
        else:
            chains[word_pair].append(words[i + 2])

    # for i in range(len(words) -1):
    #     if words[i + 2] not in chains[word_pair]:
    #         chains[word_pair].append(words[i + 2])

    print chains
 
    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
