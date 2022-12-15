
# Script que calcula el máximo común divisor entre dos números
# y los coeficientes de Bézout que cumplen con la identidad de Bézout

def mcd_extendido(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = mcd_extendido(b % a, a)
    # Actualiza x e y con los resultados recursivos de la función
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def __lanzador__():
    a, b = 35, 15
    gcd, x, y = mcd_extendido(a, b)

    print("El máximo común divisor entre {} y {} es: {}".format(a, b, gcd))
    print("Luego, se tiene que:")
    print("ax + by = g(a,b) => {}({}) + {}({}) = {}".format(a, x, b, y, gcd))


if __name__ == "__main__":
    __lanzador__()