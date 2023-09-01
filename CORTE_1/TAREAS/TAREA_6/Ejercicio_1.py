import random

numeros = [random.randint(1, 100) for _ in range(15)]

print("Números aleatorios sin ordenar:")
print(numeros)

numeros.sort()

print("Números ordenados de menor a mayor:")
print(numeros)
