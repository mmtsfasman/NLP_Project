import pickle, math
import pandas as pd

class ReverseIndex:

    def __init__(self):
        self.words = {}
        self.length = 0

    def add(self, text:str):
        tokens = text.split()
        for token in tokens:
            self.words.setdefault(token, set()).add(self.length)
        self.length += 1
        print("Added a text")

    def get_idf(self, term):
        termlist = self.words.get(term, [])
        df = len(termlist) + 1

        return math.log(self.length / df)

    def get_df(self, term):
        termlist = self.words.get(term, [])
        df = len(termlist) + 1

        return df

    def load(self, name="index.pkl"):
        if name:
            with open(name, 'rb') as loadfile:
                tmp_dict = pickle.load(loadfile)

            self.__dict__.update(tmp_dict)

    def save(self, name="index.pkl"):
        with open(name, 'wb') as savefile:
            pickle.dump(self.__dict__, savefile, 2)


if __name__ == "__main__":
    index = ReverseIndex()
    corpus = pd.read_csv("corpus.csv")
    for i, text in corpus.iterrows():
        index.add(text["Stemmed"])

    index.save("reverse_index.pkl")