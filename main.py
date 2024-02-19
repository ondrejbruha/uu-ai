import string
import random
import math

rows = [
    {
        "age": 10,
        "id": "abcdefghijklmnop"
    }
]


def get_random_age():
    return math.floor(100 * random.random()) + 1


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


def print_row(row):
    for key, value in row.items():
        print(f"{key}: {value}")


def print_rows(rows_list):
    for row in rows_list:
        print_row(row)


def main():
    for i in range(10):
        new_row = step(rows[i])
        rows.append(new_row)
    print_rows(rows)


if __name__ == '__main__':
    main()
