from sympy.parsing.sympy_parser import parse_expr
from core.theorem import binomial_theorem
from core.utils import k_to_list, k_complete, is_positive


def k_input_menu():
    while True:
        try:
            k_value = int(input("1. Listar elementos de k\n2. Todos\n"))
            if k_value != 1 or k_value != 2:
                return k_value
            else:
                raise ValueError("Valor fuera de rango")
        except ValueError:
            pass


def main_input():
    x_sustitution = parse_expr(input("Introduce el valor de X: "))
    y_sustitution = parse_expr(input("Introduce el valor de Y: "))
    n = int(input("Introduce el valor de N: "))
    return x_sustitution, y_sustitution, n


def print_binomialtheorem(n, i, x, y):
    if is_positive(str(binomial_theorem(n, i, x, y))) == False:
        print("+", end="")
        print(binomial_theorem(n, i, x, y), end=" ")
    else:
        print(parse_expr(str(binomial_theorem(n, i, x, y))), end=" ")


def main():
    x, y, n = main_input()
    k_menu = k_input_menu()
    if k_menu == 1:
        k = k_to_list(n)
        for i in k:
            print_binomialtheorem(n, i, x, y)
        print("\n")
    else:
        k = k_complete(n)
        for i in k:
            print_binomialtheorem(n, i, x, y)
        print("\n")


if __name__ == "__main__":
    main()
