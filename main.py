import string
import random
import math
from dotenv import load_dotenv
import os
import enums

load_dotenv()

config = {
    "max_age": int(os.environ.get("MAX_AGE")),
    "num_rows": int(os.environ.get("NUM_ROWS"))
}
rows = [
    {
        "age": 24,
        "id": "aaaaaaaaaaaa",
        "name": {
            "first_name": "Ondřej",
            "last_name": "Brůha"
        }
    }
]


def get_random_age():
    return math.floor(config["max_age"] * random.random()) + 1


def get_random_name():
    last_name = random.choice(enums.enum_last_names)
    first_name = random.choice(enums.enum_first_names)
    return {"first_name": first_name, "last_name": last_name}


def get_random_id(prev):
    letters = string.ascii_lowercase
    rand_id = str(prev)
    while id == prev:
        rand_id = ''.join(random.choice(letters) for _ in range(len(prev)))
    return rand_id


def step(row):
    next_row = {}
    if isinstance(row, dict):
        for key in row.keys():
            if key == "age":
                next_row[key] = get_random_age()
            elif key == "id":
                next_row[key] = str(get_random_id(row[key]))
            elif key == "name":
                next_row[key] = get_random_name()
            else:
                print(f"key {key} is invalid")
    else:
        raise Exception("invalid row type")
    return next_row


def print_row(row, index):
    print("")
    print(f"Row {index}: {row}")


def print_rows(rows_list):
    for index, row in enumerate(rows_list):
        print_row(row, index)


def main():
    for i in range(config["num_rows"]):
        new_row = step(rows[i])
        rows.append(new_row)
    print_rows(rows)


if __name__ == '__main__':
    main()
