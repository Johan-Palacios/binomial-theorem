from sympy.parsing.sympy_parser import parse_expr
from core.theorem import binomial_theorem
from core.utils import k_to_list, k_complete, is_positive
from sympy import pprint


def k_input_menu():
    while True:
        try:
            k_value = int(input("1. Listar elementos de k\n2. Todos\n--> "))
            if k_value in [1, 2]:
                return k_value
            else:
                raise ValueError("Valor fuera de rango")
        except ValueError:
            continue


def main_input():
    while True:
        try:
            x_sustitution = parse_expr(input("Introduce el valor de X: "))
            y_sustitution = parse_expr(input("Introduce el valor de Y: "))
            n = int(input("Introduce el valor de N: "))
            return x_sustitution, y_sustitution, n
        except Exception:
            continue


def binomial_theorem_complete(n, i, x, y, binomial_solution):
    resultBinomial = str(binomial_theorem(n, i, x, y))
    if is_positive(resultBinomial):
        return "+" + resultBinomial
    else:
        return resultBinomial


def main():
    x, y, n = main_input()
    k_menu = k_input_menu()
    if k_menu == 1:
        values = (
            input("Introduce los elementos separados por comas: ")
            .replace(" ", "")
            .split(",")
        )
        k_list = k_to_list(n, values)
        binomial_solution = ""
        for k in k_list:
            binomial_solution += binomial_theorem_complete(n, k, x, y, binomial_solution)
        pprint(parse_expr(binomial_solution))
        print("\n")
    else:
        k_list = k_complete(n)
        binomial_solution = ""
        for k in k_list:
            binomial_solution += binomial_theorem_complete(n, k, x, y, binomial_solution)
        pprint(parse_expr(binomial_solution))
        print("\n")


if __name__ == "__main__":
    main()
