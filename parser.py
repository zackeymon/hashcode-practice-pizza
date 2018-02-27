from pizza import Pizza

_topping = {"T": 0, "M": 1}


def parse(file_name):
    with open(file_name) as f:
        R, C, L, H = map(int, f.readline().strip().split())
        pizza = Pizza(R, C, L, H)

        for line in f:
            row = []
            for char in line.strip():
                row.append(_topping[char])
            pizza.grid.append(row)

    return pizza