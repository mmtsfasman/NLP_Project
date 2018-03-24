import pandas as pd
import numpy as np
import json
from indexer import ReverseIndex


corpus = pd.read_csv("corpus.csv")
corpus["Stemmed"] = corpus["Stemmed"].apply(lambda x: set(x.split()))
with open("seed_extended.json") as io:
    words = json.load(io)

index = ReverseIndex()
index.load("reverse_index.pkl")

ratings = {"Interior": {}, "Service": {}, "Food": {}}

for category in ratings.keys():
    for word, count in words.items():
        lword = word.lower()
        ratings[category][lword] = []
        try:
            texts_with_word = corpus[corpus["Index"].isin(list(index.words[lword]))]
        except KeyError:
            print(f"Missed word {lword}")
            continue
        ratings[category][lword] = [x[category] for i, x in texts_with_word.iterrows()]
        print(f"Processed word {lword}")

    for word, rlist in ratings[category].items():
        mean = np.mean(rlist)
        sd = np.std(rlist)
        df = len(rlist)
        ratings[category][word] = (mean, sd, df)

with open("cat_polarized.json", "w") as io:
    json.dump(ratings, io)

for category, values in ratings.items():
    with open(f"{category}_words.csv", "w") as io:
        val_list = values.items()
        val_list = sorted(val_list, key=lambda x: x[1][1])
        for val in val_list:
            io.write(f"{val[0]};{val[1][0]};{val[1][1]};{val[1][2]}\n")
