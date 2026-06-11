
def x_power_x(x):
    return x ** x


def format_result(x):
    return f"{x} elevado a {x} é {x_power_x(x)}"


def main():
    x = int(input("Digite um numero para elevar ele a ele mesmo: "))
    print(format_result(x))


if __name__ == "__main__":
    main()