from utilidades import tcr

def calcular_sistema(residuos):
    sistema = []
    for i in range(len(modulos_coprimos)):
        sistema.append([residuos[i], modulos_coprimos[i]])
    return sistema

def calcular_residuos(dividendo, modulos_coprimos):
    residuos = []
    for i in range(len(modulos_coprimos)):
        residuos.append(divmod(dividendo, modulos_coprimos[i])[1])
    return residuos

def calcular_productos(residuos_u, residuos_v, modulos_coprimos):
    residuos = []
    for i in range(len(modulos_coprimos)):
        residuos.append(divmod(residuos_u[i]*residuos_v[i], modulos_coprimos[i])[1])
    return residuos

def calcular_solucion(sistema):
    if tcr.existe_solucion(sistema):
        solucion = tcr.teorema_del_resto_chino(sistema)
        return solucion
    else:
        print("No existe solución para el sistema ingresado.")
        return 0

def mostrar_representacion_modular(numero, residuos):
    print("Representación modular de " + str(numero) + "\nes " + str(residuos))

def mostrar_sistema(residuos_u, residuos_v, modulos_coprimos):
    print("El sistema de congruencias formado es")
    for i in range(len(modulos_coprimos)):
        print("\tx ≡ {} mod {}".format(residuos_u[i] * residuos_v[i], modulos_coprimos[i]))

def mostrar_solucion(solucion, sistema):
    print("Se tiene que")
    print("x = {} (mod {})".format(solucion, tcr.calcular_producto_de_modulos(sistema)))
    print("Luego,\nla solución del sistema ingresado\nes", solucion)


# Números grandes de entrada
u = 227639655
v = 77829412

# Conjunto arbitrario de
# números enteros coprimos entre sí
modulos_coprimos = \
    [99, 97, 95, 91, 89, 83, 79, 74, 71]

# Residuos de los números grandes u y
# v con respecto a los módulos coprimos
residuos_u = calcular_residuos(
        u, modulos_coprimos)
residuos_v = calcular_residuos(
        v, modulos_coprimos)

# Residuos de los productos u_k*v_k,
# con respecto a los módulos coprimos
residuos_m = calcular_productos(
    residuos_u,
    residuos_v,
    modulos_coprimos)

# Se muestran las representaciones
# modulares de u y v
mostrar_representacion_modular(
        u, residuos_u)
mostrar_representacion_modular(
        v, residuos_v)

# Muestra el sistema
# de congruencias formado
mostrar_sistema(
    residuos_u,
    residuos_v,
    modulos_coprimos)

# Calcula el sistema de congruencias
# y muestra su solución
sistema = calcular_sistema(residuos_m)
solucion = calcular_solucion(sistema)
mostrar_solucion(solucion, sistema)


