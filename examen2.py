# Pedir la cantidad de elementos
cantidad = int(input("¿Cuántos elementos tendrá el arreglo? "))

# Crear una lista vacía
arreglo = []

# Pedir los elementos uno por uno
for i in range(cantidad):
    valor = input(f"Ingrese el elemento {i + 1}: ")
    arreglo.append(valor)

# Mostrar el arreglo original
print("Arreglo original:", arreglo)

# Invertir el arreglo (usando un método simple)
arreglo_invertido = list(reversed(arreglo))

# Mostrar el arreglo invertido
print("Arreglo invertido:", arreglo_invertido)
