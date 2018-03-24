from bs4 import BeautifulSoup
import pandas as pd
from pymystem3 import Mystem
from re import sub
from string import punctuation

def save_csv(path: str):
    rows = []
    m = Mystem()
    with open(path, "r", encoding="utf8") as io:
        text = io.read()
        soup = BeautifulSoup(text)
    reviews = soup.find_all("review")
    for review in reviews:
        line = {"Text": review.find("text").string, "Stemmed": process_string(review.find("text").string, m),
                "Food":review.scores.food.string,
                "Interior": review.scores.interior.string, "Service": review.scores.service.string}
        rows.append(line)
        print("Processed line")

    df = pd.DataFrame(rows)
    df.to_csv("corpus.csv")

def process_string(string:str, stemmer):
    new_string = sub("[%s]" % punctuation, "", string)
    new_string = sub('\s+', ' ', ' '.join(stemmer.lemmatize(new_string.lower())))
    return new_string

if __name__ == "__main__":
    save_csv("SentiRuEval_rest_train.xml")