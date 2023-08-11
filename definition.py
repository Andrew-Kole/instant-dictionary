import pandas

class Definition:
    """
    This class represents definitions of the words.
    """

    def __init__(self, term):
        self.term = term

    def get_definition(self):
        """gets definition of the word from dataFrame"""
        df = pandas.read_csv('files/data.csv')
        word_definitions = tuple(df.loc[df['word'] == self.term]['definition'])
        return word_definitions


if __name__ == '__main__':
    term = input('Type word: ')
    definition = Definition(term=term)
    definitions = definition.get_definition()
    for i in definitions:
        print(i)
