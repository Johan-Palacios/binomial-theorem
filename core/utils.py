def k_to_list(n):
    k_items = [
        int(item)
        for item in input("Introduce los elementos separados por espacios: ").split()
        if int(item) >= 0 and int(item) <= n
    ]
    return k_items


def k_complete(n: int):
    k_items = [int(item) for item in range(0, n + 1)]
    return k_items


def is_positive(prompt: str):
    return prompt[0] == "-"


if __name__ == "__main__":
    pass
