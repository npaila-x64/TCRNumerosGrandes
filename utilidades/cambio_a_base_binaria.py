
# Convierte un número de base decimal a uno de base binaria
# Acepta como parámetros un número de base decimal y una base numérica

def convertir_numero_a_binario(numero: int):
    digitos = []
    while numero > 0:
        resto = numero % 2
        digitos.append(str(resto))
        numero = numero // 2
    digitos.reverse()
    return "".join(digitos)

def __lanzador__():
    numero= 12415512
    print(convertir_numero_a_binario(numero))


if __name__ == "__main__":
    __lanzador__()