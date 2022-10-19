def k_to_list(n: int, values: list) -> list:
    k_items = []
    for value in values:
        if value == "":
            continue
        if (int(value) >= 0 and int(value) <= n) and (int(value) not in k_items):
            k_items.append(int(value))
    return k_items


def k_complete(n: int):
    k_items = [int(item) for item in range(0, n + 1)]
    return k_items


def is_positive(prompt: str):
    return prompt[0] == "-"


if __name__ == "__main__":
    pass
