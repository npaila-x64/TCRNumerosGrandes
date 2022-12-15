from utilidades.euclides_mcd_extendido import mcd_extendido
from utilidades.euclides_mcd import euclides_mcd

# Script con métodos relacionados al cálculo del máximo común divisor entre dos
# números y los coeficientes de Bézout que cumplen con la identidad de Bézout

def inversa_modular(a, m):
    gdc, x, y = mcd_extendido(a, m)
    return x if gdc == 1 else 0

def existe_inversa_modular(a, m):
    return euclides_mcd(a, m) == 1

def __lanzador__():
    a, b = 3, 11
    if existe_inversa_modular(a, b):
        print("Ls inversa modular multiplicativa es:", inversa_modular(a, b))
    else:
        print("La inversa modular no existe.")


if __name__ == "__main__":
    __lanzador__()
