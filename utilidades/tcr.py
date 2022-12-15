from utilidades.inversa_modular import inversa_modular
from utilidades.euclides_mcd import euclides_mcd

# Script que calcula la solución de un sistema de congruencias
# a través del uso del teorema del resto chino, si es que existe

def teorema_del_resto_chino(sistema: list):
    sumatoria = 0
    for congruencia in sistema:
        N = 1
        for c in sistema:
            if c[1] == congruencia[1]:
                continue
            N *= c[1]
        inversa = inversa_modular(N, congruencia[1])
        sumatoria += congruencia[0] * N * inversa

    return sumatoria % calcular_producto_de_modulos(sistema)

def calcular_producto_de_modulos(sistema: list):
    producto_de_modulos = 1
    for congruencia in sistema:
        producto_de_modulos *= congruencia[1]
    return producto_de_modulos

def existe_solucion(sistema: list):
    for congruencia in sistema:
        for c in sistema:
            if c[1] == congruencia[1]:
                continue
            if euclides_mcd(congruencia[1], c[1]) != 1:
                return False
    return True

def __lanzador__():
    # El sistema de n números de congruencias se representa como una
    # matriz de n filas cuya primera columna es el coeficiente al lado
    # derecho de la congruencia y la segunda columna es el módulo
    sistema = []
    sistema.append([5, 7])
    sistema.append([6, 11])
    sistema.append([7, 13])

    if existe_solucion(sistema):
        solucion = teorema_del_resto_chino(sistema)
        print("La solución del sistema ingresado es:", solucion)
        print("Luego, se tiene que:")
        print("x = {} (mod {})".format(solucion, calcular_producto_de_modulos(sistema)))
    else:
        print("No existe solución para el sistema ingresado.")


if __name__ == "__main__":
    __lanzador__()
