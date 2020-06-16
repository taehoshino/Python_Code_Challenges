import json


def save_dict(jisho, path):
    with open(path, "w") as f:
        json.dump(jisho, f, indent=2)

def load_dict(path):
    with open(path, "r") as f:
        return json.load(f)

sample = {"ID": 11111, "Name": "Smith", "Age": "34"}
save_dict(sample, "sample.json")

sample_loaded = load_dict("sample.json")
print(sample_loaded)


