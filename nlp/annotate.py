import spacy

from poetaster.io import Loader

from pprint import pprint


class Annotater(object):

    def __init__(self):
        self.loader = Loader()
        self.tokenizer = spacy.load('en')

    def annotate_author(self, author):
        poems = self.loader.load_author(author)

        pprint(poems)

        for poem in poems:
            annotated_poem = self.annotate_poem(poem)
            self.pprint(poem, annotated_poem)

    def pprint(self, poem, annotated_poem):
            print('\n\n{}, {} \n\n'.format(poem['author'], poem['period']))
            pprint(poem['text'])
            print('--\n----\n------\n--------\n----------\n------------>')
            print('ENTITIES:')
            pprint(list(annotated_poem.ents))

            print('NOUN CHUNKS:')
            pprint(list(annotated_poem.noun_chunks))

            print('VOCAB LEN: {}'.format(len(annotated_poem.vocab)))

            for word in annotated_poem:
                print(word)
                print(list(word.children))

    def annotate_poem(self, poem):
        # expect an array of lines
        poem = '\n'.join(poem['text'])

        return self.tokenizer(poem)


if __name__ == '__main__':

    Annotater().annotate_author('Eliot')
