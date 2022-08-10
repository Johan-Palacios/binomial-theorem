def k_to_list():
    k_items = []
    k_items = [int(item) for item in input("Introduce los elementos separados por espacios: ").split()]
    return k_items

def k_complete(n:int):
    k_items = []
    k_items = [int(item) for item in range(0, n+1)]
    return k_items

def add_plus(prompt:str):
    for i in prompt:
        return i == "-"

if __name__ == "__main__":
    pass
