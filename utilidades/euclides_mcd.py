
# Script que calcula el máximo común divisor
# entre dos números usando el algoritmo de Euclides

def euclides_mcd(a: int, b: int):
    while b != 0:
        c = a % b
        a, b = b, c
    return a

def __lanzador__():
    a, b = 3, 11
    print("El máximo común divisor entre {} y {} es: {}".format(a, b, euclides_mcd(a, b)))


if __name__ == "__main__":
    __lanzador__()
