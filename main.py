from sympy import symbols, lambdify
from sympy.polys.polyfuncs import interpolate
import numpy as np
import matplotlib.pyplot as plt

def ler_entradas() -> tuple[int,list[tuple[float, float]]]:
    try:
        x_count = int(input("Digite a quantidade de pontos: "))
        xs = []
        ys = []
        for i in range(x_count):
            xs.append(float(input(f"{i+1} - Digite o x: ").strip()))
            ys.append(float(input(f"{i+1} - Digite o f(x): ").strip()))

    except ValueError:
        print("Erro: entrada inválida")
        return ler_entradas()
    else:
        return x_count, list(zip(xs, ys))

def gerar_grafico(x, pontos, poly):
    poly_num = lambdify(x, poly, 'numpy')
    x_vals = np.linspace(-10, 10, 400)
    y_vals = poly_num(x_vals)

    plt.plot(x_vals, y_vals)
    xs, ys = zip(*pontos)
    plt.scatter(xs, ys, color='red', s=50)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Gráfico de {poly}')
    plt.grid(True)
    plt.show()


def calcular_l_n(x, pontos, n):
    l_n = 1
    x_n, _ = pontos[n]

    for i, (x_i, _) in enumerate(pontos):
        if i != n:
            l_n *= (x - x_i) / (x_n - x_i)

    return l_n


def main():
    x = symbols('x')

    x_count, pontos = ler_entradas()

    for n in range(x_count):
        l_n = calcular_l_n(x, pontos, n)
        print(f"L_{n}(x) = {l_n}")

    poly = interpolate(pontos, x)

    print(f"Função gerada -> {poly}")

    if input("Gerar gráfico? (s/n): ").lower().strip() == "s":
        gerar_grafico(x, pontos, poly)


if __name__ == "__main__":
    main()