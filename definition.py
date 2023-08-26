import pandas


class Definition:
    """
    This class represents definitions of the words.
    """

    def __init__(self, word):
        self.word = word

    def get_definition(self):
        """gets definition of the word from dataFrame"""
        df = pandas.read_csv('files/data.csv')
        word_definitions = tuple(df.loc[df['word'] == self.word]['definition'])
        return word_definitions


if __name__ == '__main__':
    term = input('Type word: ')
    definition = Definition(word=term)
    definitions = definition.get_definition()
    for i in definitions:
        print(i)
