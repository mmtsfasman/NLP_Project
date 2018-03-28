import pandas as pd
import numpy as np
import json
from rated_words.indexer import ReverseIndex
from string import punctuation
from re import sub
from functools import reduce


corpus = pd.read_csv("../corpus.csv")
corpus["Stemmed"] = corpus["Stemmed"].apply(lambda x: set(x.split()))
with open("../ngrams.txt", encoding="utf8") as io:
    lines = [sub("[%s]" % punctuation, "", x.strip()) for x in io.readlines()]
    lines = [x for x in lines if x]

index = ReverseIndex()
index.load("../reverse_index.pkl")

ratings = {"Interior": {}, "Service": {}, "Food": {}}

for category in ratings.keys():
    for line in lines:
        words = [x.lower() for x in line.split()]
        texts = []

        for word in words:
            lword = word.lower()
            ratings[category][lword] = []
            try:
                texts_with_word = corpus[corpus["Index"].isin(list(index.words[lword]))]
                texts.append(texts_with_word)
            except KeyError:
                print("Missed word %s" % lword)
                continue
        texts_with_word = reduce(lambda x, y: pd.merge(x, y, on = 'Index', how="inner"), texts)
        # texts_with_word = pd.merge(*texts, on="Index", how="inner")
        ratings[category][" ".join(words)] = [x[category + "_x"] for i, x in texts_with_word.iterrows()]
        print("Processed word %s" % " ".join(words))

    for word, rlist in ratings[category].items():
        mean = np.mean(rlist)
        sd = np.std(rlist)
        df = len(rlist)
        ratings[category][word] = (mean, sd, df)

with open("cat_polarized_ngrams.json", "w") as io:
    json.dump(ratings, io)

for category, values in ratings.items():
    with open("%s_ngrams.csv" % category, "w") as io:
        val_list = values.items()
        val_list = sorted(val_list, key=lambda x: x[1][1])
        for val in val_list:
            io.write("%s,%s,%s,%s\n" % (val[0], val[1][0], val[1][1], val[1][2]))
