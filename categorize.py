import pandas as pd
import numpy as np
import json

corpus = pd.read_csv("corpus.csv")
corpus["Stemmed"].apply(lambda x: x.split())
with open("param.json") as io:
    words = json.load(io)

ratings = {"interior": {}, "service": {}, "food": {}}
for category, wordlist in words.items():
    for word in wordlist:
        ratings[category][word] = []
        for i, text in corpus.iterrows():
            if word in text["Stemmed"]:
                ratings[category][word].append(text[category.capitalize()])

    for word, rlist in ratings[category].items():
        mean = np.mean(rlist)
        sd = np.std(rlist)
        ratings[category][word] = (mean, sd)

with open("cat_polarized.json", "w") as io:
    json.dump(ratings, io)
