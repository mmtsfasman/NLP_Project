import json

with open("rated_words/cat_polarized.json", "r") as io:
    words = json.load(io)


for category, values in words.items():
    with open(f"{category}_words.csv", "w") as io:
        val_list = values.items()
        val_list = sorted(val_list, key=lambda x: x[1][1])
        for val in val_list:
            io.write(f"{val[0]};{val[1][0]};{val[1][1]};{val[1][2]}\n")

