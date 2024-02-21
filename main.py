import string
import random
import math

rows = [
    {
        "age": 10,
        "id": "abcdefghijklmnop"
    }
]
num_rows = 100
max_age = 100


def get_random_age():
    return math.floor(max_age * random.random()) + 1


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
    for i in range(num_rows):
        new_row = step(rows[i])
        rows.append(new_row)
    print_rows(rows)


if __name__ == '__main__':
    main()
