class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """ Initializes a wordfinder object which creates a list of words read
         from a given file path and prints out the number of words read """
        self.file_path = file_path
        self.word_list = self.get_word_list()


    def get_word_list(self):
        """ read a file at the given file path and return a list of words """

        word_list = []
        file = open(self.file_path, 'r')

        for line in file:
            word_list.append(line.strip('\n'))

        file.close()

        return word_list
