from bs4 import BeautifulSoup
import pandas as pd

def save_csv(path: str):
    rows = []
    with open(path, "r", encoding="utf8") as io:
        text = io.read()
        soup = BeautifulSoup(text)
    reviews = soup.find_all("review")
    for review in reviews:
        line = {"Text": review.find("text").string, "Food":review.scores.food.string,
                "Interior": review.scores.interior.string, "Service": review.scores.service.string}
        rows.append(line)
        print("Processed line")

    df = pd.DataFrame(rows)
    df.to_csv("corpus.csv")

if __name__ == "__main__":
    save_csv("SentiRuEval_rest_train.xml")