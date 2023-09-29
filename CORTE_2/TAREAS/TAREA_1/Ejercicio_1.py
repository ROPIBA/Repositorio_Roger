import random
matriz = [[random.randint(1, 100) for _ in range(10)] for _ in range(5)]

for f in matriz:
    print(f)

mayor= matriz[0][0]
menor= matriz[0][0]

for f in matriz:
    for valor in f:
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor

print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
#no pude organizar la matriz de mayor a menor :)
