def is_even(n):
    return n % 2 == 0


def format_result(n):
    if is_even(n):
        return "O numero é par."
    return "O numero é impar."


def main():
    n = int(input("Digite um numero para saber se e par ou impar: "))
    print(format_result(n))


if __name__ == "__main__":
    main()