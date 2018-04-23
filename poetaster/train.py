import spacy

from poetaster.io import Loader

from pprint import pprint

class Trainer(object):

    def __init__(self):
        self.loader = Loader()

    def train(self):
        poems = self.loader.load_author('Milne')

        pprint(poems)

        nlp = spacy.load('en')


if __name__ == '__main__':

    Trainer().train()
