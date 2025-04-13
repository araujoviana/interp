from sympy import symbols
from sympy.polys.polyfuncs import interpolate

def ler_entradas() -> list[tuple[float, float]]:
    try:
        x_count = int(input("Digite a quantidade de pontos: "))
        xs = []
        ys = []
        for i in range(x_count):
            xs.append(float(input(f"{i} - Digite o x: ").strip()))
            ys.append(float(input(f"{i} - Digite o f(x): ").strip()))

    except ValueError:
        print("Erro: entrada inválida")
        return ler_entradas()
    else:
        return list(zip(xs, ys))


def main():
    x = symbols('x')

    pontos = ler_entradas()

    poly = interpolate(pontos, x)

    print(poly)


if __name__ == "__main__":
    main()