from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

        >>> wf = WordFinder('test-words.txt')
        3 words read

        >>> wf.random() in ['cat', 'dog', 'rat']
        True

        >>> wf.random() in ['cat', 'dog', 'rat']
        True

        >>> wf.random() in ['cat', 'dog', 'rat']
        True


    """

    def __init__(self, file_path):
        """ Initializes a wordfinder object which creates a list of words read
         from a given file path and prints out the number of words """

        self.words = self.get_words(file_path)

        print(f"{len(self.words)} words read")

    def get_words(self, file_path):
        """ read a file at the given file path and return a list of words """

        file = open(file_path, 'r')

        words = [line.strip() for line in file]

        file.close()

        return words

    def random(self):
        """ Returns random word from list of words """

        return choice(self.words)
        # return set(self.word_list).pop()


class SpecialWordFinder(WordFinder):
    """Random Word Finder: handles # and blank space cases"""

    def get_words(self, file_path):
        """ Filters out lines that start with # and blank lines """

        dirty_words = super().get_words(file_path)

        return [word for word in dirty_words if word and not word.startswith("#")]
