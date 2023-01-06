import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=",") -> list[dict]:
    list_add = []
    with open(filename) as p:
        for s in p:
            list_add.append(s.rstrip().split(delimeter))
        dict_ = [dict(zip(list_add[0], s)) for s in list_add[1:]]
    return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
