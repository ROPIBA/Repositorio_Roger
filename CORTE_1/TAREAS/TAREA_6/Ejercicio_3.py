
numeros = []

while True:
    numero = int(input("Ingrese un número (ingrese un numero negstivo para terminar): "))
    
    
    if numero < 0:
        break
    
  
    numeros.append(numero)

print("Lista original:", numeros)


numeros_sin_duplicados = list(set(numeros))

print("Lista sin elementos duplicados:", numeros_sin_duplicados)
